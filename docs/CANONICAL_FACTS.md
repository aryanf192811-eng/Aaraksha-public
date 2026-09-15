# Canonical Project Facts — Aaraksha

> **Source of truth for every number, metric, and claim in this repository.**
> All values below were verified directly from the codebase on 2026-09-15.
> Cross-checked against: migration files, route files, test files, Postman collection, seed scripts.

---

## Engineering Metrics

| Metric | Verified Value | Source |
|--------|---------------|--------|
| Portals | 4 | `frontend/` — tourist, govt, guardian, volunteer |
| API endpoints | 152 (across 20 route files) | `router.(get|post|patch|put|delete)()` count in route files |
| API route groups | 19 functional groups + 1 index | `backend/src/routes/` |
| Database tables | 34 (+ `pgmigrations` tracking table) | `pgm.createTable()` in all 36 migrations |
| Database migrations | 36 | `backend/src/migrations/001_initial_schema.js` → `036_vehicle_rental_tour_operator_categories.js` |
| Vitest tests | 74 (7 test files) | `it()` / `test()` count in `backend/tests/` |
| Frontend tests | ~95 across 4 apps | `npm test` output per portal |
| Postman test assertions | 336 (`pm.test()` calls) | `backend/postman/aaraksha-collection.json` |
| Postman requests | 151 | `"request":` count in collection |
| QA phases | 13 (12 adversarial + 1 final acceptance) | `docs/testing/` |
| Security defects found & fixed | 8 | `docs/testing/09-security-audit.md` |
| Services (backend) | 38 | `backend/src/services/` |
| Repositories (backend) | 19 | `backend/src/repositories/` |
| Node.js version | ≥20 (LTS) | `Architecture.md` |

## Destinations

| Metric | Verified Value | Source |
|--------|---------------|--------|
| NER destinations (seeded) | 10 core destinations in `seed.js` | `backend/scripts/seed.js` |
| States represented | 7 of 8 NER states | Arunachal Pradesh, Meghalaya, Assam, Nagaland, Manipur, Sikkim, Nagaland (Longwa) |
| Destination highlights | 15 destinations with verified `highlights[]` JSON | `backend/scripts/seed_destination_highlights.js` |

**10 seeded destinations:**
1. Tawang — Arunachal Pradesh
2. Shillong — Meghalaya
3. Cherrapunji (Sohra) — Meghalaya
4. Kaziranga — Assam
5. Dzukou Valley — Nagaland
6. Ziro Valley — Arunachal Pradesh
7. Loktak Lake — Manipur
8. Pelling — Sikkim
9. Majuli Island — Assam
10. Longwa Village — Nagaland

## Local Operator Ecosystem

| Category | Count (seeded) | Source |
|----------|---------------|--------|
| TOUR_OPERATOR | ~25 (incl. expansion script) | `curate_tour_operators.js` + `curate_vehicle_rental_tour_operator_expansion.js` |
| VEHICLE_RENTAL | ~8 | `curate_vehicle_rentals.js` + `curate_vehicle_rental_tour_operator_expansion.js` |
| Total local_operators rows | ~33 (all govt-verified, is_verified=true) | `local_operators` table |
| Operator categories (schema) | HOTEL, HOMESTAY, GUIDE, EXPERIENCE, ARTISAN, TOUR_OPERATOR, VEHICLE_RENTAL | `036_vehicle_rental_tour_operator_categories.js` |

> NOTE: The current seed data focuses on TOUR_OPERATOR and VEHICLE_RENTAL categories.
> HOTEL, HOMESTAY, GUIDE, EXPERIENCE, ARTISAN categories exist in the schema and are
> available for future data entry — no fabricated rows exist for them.

## PS 26204

**Official wording:**
> Student Innovation - A solution/idea that can boost the current situation of the tourism
> industries including hotels, travel and others.

**Ministry / Organization:** Ministry of Tourism, Government of India

**Category:** Travel & Tourism

## Claims Removed from Previous Documentation

The following claims were in the previous README version but could not be verified:

| Removed Claim | Reason |
|---------------|--------|
| "30 NER destinations" | Only 10 destinations seeded in seed.js |
| "all 8 states" | Only 7 states represented in 10 seeded destinations |
| "56 vitest tests" | Current count is 74 (the 56 was an older snapshot from Sept 4) |
| "331 Postman assertions" | Current is 336 pm.test() calls |
| "146 API endpoints" | Current count from route files is 152 |
| "33 database tables" | Current count from migrations is 34 |
| "HOTEL/HOMESTAY/GUIDE/EXPERIENCE/ARTISAN operators" | Schema supports these categories but no seeded data for them exists — only TOUR_OPERATOR and VEHICLE_RENTAL have seeded entries |
| "gemini-3.5-flash-lite" | Verify current model name against actual config |
