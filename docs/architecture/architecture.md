# Architecture Documentation — Aaraksha

## System Overview

Aaraksha is a four-portal platform with a single shared backend. Each portal is a separate
Vite/React TypeScript application deployed independently on Vercel. The backend is a Node.js
Express application deployed on Render with a PostgreSQL database.

```
Tourist PWA         Govt Command Center     Guardian Portal      Aaraksha Sahayak
(aaraksha-tourist   (aaraksha-govt          (aaraksha-guardian   (aaraksha-rescuer
 .vercel.app)        .vercel.app)            .vercel.app)         .vercel.app)
     |                    |                       |                    |
     +--------------------+-----------------------+--------------------+
                                    |
                          Express API (Render, Singapore)
                          Node.js 22 / Express 4
                          Socket.IO 4.x (real-time)
                                    |
                          PostgreSQL 15 (Render, Singapore)
                          39 tables, 41 migrations
```

## Backend — Layer Structure

```
HTTP Request
    │
    ▼
Route File           (routes/*.js)         — URL pattern + middleware mount
    │
    ▼
Controller           (controllers/*.js)    — input validation, calls service
    │
    ▼
Service              (services/*.js)       — business logic, orchestration
    │
    ▼
Repository           (repositories/*.js)  — parameterized SQL queries only
    │
    ▼
pg Pool              (database/pool.js)   — raw PostgreSQL connection pool
    │
    ▼
PostgreSQL 15
```

**Invariants:**
- Business logic never in routes or repositories
- SQL never in services
- No string interpolation in SQL — parameterized queries ($1, $2, ...) only
- All errors thrown as `Error` objects with `.statusCode` → caught by `errorHandler.js`
- All responses go through `utils/response.js` (sendSuccess / sendError / sendPaginated)
- All logging through `pino` — zero `console.log` in the codebase

## Socket.IO Room Architecture

```
Server
├── Room: govt-dashboard
│   └── Members: authenticated govt users (JWT verified on Socket.IO connect)
│   └── Events received:
│       ├── SOS_RECEIVED    {sos, tourist, destination}
│       ├── SOS_RESOLVED    {sosId, resolvedBy, timestamp}
│       ├── RESCUE_ASSIGNED {sosId, team}
│       ├── DMS_TRIGGERED   {touristId, dmsId, location}
│       └── RESCUER_LOCATION_UPDATE {volunteerId, lat, lng}
│
├── Room: tourist-{touristId}
│   └── Members: tourist on login
│   └── Events received:
│       ├── TSI_UPDATED     {tsiScore, tsiLabel}
│       └── RESCUE_ASSIGNED {team, eta}
│
└── Room: guardian-{guardianToken}
    └── Members: anyone with the guardian token URL
    └── Events received:
        └── CHECKIN_UPDATE  {location, battery, eta, status}
```

## Cron Jobs

| Job | Schedule | Function |
|-----|----------|----------|
| DMS checker | Every 60 seconds | Query all ACTIVE DMS where `next_trigger_at <= NOW()`. Send warning if first overdue; auto-fire SOS if warning already sent and still overdue. |
| Weather updater | Every 60 minutes | Fetch current weather for all active-trip destination IDs from OWM. Upsert into `weather_cache`. |

## Security Stack

| Layer | Implementation |
|-------|---------------|
| Transport | HTTPS (Render + Vercel enforce) |
| CORS | Whitelist from `TOURIST_FRONTEND_URL`, `GOVT_FRONTEND_URL`, etc. env vars |
| Headers | `helmet()` — CSP, HSTS, X-Frame-Options, etc. |
| Rate limiting | `express-rate-limit` — auth: 5 req/15min, webhooks: 1000 req/15min, general: 100 req/15min |
| Auth | JWT HS256, algorithm-pinned, 24h expiry |
| Passwords | bcrypt rounds=12 |
| Govt ID | SHA-256 hash stored; last 4 digits only for display |
| SQL | Parameterized only — no template literals with user data |
| File uploads | Multer — 5MB max, jpeg/png/webp only, auth-checked before serving |
| Logging | PII fields masked: phone, JWT, password, Aadhaar/PAN, GPS at DEBUG level |

## Deployment Configuration

**Backend (Render `render.yaml`):**
```yaml
startCommand: npm run migrate && npm start
healthCheckPath: /health
```
Every deploy auto-applies pending migrations. Health check at `/health` returns `{status: "ok"}`.

**Frontend (Vercel):**
- 4 separate Vercel projects, each with its own `vercel.json`
- GitHub integration: push to `main` → all 4 deploy independently
- No shared build — each portal is a standalone Vite app

**CI (GitHub Actions):**
- Backend: `vitest run` against an ephemeral PostgreSQL (matrix)
- Frontend: `tsc -b` across all 4 apps (matrix)
- Triggers: every push and PR to `main`

## Frontend Architecture (per portal)

```
src/
├── main.tsx          ← Vite entry, React root, Router, QueryClient
├── api/
│   ├── client.ts     ← Single axios instance + JWT interceptor
│   └── *.api.ts      ← Domain API files (sos.api.ts, trip.api.ts, ...)
├── store/
│   └── *.store.ts    ← Zustand stores (auth, trip, safety)
├── hooks/
│   └── use*.ts       ← Custom hooks wrapping TanStack Query + Zustand
├── pages/            ← React Router page components
├── components/       ← Reusable components + shadcn/ui
├── types/            ← TypeScript interfaces
└── lib/
    ├── db.ts         ← Dexie.js IndexedDB schema (tourist only)
    └── utils.ts      ← cn() + formatters
```

**State management rules:**
- Server data (API responses) → TanStack Query (never Zustand)
- Global app state (auth token, active trip) → Zustand
- Form state → React Hook Form
- Local UI state (modal open, tab) → useState
- Offline persistence → Dexie.js IndexedDB

## Key Algorithms

### TSI — Worst-Stop-Wins

The Travel Safety Index uses a "worst stop drives the score" rule instead of averaging.
Rationale: if a 7-day trip has 6 easy days in Guwahati and 1 extreme day on a Tawang winter
pass, averaging would show a misleadingly safe score. The worst stop's penalty dominates.

```
score = 100
score += travelTypeDelta[travelType]    // SOLO: -12, ADVENTURE: -15
score += durationPenalty               // >14 days: -5, >30 days: -10
score += seasonPenalty                 // June-Sept: -10
score -= max(stopPenalties)            // WORST STOP only
score = clamp(score, 10, 100)
```

### SOS Cluster Detection (Anomaly Service)

Uses Haversine distance formula to group SOS events within a configurable radius
(default 10km) within a configurable time window (default 24h). If a cluster exceeds
a threshold size, a `safety_anomaly` row is inserted and surfaced on the govt dashboard.

### Checkpoint Hash Chain

Each checkpoint scan generates a hash of: `{tripId}|{checkpointId}|{timestamp}|{prevHash}`.
The chain is verifiable — tampering with any scan invalidates all subsequent hashes.

### Rescue Readiness Score

Six boolean items → percentage:
```
emergencyContacts set? + bloodGroup recorded? + govtId complete? +
dmsEnabled? + tsiReviewed? + offlineMaps acknowledged?
= trueCount / 6 * 100
```
