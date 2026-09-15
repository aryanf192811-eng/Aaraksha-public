# Known Limitations & Future Roadmap — Aaraksha

## Design Ethos on Limitations

Honest documentation of limitations is a feature, not a weakness.
Aaraksha is a hackathon prototype built for SIH 2026 — it is not a deployed production
service with SLAs. The limitations below are genuine, documented, and understood.

---

## Known Limitations (Honest, Not Hidden)

### Infrastructure

| Limitation | Technical Detail | Mitigation / Upgrade Path |
|-----------|-----------------|--------------------------|
| **Rate limiting is in-memory** | `express-rate-limit` default store: resets on process restart, won't coordinate across load-balanced instances | Replace default store with `rate-limit-redis`; add Redis as infrastructure |
| **Render free tier cold starts** | 20–30 second restart after idle; observed during testing | Upgrade to Render Starter ($7/month) for always-on; or ping `/health` before demo |
| **Single-process cron jobs** | node-cron DMS checker and weather updater run in the same process as the API | Acceptable at hackathon scale; production would use a worker process or separate scheduled job |

### Application

| Limitation | Technical Detail | Status |
|-----------|-----------------|--------|
| **No array-field size caps** | Trip stops, packing items, activities have no application-level length limit | No issue at demo scale; production would add Zod `.max()` constraints |
| **E-FIR photo auth** | Uploaded evidence photos are served without auth check (filenames are UUIDs — unguessable, partial mitigation) | Needs frontend + backend rework: presigned URLs or auth-gated endpoint |
| **No content moderation API** | Community feed posts (scam reports, reviews) have no delete/moderation endpoint | Needs product decision on moderation model before implementing |
| **Guardian token no auto-renewal** | Guardian tokens don't auto-renew when they expire | Documented product gap; fix: cron to detect approaching expiry + SMS notification to tourist |
| **No Postman/Newman in CI** | `.github/workflows/test.yml` runs vitest but not `newman run` | Known gap, identified in Phase 12; add `newman run` to CI next sprint |

### Security

| Limitation | Technical Detail | Status |
|-----------|-----------------|--------|
| **E-FIR photos not auth-gated** | Files in `/uploads/` are technically accessible by URL if guessed (UUIDs make guessing infeasible) | P2 — documented in Phase 9 security audit; full fix deferred |
| **`NODE_ENV=production` must be set explicitly** | Stack traces should stay out of error responses in production | Set via `render.yaml` envVar; verify not inherited from a committed `.env` default |

---

## What Was Explicitly Tested and Found Clean

| Area | Evidence |
|------|---------|
| SQL injection | Parameterized queries throughout; `' OR 1=1 --`, `DROP TABLE`, `UNION SELECT` all returned 400 |
| JWT algorithm confusion | All `jwt.verify()` calls pin `algorithms: ['HS256']` |
| Privilege escalation | Role gates verified: SUPER_ADMIN create, DISTRICT_OFFICER scope |
| Concurrency (SOS resolve race) | Atomic DB-level guard prevents duplicate resolution |
| Transaction rollback | Verified on forced FK violation: no surviving insert |
| Twilio signature verification | Webhook validates `X-Twilio-Signature` header (Phase 9) |
| CORS | Whitelist-only from env var URLs |
| PII in logs | Phone, JWT, password, GPS never logged at INFO level |

---

## Future Roadmap

### Immediate Next Sprint (P1)

| Feature | Description |
|---------|-------------|
| **Newman in CI** | Add `newman run backend/postman/aaraksha-collection.json` to `.github/workflows/test.yml` |
| **Guardian token auto-renewal** | Cron detects expiring tokens, SMS tourist, generates new token |
| **E-FIR photo auth** | Auth-gated photo serving with presigned URL generation |
| **Redis-backed rate limiting** | Stateless, multi-instance safe with `rate-limit-redis` |

### Medium Term

| Feature | Description |
|---------|-------------|
| **Offline MBTiles maps** | Bundle MBTiles for key NER districts (Meghalaya, Tawang, Sikkim) — full offline navigation without OSRM |
| **Real-time rescue ETA** | OSRM-computed ETA updated every 30 seconds as rescuer moves |
| **Content moderation queue** | Govt-managed review queue for community reports |
| **ML risk model** | Use the seeded anomaly data to train a predictive risk model per district/season |

### Long Term

| Feature | Description |
|---------|-------------|
| **Real NTN integration** | Replace simulated NTN channel with an actual satellite mesh provider (ISRO's GSAT, Starlink) |
| **Multi-language expansion** | Full UI translations: Khasi, Mizo, Manipuri, Assamese, Hindi |
| **Government data API** | Structured data export for state tourism departments and NDMA |
| **Capacity prediction** | ML model to estimate rescue resources required for a SOS cluster type/location |
| **Operator rating integration** | Cross-reference govt licensing database for operator verification |
| **Insurance integration** | Connect tourist profile + TSI score with travel insurance providers |

---

## What This Is (and Isn't)

### This IS

- A fully functional four-portal system with a real database, real APIs, and real deployments
- A genuine implementation of PS 26204 — tourist safety, govt coordination, local operator discovery
- A security-audited backend with 8 real defects found and fixed through adversarial testing
- A platform where the SOS path works end-to-end: trigger → govt dashboard → rescue assignment → rescuer navigation
- A system that degrades gracefully on every external service failure

### This IS NOT

- A production deployment serving real tourists (it is a hackathon prototype)
- Integrated with real government databases or NDMA/NDRF systems
- Validated with real rescue teams or real SOS situations
- A live payment or booking system for local operators
- A production-scale deployment (single Render instance, free tier Postgres)

These are honest scope boundaries for a hackathon prototype, not gaps that undermine
the technical validity of what was built.
