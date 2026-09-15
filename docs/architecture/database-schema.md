# Database Schema Reference — Aaraksha

**33 tables, 36 migrations** from `001_initial_schema.js` to `036_vehicle_rental_tour_operator_categories.js`.

The migrations directory (`backend/src/migrations/`) is the authoritative source.
This document provides the map and key decisions; column-level detail is in the migration files.

---

## Table Map by Area

### Identity & Auth (4 tables)

| Table | Purpose |
|-------|---------|
| `tourists` | Tourist accounts: profile, govt ID hash, guardian token, trust score |
| `govt_users` | Government officer accounts with RBAC roles |
| `otp_verifications` | OTP send/verify flow for tourist phone verification |
| `data_deletion_requests` | DPDP erasure requests (pending / processed) |

### Trips & Travel Planning (10 tables)

| Table | Purpose |
|-------|---------|
| `trips` | Trip records: title, dates, travel_type, status, TSI score/factors, rescue readiness |
| `trip_members` | Group trip member list (tourist_id + member details) |
| `destinations` | 30+ NER destinations: connectivity, altitude, zone_type, hospital proximity |
| `typical_routes` | Sourced inter-destination routes: mode, cost, duration |
| `curated_itineraries` | Pre-built itineraries by interest tags |
| `destination_news` | Safety advisories, trail status, local events per destination |
| `destination_reviews` | Tourist reviews of destinations (text + rating) |
| `weather_cache` | OpenWeatherMap data per destination, refreshed every 60 min |
| `local_operators` | Govt-verified tourism providers: HOTEL/HOMESTAY/GUIDE/EXPERIENCE/ARTISAN |
| `local_operator_reviews` | Tourist reviews of local operators |

### Safety Core (6 tables)

| Table | Purpose |
|-------|---------|
| `checkins` | Manual + DMS check-ins with GPS + battery |
| `dead_mans_switches` | DMS configuration + trigger state |
| `sos_events` | SOS records: category, trigger_type, GPS, status |
| `sos_cluster_flags` | Anomaly clusters flagged by anomaly.service.js |
| `safety_anomalies` | District-level anomaly alerts (CLUSTER + FREQUENCY) |
| `tourist_locations` | Upsert table: latest tourist GPS (one row per tourist, always current) |

### Rescue Network (4 tables)

| Table | Purpose |
|-------|---------|
| `rescue_teams` | Official rescue teams: POLICE/MEDICAL/FOREST/NDRF with status/location |
| `rescue_assignments` | SOS → Team assignment with status tracking |
| `volunteers` | Govt-verified local responders |
| `volunteer_dispatches` | Volunteer → SOS dispatch with accept/decline/arrive/complete lifecycle |

### Incidents & Community (3 tables)

| Table | Purpose |
|-------|---------|
| `incident_reports` | Tourist-filed incidents with photo evidence (E-FIR pipeline) |
| `scam_reports` | Tourist scam reports: OVERCHARGING/FAKE_GUIDE/THEFT/OTHER |
| `checkpoint_scans` | Tourist checkpoint scan records with hash-chain |

### Trust & Messaging (3 tables)

| Table | Purpose |
|-------|---------|
| `tourist_trust_events` | Trust score delta log: event_type + delta + reason |
| `tourist_trust_appeals` | Tourist appeals against trust reductions |
| `messages` | In-app messages between tourist, rescuer, and govt officer on an SOS case |

### Offline / NTN / Push (3 tables)

| Table | Purpose |
|-------|---------|
| `inbound_sos_sms` | Raw + parsed Twilio inbound SMS, linked to sos_events after matching |
| `ntn_messages` | NTN satellite channel simulation messages |
| `push_subscriptions` | Web Push VAPID subscription endpoints per tourist |

---

## Key Schema Decisions

| Decision | Technical Reason |
|----------|-----------------|
| `govt_id_hash = SHA-256(full_id)` + `suffix = last 4 chars` | PII protection: full ID never stored |
| `tourist_locations` is an upsert-only table | Avoids unbounded location history growth; always has the current position |
| `sos_events.trigger_type` | Distinguishes manual, automated (DMS), and SMS-based SOS for analytics |
| `local_operators.source NOT NULL` | Provenance discipline: no operator row without a checkable source citation |
| `typical_routes.source NOT NULL` | Same provenance discipline for route data |
| `dead_mans_switches.next_trigger_at` | Computed target checked by cron; updating it is the check-in reset operation |
| `checkpoint_scans.hash + prev_hash` | Hash-chain: any tampered scan breaks all subsequent hashes |
| `tourist_trust_events` (event log, not column) | Full audit trail + reversible (appeal approval recreates the delta) |
| All SOS/trip/tourist IDs: UUID v4 | `gen_random_uuid()` from PostgreSQL 15 — unguessable, no sequential exposure |

---

## Migration Timeline

| Range | Focus |
|-------|-------|
| 001 | Initial 13-table schema: tourists, trips, sos_events, dms, checkins, govt_users, rescue_teams/assignments, destinations, weather_cache, scam_reports, inbound_sos_sms, tourist_locations |
| 002–006 | Group trips, push subscriptions, checkpoint scans, destination news, reviews |
| 007–010 | Checkpoint geo, DMS demo-seconds, volunteers, unify rescuers |
| 011–016 | Safety anomalies, incident reports, checkpoint trip link, incident photos, data rights, rescue handoff |
| 017–022 | Rescuer exit flow, Vadodara seed data, messaging, SOS category expansion, trust score |
| 023–028 | SOS cluster flags, NTN messages, typical routes, travel data provenance, local operators, guardian PIN |
| 029–036 | Local operator reviews, tourist points, destination highlights, curated itineraries, nearest police station, operator accounts, provider impressions, vehicle/rental categories |
