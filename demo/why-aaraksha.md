# Why Aaraksha — For SIH Judges

## The 30-Second Version

Northeast India has some of India's most spectacular tourism destinations.
It also has connectivity blackspots, high-altitude medical risks, Inner Line Permit complexity,
and no unified digital safety infrastructure for tourists.

Aaraksha is a four-portal platform that addresses all of this — tourist safety, government
situational awareness, family peace-of-mind, local responder coordination, and local tourism
discovery — in one integrated, working system.

---

## What Makes Aaraksha Different From "Another Safety App"

### 1. It's Four Real Applications, Not One

Most safety apps are tourist-only. Aaraksha is four distinct portals:
- Tourist (the one who needs help)
- Government (the one who coordinates rescue)
- Guardian (the family who is worried)
- Rescuer (the local volunteer who responds)

All four receive real-time events from the same backend. A tourist's SOS appears on the
govt map within ~100ms of being triggered. The rescuer's GPS position appears on the govt
map in real-time. The family's guardian portal updates every time the tourist checks in.

### 2. The Offline SOS Path Is Real

In genuine connectivity blackspots, tourists can send an SOS via SMS. The structured SMS
format carries GPS coordinates (from satellite radio, which works without mobile data),
category, battery, and tourist ID. Twilio receives it, the backend parses it, and it enters
the same SOS pipeline as an internet-triggered SOS. This is a genuine offline safety path,
not a UI feature.

### 3. The TSI Algorithm Is Auditable

The Travel Safety Index is 100% rule-based JavaScript. Every factor has an explicit penalty
table in `tsi.service.js`. A judge can read the code and verify exactly why a Tawang winter
trek scores "Extreme Risk." No model weights, no unexplainable AI decision.

### 4. The AI Boundary Is Deliberate

Gemini handles prose (narrative, packing lists, chatbot). All routing, ranking, cost
estimation, and safety scoring are deterministic code. This is a design choice, not a
limitation — AI that controls safety decisions is an inappropriate risk for an emergency system.

### 5. The Local Operator Ecosystem Directly Answers PS 26204

The PS asks for "information services including hotels, travel and others." Aaraksha has:
- A full `local_operators` table with 5 categories
- Govt verification gate (same trust model as volunteers)
- Tourist discovery integrated into trip planning
- Review system with tourist points
- Operator accounts for self-service management

This is not a bullet point on a slide — it is a working database table with a working
verification workflow visible in the live Government Command Center.

---

## Evidence Quality

Every claim in this repository is backed by code, screenshots, or QA reports:

| Claim | Evidence |
|-------|---------|
| 146 API endpoints | `PRODUCTION_READINESS_REPORT.md` + route files in private repo |
| 33 database tables | 36 migration files, each creating/altering tables |
| 331 Postman assertions | `backend/postman/aaraksha-collection.json` |
| 56 vitest tests | `backend/tests/` directory |
| 13 QA phases | `docs/testing/` — 12 phase reports + final acceptance |
| 8 security defects fixed | `docs/testing/09-security-audit.md` + `PRODUCTION_READINESS_REPORT.md` |
| 21 real screenshots | `screenshots/` directory — all captured from live running portals |
| Live deployment | 4 Vercel URLs + Render backend |

Nothing in this repository was fabricated. The limitations section is equally honest.

---

## The Architecture Choices That Matter

| Choice | Why It Matters |
|--------|----------------|
| Raw `pg` pool, no ORM | Full SQL control; parameterized queries enforced by convention, not framework |
| JWT HS256 algorithm-pinned | Prevents algorithm confusion attacks |
| Worst-stop-wins TSI | Mathematically correct for risk assessment (never average away danger) |
| Socket.IO rooms per entity type | Clean event scoping; govt can't accidentally receive tourist-private events |
| DPDP Act compliance | Indian data protection law, not an afterthought |
| node-cron for DMS, not Redis | Appropriate technology for scale; avoids infrastructure complexity |
| Graceful degradation everywhere | No external API failure can block an SOS |

---

## One Thing to Try Right Now

> Open **https://aaraksha-tourist.vercel.app** on your phone.
> Register an account.
> Create a trip to Tawang.
> Type: "Plan a 7-day solo trek to Meghalaya starting from Delhi, I love waterfalls."
> See what the AI planner builds.
> Enable the Dead Man's Switch for 60 seconds.
> Watch what happens.

The system is live. The database is real. The TSI score is computed. The DMS timer is running.

---

## Private Codebase

**[→ Request Access to the Complete Production Codebase](https://github.com/aryanf192811-eng/Aaraksha)**

The full implementation — 38 service files, 36 migrations, 20 route files, 4 TypeScript
frontend apps, CI configuration, and QA reports — is in the private repository.
