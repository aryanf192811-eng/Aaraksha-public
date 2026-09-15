# Aaraksha — Testing Documentation

Index for the final system-wide QA, integration, security, and UX validation pass.

Full plan: [`QA-MASTER-PLAN.md`](./QA-MASTER-PLAN.md)

---

## Phase Reports

| # | Phase | Report | Result |
|---|-------|--------|--------|
| 1 | System audit | [`01-system-audit.md`](./01-system-audit.md) | PASS WITH ISSUES |
| 2 | Backend / API / DB | [`02-backend-api-db.md`](./02-backend-api-db.md) | PASS WITH ISSUES |
| 3 | Tourist PWA | [`03-tourist-pwa.md`](./03-tourist-pwa.md) | PASS WITH ISSUES |
| 4 | Government Command Center | [`04-government-portal.md`](./04-government-portal.md) | PASS WITH ISSUES |
| 5 | Guardian Portal | [`05-guardian-portal.md`](./05-guardian-portal.md) | PASS WITH ISSUES |
| 6 | Rescuer App | [`06-rescuer-app.md`](./06-rescuer-app.md) | PASS WITH ISSUES |
| 7 | Cross-portal E2E | [`07-cross-portal-e2e.md`](./07-cross-portal-e2e.md) | PASS WITH ISSUES |
| 8 | Offline / resilience | [`08-offline-resilience.md`](./08-offline-resilience.md) | PASS WITH ISSUES |
| 9 | Security audit | [`09-security-audit.md`](./09-security-audit.md) | PASS WITH ISSUES |
| 10 | Real-time consistency | [`10-realtime-validation.md`](./10-realtime-validation.md) | PASS WITH ISSUES |
| 11 | UI / UX QA | [`11-ui-ux-qa.md`](./11-ui-ux-qa.md) | PASS WITH ISSUES |
| 12 | Regression | [`12-regression-report.md`](./12-regression-report.md) | **PASS** |
| — | Final acceptance | [`FINAL_QA_REPORT.md`](./FINAL_QA_REPORT.md) | **PASS ✅** |

---

## Other Testing Artifacts

- **Vitest unit + integration suite** — `backend/tests/` (in private repo)
- **Postman / Newman API contract collection** — `backend/postman/` (in private repo)
- **GitHub Actions CI** — `.github/workflows/test.yml` — backend vitest against ephemeral Postgres + frontend `tsc` matrix across all four portals

---

## Databases

| DB | Env var | Purpose |
|---|---|---|
| `aaraksha` | `DATABASE_URL` | Demo / presentation — never reset during live evaluation |
| `aaraksha_test` | `DATABASE_TEST_URL` | CI-only — reset freely |

Full discipline in [`QA-MASTER-PLAN.md`](./QA-MASTER-PLAN.md).
