<div align="center">

# 🛡️ AARAKSHA

### Smart Tourism Safety Platform · Northeast India

**SIH 2026 · Problem Statement PS 26204 · Travel & Tourism**

---

<table>
<tr>
<td align="center">

### 🔐 PRIVATE PRODUCTION CODEBASE

The complete production implementation is maintained in a **private repository** for security and controlled access.

**[→ Request / View Codebase Access](https://github.com/aryanf192811-eng/Aaraksha)**

</td>
</tr>
</table>

> **This repository** is the **Public Evaluation, Documentation & Proof-of-Work Repository**  
> containing architecture, screenshots, implementation evidence, API contracts, and QA records.

---

![Backend](https://img.shields.io/badge/Backend-Node.js%2022%20%2B%20Express-339933?style=flat-square&logo=node.js)
![Database](https://img.shields.io/badge/Database-PostgreSQL%2015-4169E1?style=flat-square&logo=postgresql)
![Frontend](https://img.shields.io/badge/Frontend-React%2018%20%2B%20TypeScript-3178C6?style=flat-square&logo=react)
![Portals](https://img.shields.io/badge/Portals-4%20Deployed-10B981?style=flat-square)
![Tables](https://img.shields.io/badge/DB%20Tables-33-F59E0B?style=flat-square)
![Endpoints](https://img.shields.io/badge/API%20Endpoints-146-8B5CF6?style=flat-square)
![Tests](https://img.shields.io/badge/Postman%20Assertions-331-22C55E?style=flat-square)
![Migrations](https://img.shields.io/badge/DB%20Migrations-36-EF4444?style=flat-square)

</div>

---

## Table of Contents

| # | Section |
|---|---------|
| 1 | [Why Aaraksha — The Problem](#-why-aaraksha--the-problem) |
| 2 | [PS 26204 Alignment](#-ps-26204-alignment) |
| 3 | [What We Built — At a Glance](#-what-we-built--at-a-glance) |
| 4 | [System Architecture](#-system-architecture) |
| 5 | [Four Portals](#-four-portals) |
| 6 | [Safety Engine](#-safety-engine--the-core-innovation) |
| 7 | [AI + Deterministic System Design](#-ai--deterministic-system-design) |
| 8 | [Tourism & Local Operator Ecosystem](#-tourism--local-operator-ecosystem) |
| 9 | [Offline & Resilience Architecture](#-offline--resilience-architecture) |
| 10 | [Government & Guardian Workflows](#-government--guardian-workflows) |
| 11 | [Tech Stack](#-tech-stack) |
| 12 | [Database — 33 Tables](#-database--33-tables-36-migrations) |
| 13 | [API Surface — 146 Endpoints](#-api-surface--146-endpoints) |
| 14 | [Testing & Security Evidence](#-testing--security-evidence) |
| 15 | [Screenshots](#-screenshots) |
| 16 | [Demo & Deployment](#-demo--deployment) |
| 17 | [Project Structure](#-project-structure) |
| 18 | [Setup & Run Locally](#-setup--run-locally) |
| 19 | [Known Limitations](#-known-limitations) |
| 20 | [Future Roadmap](#️-future-roadmap) |

---

## 🚨 Why Aaraksha — The Problem

Northeast India receives millions of tourists annually. But it is one of India's most logistically complex regions to travel safely:

| Challenge | Reality |
|-----------|---------|
| **Connectivity blackspots** | Large zones with zero mobile signal in Arunachal, Nagaland, Sikkim |
| **Terrain extremes** | Altitudes up to 5,000m+, landslide-prone monsoon routes |
| **Inner Line Permit zones** | Restricted areas requiring advance documentation |
| **Fragmented rescue** | No unified SOS routing to official teams AND local responders simultaneously |
| **No family visibility** | Families have no real-time view of a tourist's location or status |
| **Local economy gap** | Verified local operators, homestays and guides have no official discovery channel |

**No single platform existed** that addressed tourist safety, government situational awareness, family peace-of-mind, responder coordination, and local tourism enablement together.

---

## 🎯 PS 26204 Alignment

> *"Design a comprehensive travel safety and information platform for tourists visiting Northeast India, integrating real-time safety alerts, emergency response coordination, local tourism promotion and information services including hotels, travel and others."*

| PS Requirement | Aaraksha Implementation |
|----------------|------------------------|
| Real-time safety alerts | TSI (Travel Safety Index) — rule-based score updated every 60 min via OWM cron |
| Emergency response coordination | SOS → Socket.IO → Govt dashboard → Rescue team + Volunteer dispatch |
| Local tourism promotion | Govt-verified Local Operators panel inside the trip planner |
| Tourist information services | AI-powered itinerary builder grounded in real destination/route data |
| Hotels, travel and others | `local_operators` table: HOTEL / HOMESTAY / GUIDE / EXPERIENCE / ARTISAN |
| Northeast India focus | 30 NER destinations seeded (all 8 states) |

---

## ✅ What We Built — At a Glance

```
┌─────────────────────────────────────────────────────────────────┐
│                        AARAKSHA                                 │
│         Smart Tourism Safety · Northeast India                  │
├──────────────┬───────────────┬──────────────┬───────────────────┤
│  TOURIST PWA │  GOVT COMMAND │   GUARDIAN   │  RESCUER APP      │
│              │    CENTER     │   PORTAL     │                   │
│  Plan trips  │  Live ops map │  PIN-gated   │  Delivery-partner │
│  AI itinary  │  SOS triage   │  family view │  style dispatch   │
│  SOS trigger │  Rescue assign│  Live map    │  MapLibre routing │
│  Dead Man's  │  Analytics    │  Check-in    │  Points & rep     │
│  Switch      │  Risk overview│  timeline    │  system           │
│  Offline SOS │  Local ops    │              │                   │
│  Check-ins   │  verification │              │                   │
└──────────────┴───────────────┴──────────────┴───────────────────┘
              Socket.IO real-time events across all four portals
              PostgreSQL (33 tables) + node-cron + Twilio + Gemini
```

### Key Numbers (verified against live codebase)

| Metric | Value |
|--------|-------|
| Portals | 4 deployed |
| API endpoints | 146 across 19 route groups |
| Database tables | 33 (+ pgmigrations) |
| DB migrations | 36 incremental |
| Postman assertions | 331 across 149 requests / 26 folders |
| Backend vitest tests | 56 passing |
| Frontend tests | ~95 across all 4 apps |
| QA phases | 13 (12 adversarial + 1 final acceptance) |
| Security defects found & fixed | 8 (across 2 dedicated passes) |

---

## 🏗️ System Architecture

<div align="center">

![System Architecture](./docs/architecture/system-architecture.png)

*Four portals, shared backend, real-time socket rooms, PostgreSQL*

</div>

### Request Flow — SOS Event (Mermaid)

```mermaid
sequenceDiagram
    participant Tourist as Tourist PWA
    participant API as Express API
    participant DB as PostgreSQL
    participant Socket as Socket.IO
    participant Govt as Govt Dashboard
    participant Vol as Rescuer App
    participant SMS as Twilio

    Tourist->>API: POST /api/sos {category, lat, lng}
    API->>DB: INSERT sos_events (ACTIVE)
    API->>SMS: sendSMS (try/catch — never blocks response)
    API->>Socket: emit SOS_RECEIVED → govt-dashboard room
    Socket->>Govt: live pin appears on map
    Govt->>API: POST /api/govt/rescue-assignments
    API->>Socket: emit RESCUE_ASSIGNED → tourist-{id}
    API->>Socket: emit volunteer alert → nearby rescuers
    Socket->>Vol: dispatch notification
    Tourist->>Tourist: RescueTrackingCard shows live ETA
```

### Dead Man's Switch Flow (Mermaid)

```mermaid
flowchart TD
    A[Tourist enables DMS\nsets interval e.g. 2 hours] --> B[node-cron checks every 60s]
    B --> C{next_trigger_at <= NOW?}
    C -- No --> B
    C -- Yes --> D{Warning already sent?}
    D -- No --> F[Send SMS warning\nupdate warning_sent_at]
    F --> G{Check-in received\nbefore timeout?}
    G -- Yes --> I[Reset DMS]
    G -- No --> J[Auto-fire SOS\ntrigger_type = DMS]
    D -- Yes, still overdue --> J
    J --> K[Full SOS pipeline: DB → Socket → Rescue]
```

### Architecture Principles

| Principle | Implementation |
|-----------|---------------|
| Graceful degradation | Every external service fails silently — SOS path never blocked |
| Real-time everywhere | Socket.IO rooms: `govt-dashboard`, `tourist-{id}`, `guardian-{token}` |
| Offline-first safety | DMS fires without app open; SMS fallback via Twilio inbound webhook |
| Security by design | JWT HS256 algo-pinned, bcrypt-12, parameterized SQL only, Helmet, rate limiting |
| No ORMs | Raw `pg` pool — full SQL control, no abstraction surprises |

---

## 📱 Four Portals

### 1 · Tourist PWA (Mobile-First · Amber Theme)

| Feature | What's Implemented |
|---------|-------------------|
| **AI Trip Planner** | Natural language → Gemini extracts intent → deterministic scorer ranks stops → Gemini narrates. Editable via follow-up prompts. |
| **TSI Score** | Rule-based 0–100, 6 factors, worst-stop logic, updated hourly via OWM. |
| **SOS** | One-tap, 5 categories, GPS, Socket.IO + SMS. |
| **Dead Man's Switch** | User-configured interval, node-cron every 60s, auto-SOS on timeout. |
| **Check-ins** | Manual or DMS-reset. GPS + battery%. Live update to Guardian via socket. |
| **Guardian Link** | UUID token, shareable URL, PIN-gated access. |
| **Destination Browser** | 30 NER destinations: reviews, news, TSI scores, operator listings. |
| **Scam Reports** | Community reporting: OVERCHARGING / FAKE_GUIDE / THEFT / OTHER. |
| **Incident Reports** | Photo-evidence supported filing. |
| **Offline SOS** | SMS fallback with structured format. Works in zero-internet zones. |
| **Journey Passport** | PDFKit 9-section PDF with QR code. |
| **Push Notifications** | Web-push VAPID. |
| **Trust Score** | Anti-abuse: false alarms reduce score. Emergency SOS always open regardless. |
| **PWA** | Installable, offline-capable, service worker. |

**Pages (12+ screens):**
```
LandingPage · DashboardPage
auth/  → RegisterPage · LoginPage · OTPPage
trips/ → CreateTripPage · TripDetailPage · ItineraryPage
safety/ → SOSPage · CheckinPage · CheckpointPassPage · IncidentReportPage · AdvisoryPage · NewsFeedPage
destinations/ → DestinationListPage · DestinationDetailPage
community/ → CommunityPage
profile/ → ProfilePage · DataRightsPage
```

---

### 2 · Government Command Center (Desktop · Emerald Theme)

| Feature | What's Implemented |
|---------|-------------------|
| **Live Ops Map** | Leaflet + MapLibre (2D+3D toggle). Real-time SOS pins animate on arrival. |
| **SOS Management** | Full triage: assign rescue team, assign volunteer, resolve, false alarm, chat. |
| **Risk Overview** | District heatmap. Anomaly detection: cluster and frequency anomalies. |
| **Volunteer Verification** | Review and approve volunteers before dispatch access. |
| **Local Operators** | Verify/reject local tourism providers — gated before tourist visibility. |
| **Analytics** | Recharts: SOS trends, resolution times, district risk. |
| **E-FIR Queue** | Review tourist-filed incident reports. |
| **Checkpoint Scan** | Hash-chain verified tourist checkpoints. |
| **Trust Appeals** | Review tourist trust-score appeals. |
| **RBAC** | ADMIN / DISTRICT_OFFICER / RESCUE_COORDINATOR — route-level enforcement. |

**Pages (11 screens):**
```
GovtLoginPage · DashboardPage · LiveMapPage · SOSManagementPage · RiskOverviewPage
VolunteersPage · LocalOperatorsPage · AnalyticsPage · IncidentQueuePage
CheckpointScanPage · TrustAppealsPage
```

---

### 3 · Guardian Portal (Public · PIN-Gated)

| Feature | What's Implemented |
|---------|-------------------|
| PIN-gated access | UUID token in URL + tourist-set 4-digit PIN |
| Live tracking map | Leaflet with last known GPS + battery % |
| Check-in timeline | Chronological log with notes |
| SOS alert view | Live rescue assignment status |
| Socket.IO | `CHECKIN_UPDATE` events push to `guardian-{token}` room |

---

### 4 · Rescuer App (Mobile · Teal Theme · Delivery-Partner Style)

| Feature | What's Implemented |
|---------|-------------------|
| Govt verification gate | Usable only after govt marks `is_verified = true` |
| Status toggle | AVAILABLE / OFFLINE |
| Dispatch alerts | Real-time Socket.IO push. Accept or decline. |
| Active Job | MapLibre GL + OSRM routing. Live navigation to SOS site. |
| Tourist ↔ Rescuer chat | Real-time in-app messaging. Unread indicator. |
| Points system | 10 pts respond, 25 pts complete |
| Operator dashboard | Local operators log in to view verification status |
| Handoff flow | Formal volunteer → official rescue team handoff |

---

## 🔒 Safety Engine — The Core Innovation

### Travel Safety Index (TSI) — 100% Deterministic, Zero AI

```
TSI Score (0–100, higher = safer)
│
├── Travel type delta      (SOLO: -12 | ADVENTURE: -15 | FAMILY: 0)
├── Duration penalty       (>14 days: -5 | >30 days: -10)
├── NER monsoon season     (June–Sept: -10)
└── Worst-stop penalty  ← NEVER averaged — worst stop drives the score
    ├── Connectivity       (NONE: -20 | POOR: -10 | MODERATE: -4)
    ├── Medical access     (hospital >50km: -15 | >20km: -8 | <5km: +5)
    ├── Altitude           (>4000m: -20 | >3000m: -10 | >2000m: -4)
    ├── Zone type          (RESTRICTED: -25 | HIGH_RISK: -20 | ILP_REQUIRED: -10)
    ├── Difficulty         (EXTREME: -25 | HARD: -15 | MODERATE: -5)
    └── Live weather       (STORM: -20 | HEAVY_RAIN: -15 | SNOW: -10 | FOG/RAIN: -5)
                                   ↑
                   Updated every 60 min via OpenWeatherMap cron
                   (stored in weather_cache, never inline API call)

Labels: ≥80 Low Risk · 60–79 Moderate Risk · 40–59 High Risk · <40 Extreme Risk
```

### Anomaly Detection

`anomaly.service.js` detects:
- **Cluster anomalies:** Unusual geographic SOS density (Haversine distance-based)
- **Frequency anomalies:** SOS spike in a district rolling time window
- Stored in `safety_anomalies`, surfaced on govt Risk Overview

### Rescue Readiness Score (0–100%)

6-item pre-trip checklist: emergency contacts · blood group · govt ID verified · DMS enabled · TSI reviewed · offline maps acknowledged

---

## 🤖 AI + Deterministic System Design

> The boundary between AI and deterministic logic is load-bearing, not decorative.

| What | System | Why |
|------|--------|-----|
| Routing, ranking, cost estimation | `travelScoring.service.js` — pure deterministic JS | Auditable, testable, reproducible |
| Intent extraction from natural language | Gemini API | Language understanding |
| Journey narrative (prose) | Gemini API | Natural prose for an already-scored plan |
| TSI scoring | 100% rule-based JS | Judge-auditable, zero hallucination risk |
| DMS / SOS firing | node-cron + PostgreSQL | Zero-latency, zero AI in safety path |
| Safety recommendations | Rule-based in `tsi.service.js` | Deterministic, consistent |
| Packing list | Gemini API + static fallback | AI-enhanced, always available |
| Help chatbot | Gemini API, grounded in live data | Real data, not hallucinated |

**Gemini integration details:**
- Direct REST to `generativelanguage.googleapis.com` (SDK had 59s stall vs 1.2s raw REST — measured, fixed)
- 30s timeout with `AbortController`
- Every Gemini feature has a graceful static fallback
- Model: `gemini-3.5-flash-lite`

---

## 🏨 Tourism & Local Operator Ecosystem

A direct PS 26204 requirement. Aaraksha implements verified local operator discovery:

```
Tourist plans trip to Tawang
       ↓
Backend attaches verified local_operators for each destination stop
       ↓
Tourist sees: "Tawang Homestay Network ★4.2" | "Snow Leopard Trek Guide ★4.7"
       ↓
Only visible if govt-verified (is_verified = true, verified_by = govtUserId)
```

| Category | Description |
|----------|-------------|
| HOTEL | Registered accommodation providers |
| HOMESTAY | Community homestay operators |
| GUIDE | Licensed local trek guides |
| EXPERIENCE | Cultural immersion, village walks |
| ARTISAN | Handicraft workshops, weavers |

**Provenance discipline:** every operator row requires a mandatory `source` citation — no unsourced rows allowed by the DB schema constraint.

**Tourist points:** tourists earn points for reviewing operators → drives ecosystem engagement.

---

## 📡 Offline & Resilience Architecture

### The Offline SOS Path (Zero Internet Required)

```
1. Tourist has zero internet
2. App generates pre-filled SMS:
   AARAKSHA_SOS|ID:{tourist_id}|LAT:{lat}|LNG:{lng}|CAT:MEDICAL|BATT:{%}|TIME:{unix_ts}
3. Sent to Twilio number (SMS works on 2G/edge when data fails)
4. Twilio inbound webhook → POST /api/webhooks/twilio-inbound
5. Regex parser extracts all fields
6. Inserts into sos_events as trigger_type = INBOUND_SMS
7. Full pipeline continues: Socket.IO → Govt → Rescue assignment
```

GPS coordinates come from the device's satellite GPS radio — works without mobile data.

### NTN Simulation Channel

`ntn_messages` table + `/api/ntn` route simulates a Near-Term-Network satellite mesh channel — proof-of-concept that the platform is architected for alternative comms beyond SMS.

### Graceful Degradation

| Service | If unavailable |
|---------|---------------|
| Twilio | SMS skipped; SOS saves to DB and fires Socket.IO |
| Gemini API | Static fallback content |
| OpenWeatherMap | Weather factor drops out; other 5 TSI factors still compute |
| VAPID/Push | Silently no-ops |

---

## 🏛️ Government & Guardian Workflows

### Complete SOS Lifecycle

```
1. SOS RECEIVED        Tourist triggers SOS (manual/DMS/SMS)
         ↓
2. REAL-TIME ALERT     Socket.IO SOS_RECEIVED → govt-dashboard
                       Animated pin appears on live map
         ↓
3. TRIAGE              Officer views tourist profile, destination, TSI score
                       Sees nearest hospital name + distance
         ↓
4. RESCUE ASSIGNMENT   Assign official team (POLICE/MEDICAL/FOREST/NDRF)
                       Optionally assign verified volunteer
         ↓
5. EN ROUTE            Rescuer navigates via MapLibre + OSRM
                       Govt sees rescuer's live location
                       Tourist sees "Rescue en route" + ETA
         ↓
6. RESOLUTION          Govt marks RESOLVED / FALSE_ALARM
                       Socket.IO SOS_RESOLVED → tourist + guardian
                       Points awarded to volunteer (25 pts)
```

### Guardian Family Tracking

```
Tourist shares URL: https://aaraksha-guardian.vercel.app/{guardianToken}
Family visits URL → PIN prompt (4-digit PIN set by tourist)
PIN correct → sees:
  • Live map: last known GPS location + battery %
  • Check-in timeline with notes
  • SOS alert banner (if active) + rescue status
  • Real-time updates via Socket.IO guardian-{token} room
```

---

## 🔧 Tech Stack

### Backend

| | Technology |
|--|-----------|
| Runtime | Node.js 22 |
| Framework | Express.js |
| Database | PostgreSQL 15 (raw pg pool, no ORM) |
| Real-time | Socket.IO 4.x |
| Auth | JWT HS256 (algo-pinned) + bcrypt (12 rounds) |
| Scheduling | node-cron (DMS: 60s, weather: 60min) |
| SMS | Twilio (outbound + inbound webhook) |
| AI | Google Gemini API (gemini-3.5-flash-lite) |
| PDF | PDFKit (Journey Passport) |
| Push | web-push (VAPID) |
| Validation | Zod + controller-level checks |
| Logging | pino (structured JSON, PII masked) |
| Security | Helmet + express-rate-limit (auth: 5/15min, general: 100/15min) |
| Migrations | node-pg-migrate (36 migrations) |
| Testing | vitest + supertest |

### Frontend (all 4 portals)

| | Technology |
|--|-----------|
| Build | Vite 5+ |
| Framework | React 18 (concurrent mode) |
| Language | TypeScript 5 (strict mode) |
| Styling | Tailwind CSS 3.x |
| Components | shadcn/ui (3 portals) · Hand-rolled Tailwind (Rescuer) |
| Routing | React Router v6 |
| Global state | Zustand |
| Server data | TanStack Query v5 |
| Forms | React Hook Form |
| Offline storage | Dexie.js (IndexedDB) |
| Maps | react-leaflet (standard) + MapLibre GL JS (rescue/3D) |
| Routing engine | OSRM public demo server (no key) |
| Charts | Recharts |
| PWA | vite-plugin-pwa + service worker (Tourist) |
| HTTP | axios (JWT interceptor per portal) |

### DevOps

| | Technology |
|--|-----------|
| Backend | Render (Singapore, free tier) |
| Frontend | Vercel (4 separate projects, GitHub integration) |
| CI | GitHub Actions — vitest + tsc matrix |
| Migrations | Auto-run on every deploy (`npm run migrate && npm start`) |

---

## 🗄️ Database — 33 Tables, 36 Migrations

| Area | Tables |
|------|--------|
| **Identity & Auth** | `tourists`, `govt_users`, `otp_verifications`, `data_deletion_requests` |
| **Trips & Travel** | `trips`, `trip_members`, `destinations`, `typical_routes`, `curated_itineraries`, `destination_news`, `destination_reviews`, `weather_cache`, `local_operators`, `local_operator_reviews` |
| **Safety Core** | `checkins`, `dead_mans_switches`, `sos_events`, `sos_cluster_flags`, `safety_anomalies`, `tourist_locations` |
| **Rescue Network** | `rescue_teams`, `rescue_assignments`, `volunteers`, `volunteer_dispatches` |
| **Incidents & Community** | `incident_reports`, `scam_reports`, `checkpoint_scans` |
| **Trust & Messaging** | `tourist_trust_events`, `tourist_trust_appeals`, `messages` |
| **Offline / NTN / Push** | `inbound_sos_sms`, `ntn_messages`, `push_subscriptions` |

**36 incremental migrations** from `001_initial_schema.js` to `036_vehicle_rental_tour_operator_categories.js`.

### Key Schema Decisions

| Decision | Reason |
|----------|--------|
| `govt_id_hash` = SHA-256 | Govt ID never stored plaintext |
| `sos_events.trigger_type` = MANUAL/DMS/INBOUND_SMS | Tracks how SOS was initiated |
| `dead_mans_switches.next_trigger_at` | Computed target, checked by cron every 60s |
| `local_operators.is_verified` | Govt gate before tourist visibility |
| `typical_routes.source` NOT NULL | Mandatory provenance, no unsourced rows |
| Aadhaar Verhoeff checksum | UIDAI's actual 12th-digit algorithm, not format regex |

---

## 🔌 API Surface — 146 Endpoints

**19 route groups:**
```
/auth   /tourists   /trips   /sos   /dms   /ntn   /travel-planner
/checkins   /destinations   /local-operators   /scam-reports
/incidents   /packing   /journey-passport   /govt   /volunteers
/webhooks   /push   /help
```

**Standard response shapes:**
```json
{ "success": true,  "message": "SOS triggered", "data": { ... } }
{ "success": false, "message": "Tourist not found", "errors": null }
{ "success": true,  "data": [...], "pagination": { "total":42, "page":1 } }
```

See [`docs/api/api-reference.md`](./docs/api/api-reference.md) for full endpoint reference.

---

## 🧪 Testing & Security Evidence

### Coverage

| Layer | Detail |
|-------|--------|
| Backend unit + integration | 56 tests — TSI scoring, itinerary scoring, crypto, NTN simulator, auth, planner |
| Frontend (4 apps) | ~95 tests |
| Postman/Newman | 331 assertions, 149 requests, 26 folders |
| CI | GitHub Actions — backend vitest + frontend tsc matrix on every push |
| Scoring benchmark | `tests/eval/travelPlanner.benchmark.js` — 6/6 fixed queries passing |

### Security Audit — 8 Real Defects Found & Fixed

**Pass 1 — General adversarial (5 defects):**

| Finding | Fix Applied |
|---------|-------------|
| Rate limiter defined but not wired | Wired; budget no longer shared across unrelated routes |
| Concurrent SOS resolve race condition | Atomic DB-level guard |
| Transaction rollback on FK violation | Confirmed rollback; no surviving row |
| External service unconfigured → crash | All degrade gracefully |
| SQLi-shaped phone input → unhandled 500 | Clean 400 |

**Pass 2 — Authentication focus (3 defects):**

| Finding | Fix Applied |
|---------|-------------|
| `/auth/govt/register` created SUPER_ADMIN unauthenticated | Gated behind `authenticateGovt + requireGovtRole(SUPER_ADMIN)` |
| `jwt.verify()` without algorithm pinning | All calls pin `algorithms: ['HS256']` |
| OTP rate limiter on wrong budget | Reads same config; dev `debugOtp` fallback added |

**SQL injection held throughout** (`' OR 1=1 --`, `DROP TABLE`, `UNION SELECT`). Parameterized queries only.

### 12-Phase QA Process

| Phase | Focus | Result |
|-------|-------|--------|
| 1 | System audit | PASS WITH ISSUES |
| 2 | Backend/API/DB | PASS WITH ISSUES |
| 3 | Tourist PWA | PASS WITH ISSUES |
| 4 | Government Portal | PASS WITH ISSUES |
| 5 | Guardian Portal | PASS WITH ISSUES |
| 6 | Rescuer App | PASS WITH ISSUES |
| 7 | Cross-portal E2E | PASS WITH ISSUES |
| 8 | Offline/Resilience | PASS WITH ISSUES |
| 9 | Security Audit | PASS WITH ISSUES |
| 10 | Real-time Consistency | PASS WITH ISSUES |
| 11 | UI/UX QA | PASS WITH ISSUES |
| 12 | Regression | **PASS** |
| 13 | Final Acceptance | **PASS ✅** |

**Zero P0/P1 issues open. 20+ real defects found and fixed.**

Full reports: [`docs/testing/`](./docs/testing/)

---

## 📸 Screenshots

### Tourist Portal

| Dashboard | Destination Detail |
|-----------|-------------------|
| ![Dashboard](./screenshots/tourist/01_tourist_dashboard.png) | ![Destination](./screenshots/tourist/02_destination_detail.png) |
| *Home with TSI badge and quick actions* | *Destination with reviews, operators, news* |

| AI Planner Prompt | AI Plan Confirmation |
|------------------|---------------------|
| ![AI Prompt](./screenshots/tourist/03_ai_assistant_prompt.png) | ![AI Confirm](./screenshots/tourist/04_ai_confirm_screen.png) |
| *Natural language trip planning* | *Review intent before generating plan* |

| Built Itinerary | Safety Center |
|----------------|---------------|
| ![Itinerary](./screenshots/tourist/05_built_itinerary.png) | ![Safety](./screenshots/tourist/06_safety_center.png) |
| *AI-generated + deterministically scored plan* | *SOS, DMS, check-in hub* |

| Guardian Link | Trip Creation |
|--------------|---------------|
| ![Guardian](./screenshots/tourist/07_guardian_link_source.png) | ![Dates](./screenshots/tourist/verify_step1_dates.png) |
| *Share tracking URL with family* | *Trip date selection step* |

---

### Guardian Portal

| PIN Gate | Live Tracking |
|----------|--------------|
| ![PIN](./screenshots/guardian/08_guardian_pin_gate.png) | ![Tracking](./screenshots/guardian/09_guardian_live_tracking.png) |
| *4-digit PIN gate (set by tourist)* | *Live map + check-in timeline* |

---

### Government Command Center

| Login | Dashboard |
|-------|-----------|
| ![Login](./screenshots/govt/10_govt_login.png) | ![Dashboard](./screenshots/govt/11_govt_dashboard.png) |
| *Secure govt officer login* | *Ops command center with live stats* |

| Live Ops Map | Local Operators Verification |
|-------------|------------------------------|
| ![Map](./screenshots/govt/12_govt_live_map.png) | ![Operators](./screenshots/govt/13_govt_local_operators.png) |
| *Leaflet + MapLibre live SOS pins* | *Verify local tourism providers* |

| SOS Management | Verified Operators (Tawang) |
|---------------|---------------------------|
| ![SOS](./screenshots/govt/14_govt_sos_management.png) | ![Tawang](./screenshots/govt/verify_tawang_operators.png) |
| *Full SOS triage and rescue assignment* | *Verified operators in tourist planner* |

---

### Rescuer App

| Login | Home / Status | Incident Detail |
|-------|--------------|-----------------|
| ![Login](./screenshots/rescuer/15_rescuer_login.png) | ![Home](./screenshots/rescuer/16_rescuer_home.png) | ![Incident](./screenshots/rescuer/17_rescuer_incident_detail.png) |
| *Govt-verified rescuer login* | *Status toggle + live dispatches* | *SOS detail + MapLibre navigation* |

---

## 🚀 Demo & Deployment

| Portal | Live URL |
|--------|----------|
| Tourist PWA | https://aaraksha-tourist.vercel.app |
| Government Command Center | https://aaraksha-govt.vercel.app |
| Guardian Portal | https://aaraksha-guardian.vercel.app |
| Rescuer App | https://aaraksha-rescuer.vercel.app |

> ⚠️ Backend is on Render free tier. Ping `/health` ~1 minute before a demo to avoid cold-start delay.

**Demo accounts (Vadodara/Parul University):**
- Tourist: Meera Shah — active trip, DMS enabled
- Rescuer: Rajesh Solanki — verified, available
- Rescue Team: "Parul University Response Team"

Full walkthrough: [`docs/deployment/demo-guide.md`](./docs/deployment/demo-guide.md)

---

## 📁 Project Structure

```
aaraksha/                            ← Private production repo
├── backend/
│   ├── src/
│   │   ├── app.js                   ← Express + middleware stack
│   │   ├── server.js                ← HTTP + Socket.IO init
│   │   ├── routes/                  ← 20 route files
│   │   ├── controllers/             ← One per route group
│   │   ├── services/                ← 38 service files (business logic)
│   │   ├── repositories/            ← Parameterized SQL query layer
│   │   ├── middleware/              ← auth.js + errorHandler.js
│   │   ├── socket/                  ← Rooms + emitters
│   │   ├── cron/                    ← DMS (60s) + weather (60min)
│   │   ├── migrations/              ← 36 node-pg-migrate files
│   │   └── utils/                   ← response + logger + crypto + geo
│   ├── scripts/                     ← seed + preflight + trainRiskModel
│   ├── tests/unit/ integration/ eval/
│   └── postman/                     ← 331 assertions
├── frontend/
│   ├── tourist/   ← 12+ screens, amber, PWA, Dexie.js
│   ├── govt/      ← 11 screens, emerald, desktop
│   ├── guardian/  ← tracking + PIN gate, public
│   └── volunteer/ ← 5 screens, teal, dispatch
└── docs/          ← Architecture + 13 QA reports
```

---

## ⚙️ Setup & Run Locally

> Full codebase requires access to the [private repo](https://github.com/aryanf192811-eng/Aaraksha).

```bash
# Backend
cd backend
cp .env.example .env        # Fill DATABASE_URL minimum; others degrade gracefully
npm install
npm run migrate             # All 36 migrations
npm run seed                # 30 NER destinations + demo accounts
npm run dev                 # Port 5000

# Each frontend (run separately)
cd frontend/tourist  && npm install && npm run dev    # :5173
cd frontend/govt     && npm install && npm run dev    # :5174
cd frontend/guardian && npm install && npm run dev    # :5175
cd frontend/volunteer && npm install && npm run dev   # :5176

# Tests
cd backend && npm test
```

**Minimum env vars:**
```
DATABASE_URL=postgresql://user:pass@localhost:5432/aaraksha
JWT_SECRET=your-secret-min-32-chars
PORT=5000
# All external service keys optional — each degrades gracefully when absent
```

---

## ⚠️ Known Limitations

| Limitation | Detail |
|-----------|--------|
| Rate limiting is in-memory | Resets on restart; won't coordinate across load-balanced instances (Redis is the upgrade) |
| No array-field size caps | Trip stops, packing items have no application-level length limit |
| E-FIR photo auth | Evidence photos served without auth (mitigated: UUIDs are unguessable) |
| No content moderation API | Community feed has no delete/mod endpoint yet |
| Guardian token no auto-renewal | Documented product gap, not a bug |
| Render free-tier cold starts | 20–30s delay after idle. Not an app bug — platform behavior. |

---

## 🗺️ Future Roadmap

| Feature | Description |
|---------|-------------|
| Real NTN integration | Replace simulated channel with actual satellite mesh |
| Offline maps (MBTiles) | Full offline navigation for key NER districts |
| Multi-language expansion | Khasi, Mizo, Manipuri, Assamese translations |
| Redis-backed rate limiting | Stateless, multi-instance safe |
| E-FIR photo auth | Presigned URL or auth-gated serving |
| Guardian token renewal | Auto-refresh with tourist notification |
| Newman in CI | `newman run` in GitHub Actions |

---

<div align="center">

---

### 🔐 Private Production Codebase

The complete production implementation is in a private repository for security.

**[→ Request / View Codebase Access](https://github.com/aryanf192811-eng/Aaraksha)**

*This is the Public Evaluation Repository · Documentation · Architecture · Proof of Work*

---

**Built for SIH 2026 · PS 26204 · Smart Tourism Safety · Northeast India**

</div>
