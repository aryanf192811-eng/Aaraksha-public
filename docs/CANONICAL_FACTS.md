# Canonical Project Facts — Aaraksha

> **Source of truth for every number, metric, and claim in this repository.**
> All values below were verified directly from the codebase and the live production database
> on 2026-09-24. Cross-checked against: migration files, route files, test files, the Postman
> collection, and a direct query against the deployed production database.

---

## Engineering Metrics

| Metric | Verified Value | Source |
|--------|---------------|--------|
| Portals | 4 | `frontend/` — tourist, govt, guardian, volunteer (Aaraksha Sahayak) |
| API endpoints | 168 (across 19 route files + 1 index) | `router.(get|post|patch|put|delete)()` count in route files |
| API route groups | 19 functional groups + 1 index | `backend/src/routes/` |
| Database tables | 39 (+ `pgmigrations` tracking table) | `pgm.createTable()` in all 41 migrations |
| Database migrations | 41 | `backend/src/migrations/001_initial_schema.js` → `041_trip_expenses.js` |
| Vitest tests (backend) | 87 (8 test files: unit + integration) | `it()` / `test()` count in `backend/tests/` |
| Frontend tests | ~95 across 4 apps | `npm test` output per portal |
| Postman test assertions | 345 (`pm.test()` calls) | `backend/postman/aaraksha-collection.json` |
| Postman requests | 157 | `"request":` count in collection |
| Postman folders | 30 | `backend/postman/aaraksha-collection.json` |
| QA phases | 13 (12 adversarial + 1 final acceptance) | `docs/testing/` |
| Security defects found & fixed | 8 | `docs/testing/09-security-audit.md` |
| Services (backend) | 43 | `backend/src/services/` |
| Repositories (backend) | 37 | `backend/src/repositories/` |
| Node.js version | ≥20 (LTS) | `Architecture.md` (private source repo) |

## Destinations

| Metric | Verified Value | Source |
|--------|---------------|--------|
| Destinations seeded | 19 | `destinations` table, production DB, queried directly |
| Northeast Indian states represented | 8 of 8 | Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura — 2 destinations each except Assam (3) |
| Non-Northeast seed rows | 2 (Vadodara, Parul University — Gujarat) | Used for a local demo-data scenario; excluded from every Northeast-scoped count/claim in the README |
| Destinations with curated highlights | 17 of 19 (the 2 non-NE rows excluded) | `backend/scripts/seed_destination_highlights.js` |

**19 seeded destinations** (2 per NE state except Assam's 3, plus the 2 non-NE demo rows):
Tawang & Ziro Valley (Arunachal Pradesh) · Jorhat, Kaziranga & Majuli Island (Assam) · Imphal &
Loktak Lake (Manipur) · Cherrapunji (Sohra) & Shillong (Meghalaya) · Aizawl & Champhai (Mizoram) ·
Dzukou Valley & Longwa Village (Nagaland) · Gangtok & Pelling (Sikkim) · Agartala & Unakoti
(Tripura) · Vadodara & Parul University (Gujarat, non-NE demo data).

## Local Operator Ecosystem

| Category | Count | Source |
|----------|---------------|--------|
| HOTEL | 15 | `local_operators` table, production DB |
| HOMESTAY | 14 | `local_operators` table, production DB |
| TOUR_OPERATOR | 21 | `local_operators` table, production DB |
| GUIDE | 9 | `local_operators` table, production DB |
| VEHICLE_RENTAL | 6 | `local_operators` table, production DB |
| ARTISAN | 6 | `local_operators` table, production DB |
| **Total local_operators rows** | **71** | `local_operators` table, production DB |
| Government-verified (`is_verified = true`) | 68 | `local_operators` table, production DB |
| With a sourced story + sustainability profile | 27 | `local_operators.story_text IS NOT NULL`, production DB |

> Every category the schema defines has real seeded rows — none of the six categories are
> empty placeholders.

## PS 26204

**Official wording:**
> Student Innovation - A solution/idea that can boost the current situation of the tourism
> industries including hotels, travel and others.

**Ministry / Organization:** Ministry of Tourism, Government of India

**Category:** Travel & Tourism

## Resync history

This document has been re-verified against the actual codebase and production database twice:

| Date | What changed |
|---|---|
| 2026-09-15 | Initial verified pass — replaced several unverifiable inflated claims (a "30 destinations" / "all 8 states" claim that didn't match the 10-destination seed at the time, a stale vitest/Postman/endpoint count) with then-current, directly-checked numbers |
| 2026-09-24 | Full resync — the destination catalog grew from 10 to 19 seeded destinations (genuinely all 8 NE states now, not 7), the local operator roster grew from ~33 to 71 real rows across all 6 schema categories (not just 2), and the group trip expense splitter shipped, adding 1 migration/table and several endpoints. Every number above was re-derived from the live route files, migration files, Postman collection, and a direct query against the production database — not incremented by guess from the previous pass |
