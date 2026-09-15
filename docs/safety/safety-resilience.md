# Safety & Resilience Architecture — Aaraksha

## Design Principle: Safety Path Is Never Blocked

The most important architectural rule in Aaraksha:

> **Every anti-abuse mechanism, every rate limiter, every external service dependency
> must fail open on the emergency path. A tourist in genuine distress must always
> be able to trigger a real SOS.**

This is encoded in the system three ways:
1. Trust score restrictions gate convenience features, not SOS
2. Every `try/catch` around SMS/push/Gemini allows the SOS record to persist regardless
3. The offline SMS path works independently of the app, backend, and internet

---

## SOS Event Lifecycle

### Trigger Types

| Type | How | When |
|------|-----|------|
| `MANUAL` | Tourist taps SOS button in app | Internet available |
| `DMS` | Dead Man's Switch timeout — node-cron auto-fires | App may be closed |
| `INBOUND_SMS` | Structured SMS received by Twilio webhook | Zero internet on device |

### SOS Categories

`MEDICAL` · `LOST` · `TRAPPED` · `DISASTER` · `OTHER`

(Expanded in migration `021_sos_category_amendment.js`)

### SOS Status Machine

```
ACTIVE
  │
  ├─→ RESOLVED   (govt officer marks resolved — full rescue completed)
  └─→ FALSE_ALARM (tourist or govt marks as false — affects trust score)
```

### SOS Record Schema (key fields)

```sql
sos_events:
  id            UUID PK
  tourist_id    UUID FK → tourists
  trip_id       UUID FK → trips (nullable — SOS can fire outside active trip)
  latitude      NUMERIC(10,7)
  longitude     NUMERIC(10,7)
  category      TEXT (MEDICAL/LOST/TRAPPED/DISASTER/OTHER)
  trigger_type  TEXT (MANUAL/DMS/INBOUND_SMS)
  status        TEXT (ACTIVE/RESOLVED/FALSE_ALARM)
  message       TEXT (optional tourist note)
  resolved_at   TIMESTAMPTZ
  resolved_by   UUID FK → govt_users
  created_at    TIMESTAMPTZ
```

---

## Dead Man's Switch (DMS) — Detailed

### How It Works

1. Tourist activates DMS and sets an interval (e.g., 2 hours)
2. `dead_mans_switches` row created with `status = ACTIVE` and `next_trigger_at = NOW() + interval`
3. Every manual check-in resets `next_trigger_at` to `NOW() + interval`
4. `node-cron` job fires **every 60 seconds** and queries:
   ```sql
   SELECT * FROM dead_mans_switches dms
   JOIN tourists t ON t.id = dms.tourist_id
   WHERE dms.status = 'ACTIVE' AND dms.next_trigger_at <= NOW()
   ```
5. If `warning_sent_at` is null: sends SMS warning, sets `warning_sent_at = NOW()`
6. If `warning_sent_at` is set (warning already sent, still overdue): auto-fires SOS
   with `trigger_type = DMS`, sends emergency contact SMS

### DMS Configuration

```
interval_minutes: tourist-configured (minimum enforced)
last_checkin_at:  updated on every check-in
next_trigger_at:  computed = last_checkin_at + interval_minutes
warning_sent_at:  set when first overdue notification is sent
status:           ACTIVE / TRIGGERED / PAUSED / CANCELLED
```

### Demo Mode

Migration `008_dms_demo_seconds.js` adds `interval_demo_seconds` — allows demo scenarios
with 30-second DMS intervals for live presentations without waiting 2 hours.

---

## Offline SOS — Complete Path

### SMS Format

```
AARAKSHA_SOS|ID:{tourist_id}|LAT:{lat}|LNG:{lng}|CAT:{category}|BATT:{battery_pct}|TIME:{unix_ts}
```

Example:
```
AARAKSHA_SOS|ID:a1b2c3d4-...|LAT:27.5860|LNG:91.8933|CAT:MEDICAL|BATT:23|TIME:1726384800
```

### Parser

```js
const FIELD_RE = /AARAKSHA_SOS\|ID:([^|]+)\|LAT:([^|]+)\|LNG:([^|]+)\|CAT:([^|]+)\|BATT:([^|]+)\|TIME:(\d+)/
const [, id, lat, lng, cat, batt, time] = body.match(FIELD_RE) || []
```

### Twilio Inbound Webhook Flow

```
Tourist sends SMS → Twilio receives → POST /api/webhooks/twilio-inbound
  ↓
webhook.service.js parses SMS body
  ↓
Looks up tourist by ID (from SMS)
  ↓
Creates sos_events row (trigger_type = INBOUND_SMS)
  ↓
Saves inbound_sos_sms row (raw body + parsed + linked sos_event_id)
  ↓
Socket.IO: emits SOS_RECEIVED to govt-dashboard
  ↓
Twilio: sends acknowledgement SMS to tourist (if Twilio configured)
  ↓
Returns TwiML response (200)
```

### Why SMS Works in Connectivity Blackspots

- Modern smartphones have a **separate satellite GPS radio** — it works without mobile data
- SMS operates on **GSM voice/2G bands** which have better tower penetration than 4G data
- The structured SMS is short enough to transmit even in poor signal conditions
- Twilio's inbound webhook processes it server-side — no internet required on the device at time of receipt

---

## Trust Score System

### Purpose

Prevent abuse of SOS (false alarms drain rescue resources) without ever blocking a real emergency.

