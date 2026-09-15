# Testing Evidence — Aaraksha

## Summary

| Layer | Coverage |
|-------|---------|
| Backend unit + integration (vitest) | **56 tests** — TSI scoring, itinerary scoring, crypto utils, NTN channel simulator, auth integration, travel planner adjustment |
| Frontend (vitest, all 4 apps) | **~95 tests** across tourist/govt/guardian/volunteer |
| API contract (Postman/Newman) | **331 assertions** across **149 requests** in **26 folders** |
| CI (GitHub Actions) | Backend vitest against ephemeral Postgres + frontend `tsc -b` matrix, every push |
| Scoring benchmark | `tests/eval/travelPlanner.benchmark.js` — 6/6 fixed real-world queries passing |
| QA phases | **13 phases** across 12+ weeks of development |

---

## Backend Test Files (vitest)

### Unit Tests (`backend/tests/unit/`)

| File | What It Tests |
|------|--------------|
| `tsi.service.test.js` | TSI algorithm: worst-stop logic, label thresholds, all 6 factors, edge cases |
| `travelScoring.service.test.js` | Itinerary scoring: interest tags, cost bands, distance penalties |
| `crypto.utils.test.js` | SHA-256 govt ID hashing, bcrypt compare, Aadhaar Verhoeff checksum |
| `ntnChannel.simulator.test.js` | NTN message send/receive simulation |
| `planningIntentDelta.test.js` | Trip adjustment delta extraction |

### Integration Tests (`backend/tests/integration/`)

| File | What It Tests |
|------|--------------|
| `auth.test.js` | Full registration → OTP → login flow against `aaraksha_test` DB |
| `travelPlanner.adjustment.test.js` | Full plan → adjust → verify delta pipeline |

### Scoring Benchmark (`backend/tests/eval/`)

`travelPlanner.benchmark.js` — 6 fixed, real-world Northeast India trip queries run against
the live scorer + dev database. All 6 pass with expected score ranges.

---

## Postman Collection (331 Assertions / 149 Requests / 26 Folders)

Located at `backend/postman/aaraksha-collection.json` in the private repo.

### Folder Coverage

| Folder | Coverage |
|--------|---------|
| Auth — Tourist | Register, login, OTP send/verify |
| Auth — Govt | Login, register (SUPER_ADMIN gated) |
| Auth — Volunteer | Register, login |
| Trips | CRUD, TSI fetch, group members |
| SOS | Trigger, resolve, false alarm, history |
| Dead Man's Switch | Create, check-in, pause, cancel |
| Destinations | List, detail, TSI, news, reviews |
| Local Operators | List, detail, reviews |
| Travel Planner | Plan from prompt, adjust, curated |
| Govt — SOS Management | List active, triage, resolve |
| Govt — Rescue Teams | CRUD, status update |
| Govt — Volunteers | List, verify, reject |
| Govt — Local Operators | List, verify, reject |
| Govt — Analytics | Trends, risk overview |
| Govt — Incidents | Queue, status update |
| Volunteers | Status toggle, location, dispatches, accept/decline |
| Check-ins | Submit, list |
| Scam Reports | File, list by destination |
| Security Guards | SQLi payloads, privilege escalation, role confusion |
| Validation | Missing required fields, invalid enum values, out-of-range coords |
| Edge Cases | Empty results, concurrent requests, idempotency |
| AI Travel Assistant | Plan + adjust pipeline with real NER destinations |
| NTN Channel | Send + receive simulated messages |
| Operator Review Loop | Review + points + reply cycle |
| E-FIR Queue | Incident → govt review → status update |
| Unified Rescuer Flow | Register → verify → dispatch → accept → arrive → complete |

---

## 12-Phase QA Process

All 12 phase reports are in this `docs/testing/` directory.

| Phase | Report | Focus | Findings |
|-------|--------|-------|----------|
| 1 | [01-system-audit.md](./01-system-audit.md) | System audit | 5 doc discrepancies, stale test DB schema |
| 2 | [02-backend-api-db.md](./02-backend-api-db.md) | Backend/API/DB | 3 real backend bugs + 1 behavior fix |
| 3 | [03-tourist-pwa.md](./03-tourist-pwa.md) | Tourist PWA | 6 bugs across 12-screen app |
| 4 | [04-government-portal.md](./04-government-portal.md) | Govt portal | 5 missing error handlers + E-FIR status |
| 5 | [05-guardian-portal.md](./05-guardian-portal.md) | Guardian | 1 copy bug (3 locales) |
| 6 | [06-rescuer-app.md](./06-rescuer-app.md) | Rescuer app | 3 bugs including MapLibre fitBounds |
| 7 | [07-cross-portal-e2e.md](./07-cross-portal-e2e.md) | Cross-portal E2E | Govt real-time connection dying after navigation — most severe bug found |
| 8 | [08-offline-resilience.md](./08-offline-resilience.md) | Offline/resilience | 4 bugs + Twilio signature (deferred to Phase 9) |
| 9 | [09-security-audit.md](./09-security-audit.md) | Security | 4 findings: Twilio sig gap, missing RBAC gate |
| 10 | [10-realtime-validation.md](./10-realtime-validation.md) | Real-time | 5 bugs: socket auth, session bleed, reconnect |
| 11 | [11-ui-ux-qa.md](./11-ui-ux-qa.md) | UI/UX | 1 design fix; live stale SOS cleanup |
| 12 | [12-regression-report.md](./12-regression-report.md) | Regression | 28/28 backend, 269/269 Postman — CLEAN |
| 13 | [FINAL_QA_REPORT.md](./FINAL_QA_REPORT.md) | Final acceptance | PASS ✅ — zero P0/P1 |

**Total: 20+ real defects found and fixed across all phases.**

---

## Security Audit Highlights (Phase 9)

Full report: [09-security-audit.md](./09-security-audit.md)

### SQL Injection

Tested: `' OR 1=1 --`, `Robert'; DROP TABLE tourists; --`, `UNION SELECT 1,2,3--`

All held. Parameterized queries (`$1, $2, ...`) throughout — no string-built SQL in the codebase.

### Authentication

- JWT algorithm confusion: all `jwt.verify()` calls now pin `algorithms: ['HS256']`
- Privilege escalation: `POST /auth/govt/register` was open — now requires SUPER_ADMIN
- OTP rate limiting: fixed budget scope

### Input Validation

- All required fields validated in controller before DB query
- Enum values validated against allowed list
- Coordinate ranges validated (lat ∈ [-90,90], lng ∈ [-180,180])
- Phone numbers normalized before storage

### WCAG 2.1 AA (Government Portal)

- `aria-label` on all interactive elements
- Keyboard focus visibility
- 4.5:1 contrast tokens
- Modal keyboard handling (Escape closes)
- Alt text on all images
- Form label association

---

## Regression Report (Phase 12 — Final Numbers)

- Backend vitest: **28/28 tests passing**
- Postman/Newman: **269/269 assertions passing**
- `tsc -b` across all 4 frontends: **clean** (zero type errors)

See full report: [12-regression-report.md](./12-regression-report.md)