### Trust Score Events (from migration `022_trust_score.js`)

| Event | Delta |
|-------|-------|
| First registration | 0 (neutral) |
| False alarm (tourist self-reported) | -5 |
| False alarm (govt-reported) | -10 |
| Verified check-in | +2 |
| Verified incident report (accepted) | +5 |
| Successful rescue completion | +10 |
| Appeal accepted | +reversal |

### Trust Score Effects

| Trust Score Range | Effect |
|------------------|--------|
| 70–100 | Full access, no restrictions |
| 40–69 | Warnings shown; extra confirmation required for SOS |
| 0–39 | Restricted: some convenience features gated |
| Any score | **SOS always allowed — never blocked** |

### Appeals Process

1. Tourist sees trust reduction → reads reason
2. Tourist files appeal via `TrustAppealsPage` in app
3. Govt reviews in `TrustAppealsPage` on command center
4. Govt approves → trust event reversed; rejects → remains

---

## SOS Cluster Detection (Anomaly Service)

### Algorithm

```js
// Group SOS events within CLUSTER_RADIUS_KM (default 10km)
// in CLUSTER_WINDOW_HOURS (default 24h) rolling window
// If cluster size >= CLUSTER_THRESHOLD (default 3): flag as anomaly

for (const sos of recentSOS) {
  for (const existing of clusters) {
    const dist = haversineKm(sos.lat, sos.lng, existing.centroid.lat, existing.centroid.lng)
    if (dist <= CLUSTER_RADIUS_KM) {
      existing.members.push(sos)
      break
    }
  }
  clusters.push(newCluster(sos))
}

clusters
  .filter(c => c.members.length >= CLUSTER_THRESHOLD)
  .forEach(c => insertSafetyAnomaly(c))
```

### Anomaly Types

| Type | Trigger |
|------|---------|
| `CLUSTER` | ≥3 SOS events within 10km in 24h |
| `FREQUENCY` | District SOS rate > 2× rolling 7-day average |

### Storage

`safety_anomalies` table — surfaced on Govt Risk Overview page.

---

## Checkpoint Hash Chain

Implemented in `checkpoint.service.js`:

```js
// Each checkpoint scan generates:
hash = SHA-256(`${tripId}|${checkpointId}|${timestamp}|${prevHash}`)

// Stored in checkpoint_scans:
{
  trip_id, checkpoint_id, scanned_at,
  hash,      // This scan's hash
  prev_hash  // Previous scan's hash (null for first)
}
```

Verification: recompute hash from stored fields and compare. Any tampered scan breaks the chain.

---

## Rescue Assignment Flow

```sql
-- Assign rescue team to SOS
INSERT INTO rescue_assignments
  (sos_event_id, team_id, assigned_by, status, assigned_at)
VALUES ($1, $2, $3, 'ASSIGNED', NOW())

-- Update team status
UPDATE rescue_teams SET status = 'DISPATCHED' WHERE id = $1

-- Socket.IO events emitted:
io.to('govt-dashboard').emit('RESCUE_ASSIGNED', { sosId, team })
io.to(`tourist-${touristId}`).emit('RESCUE_ASSIGNED', { team, eta })
```

### Rescue Assignment Statuses
`ASSIGNED` → `EN_ROUTE` → `COMPLETED`

### Handoff Flow (Volunteer → Official Team)

When a volunteer arrives at scene, a formal handoff record is created via `handoff.service.js`:
- Volunteer marks arrival
- Handoff record created with volunteer ID, official team ID, timestamp, notes
- Volunteer status transitions to COMPLETED
- Official team takes over case
- Volunteer earns 25 completion points

---

## Graceful Degradation Matrix

| External Service | Failure Mode | System Behavior |
|-----------------|-------------|-----------------|
| Twilio (outbound) | API key missing / network fail | SMS skipped; SOS saved to DB; Socket.IO fires normally |
| Twilio (inbound webhook) | Signature mismatch | 403 returned; no SOS created (correct — invalid request) |
| Gemini API | Key missing / timeout | Packing: static fallback list. Itinerary: error message. Chatbot: error message. |
| OpenWeatherMap | Key missing / API fail | Weather factor = 0 in TSI. Score computed on remaining 5 factors. |
| VAPID/Push | Key missing | Push silently no-ops; no error thrown |
| PostgreSQL | Connection timeout | 500 returned from errorHandler; pino logs the error |

---

## DPDP Act 2023 Compliance

| Right | Implementation |
|-------|---------------|
| Right to notice | Privacy notice shown at registration |
| Right to access | `GET /api/tourists/me/export` — full JSON of tourist's data |
| Right to correction | `PATCH /api/tourists/me` — update profile fields |
| Right to erasure | `POST /api/tourists/me/delete-request` — anonymize-in-place |
| Erasure guard | Blocked automatically if open SOS or E-FIR exists |
| Govt ID on erasure | Hash replaced with placeholder (not left behind) |
| Grievance redressal | In-app appeal + email contact |

### Erasure Implementation

Tourist data is **anonymized in place** on confirmed deletion — not raw `DELETE`:
```sql
UPDATE tourists SET
  full_name = 'Deleted User',
  phone = 'deleted_' || id,
  email = 'deleted_' || id || '@deleted.aaraksha',
  password_hash = 'DELETED',
  govt_id_hash = 'DELETED',
  govt_id_suffix = '****',
  is_active = false
WHERE id = $1
```
This preserves referential integrity (SOS history, rescue records remain) while removing PII.
