# 🛡️ Aaraksha — Smart Tourism, Safe Journey

<p align="center">
  <video src="./docs/aaraksha-video/Aaraksha_Full_Ecosystem_Video.mp4" controls="controls" muted="muted" style="max-width:100%; max-height:640px;"></video>
</p>

### 🧠 [**→ Explore the live Aaraksha Neural Map**](https://claude.ai/artifact/2XBsvLZRxmtQXdStDi4wJc) — the entire real codebase, rendered as an interactive 3D graph
4,162 real functions, classes, and files across the backend and all four portals, connected by
8,533 AST-extracted calls and imports, laid out live in the browser with GPU-accelerated
force physics. Not a diagram of the architecture — the architecture itself. Search any symbol,
click to trace its real call graph, orbit and zoom through the whole system in 3D.
([local copy](./docs/neural-map/index.html) also included — serve it, e.g. `npx serve docs/neural-map`,
since browsers block `fetch()` on `file://`)

---

**One journey, three intelligence layers: AI-planned, verified-tourism-enabled, and
safety-protected — an integrated platform for Northeast India built for Smart India Hackathon
2026, Student Innovation category, Travel & Tourism theme.**

> *Aaraksha* (आराक्षा) — "protection." Not a translation exercise: it's the one-word summary of
> what every screen in this system is trying to do — including, now, protecting a tourist's
> money and time from a fragmented planning experience, not just their body from an emergency.

> **Submission title:** *Aaraksha — An AI-Native Travel Planning, Verified Local Tourism
> Discovery, and Offline-Resilient Safety Platform for Northeast Indian Terrain*
>
> Deliberately three claims, not one, because that's what the system actually is: an AI travel
> assistant that plans, costs, and adapts a real itinerary; a government-verified directory of
> real local hotels, homestays, guides, and artisans surfaced inside that same itinerary — the
> direct answer to this PS's own "including hotels, travel and others"; and a safety layer that
> keeps working with zero signal, ties the tourist, their family, government dispatch, and a
> rescuer on the ground into one live picture, and never lets the first two claims come at the
> cost of the third.

[![Status](https://img.shields.io/badge/status-demo--ready-brightgreen)]()
[![Portals](https://img.shields.io/badge/portals-4-blue)]()
[![API](https://img.shields.io/badge/API%20endpoints-168-orange)]()
[![Tables](https://img.shields.io/badge/DB%20tables-39-orange)]()
[![Local providers](https://img.shields.io/badge/verified%20local%20providers-68-brightgreen)]()
[![Offline SOS](https://img.shields.io/badge/offline%20SOS-2G%20capable-red)]()
[![Digital ID](https://img.shields.io/badge/digital%20ID-hash--chained-9cf)]()
[![Category](https://img.shields.io/badge/SIH%202026-Student%20Innovation-purple)]()
[![Theme](https://img.shields.io/badge/theme-Travel%20%26%20Tourism-blueviolet)]()

---

## 🎯 The pitch, in one paragraph

Northeast India's terrain (3000m passes, zero-connectivity valleys, 2-hour hospital drives) and its
undiscoverable local tourism economy (real homestays, guides, cooperatives with no digital
presence) break most tourism and safety apps built for elsewhere. Aaraksha connects three things
no competitor connects: an **AI Travel Assistant** that plans/costs/safety-scores a real itinerary
from curated data; a **government-verified Local Tourism Providers directory** surfaced directly
inside that itinerary — the concrete answer to PS 26204's "hotels, travel and others"; and a
**safety layer built on the assumption phones fail exactly when needed most** — offline SMS SOS,
an auto-firing Dead Man's Switch, a citizen volunteer network with real routing, one government
command center watching the same live picture. One real-time data model, not three slide bullets.

<p align="center">
  <img src="./docs/screenshots/govt-dashboard.png" alt="Aaraksha government command center dashboard" width="100%">
</p>

---

## 📑 Table of contents

- [🔬 Research & prior art — where Aaraksha sits](#-research--prior-art--where-aaraksha-sits)
- [🧩 Four portals, one system](#-four-portals-one-system)
- [⭐ Feature walkthrough](#-feature-walkthrough)
- [🏨 Local Tourism Providers — the tourism-industry pillar](#-local-tourism-providers--the-tourism-industry-pillar)
- [🔗 Verifiable Digital ID — the Journey Integrity Hash](#-verifiable-digital-id--the-journey-integrity-hash)
- [🤖 A real trained model — the Predictive Risk Score](#-a-real-trained-model--the-predictive-risk-score)
- [🧭 AI Travel Assistant — plan, adjust, and track a journey](#-ai-travel-assistant--plan-adjust-and-track-a-journey)
- [🚑 The unified Rescuer network](#-the-unified-rescuer-network)
- [🗺️ Routing Engine — OSRM & Contraction Hierarchies](#️-routing-engine--osrm--contraction-hierarchies)
- [🛰️ NTN — a satellite fallback transport](#️-ntn--a-satellite-fallback-transport)
- [📸 Screenshots](#-screenshots)
- [🏗️ Architecture at a glance](#️-architecture-at-a-glance)
- [📈 By the numbers](#-by-the-numbers)
- [📁 Repository layout](#-repository-layout)
- [🚀 Getting started](#-getting-started)
- [🔑 Demo accounts](#-demo-accounts)
- [🔌 API surface](#-api-surface)
- [✅ Testing](#-testing)
- [🛡️ Production readiness](#️-production-readiness)
- [⚖️ Legal & Compliance](#️-legal--compliance)
- [📚 Documentation map](#-documentation-map)
- [🛤️ Roadmap](#️-roadmap)

---

## 🔬 Research & prior art — where Aaraksha sits

<details>
<summary><b>Click to expand</b> — competitive research against real SIH25002 submissions and market alternatives, plus a claim-by-claim comparison table</summary>

Aaraksha's origin point is real and worth stating plainly: it began as an answer to **SIH25002 —
"Smart Tourist Safety Monitoring & Incident Response System using AI, Geo-Fencing, and
Blockchain-based Digital ID,"** the Ministry of Development of North Eastern Region's problem
statement from SIH 2025. This year the team is entering through the **Student Innovation
category** under the **Travel & Tourism** theme — which means proposing and scoping the problem
ourselves rather than answering a fixed departmental brief. We kept building on the same real
problem (tourist safety in a genuinely hard, genuinely underserved terrain) because a year of
iteration had already turned up gaps a fixed PS wouldn't have surfaced on its own — the Dead Man's
Switch, the unified rescuer network, the handoff verification code, the anomaly detector, the
E-FIR triage queue, and everything else below didn't come from a requirements doc, they came from
asking "what would actually leave a family reassured and a rescuer accountable" and building
until the answer held up.

**What already exists in this exact problem space**, checked directly rather than assumed:

| Project | What it is | How Aaraksha differs |
|---|---|---|
| [RakshaSetu](https://github.com/ArindamTripathi619/smart-tourist-safety-system) | An open-source SIH25002 build — full-stack tourist safety monitoring, GPS tracking, digital ID | Single-audience (tourist + a dashboard); no offline/SMS path, no Dead Man's Switch, no live-tracked rescuer network with road routing, no anti-fraud handoff verification |
| SafeVoyage (SIH25002 submission) | Shake-to-SOS, blockchain audit trail, geo-fence guidance, phone-first E-FIR filing | Closest in spirit to Aaraksha's E-FIR flow; Aaraksha deliberately doesn't ship a shake/gesture SOS trigger — unreliable with the screen off in a web PWA — and uses a confirmed voice trigger instead. No public evidence of an offline-SMS fallback, a trained risk model, or government-side rescue *dispatch* (vs. alerting) |
| Multiple other SIH25002 repos (e.g. [SharandeepSingh295](https://github.com/SharandeepSingh295/smart-tourist-safety-system), [APC2005-dev](https://github.com/APC2005-dev/Smart-Tourist-Safety-Monitoring)) | The same brief, independently built dozens of times across SIH 2025 | Confirms the recognizable shape of a "PS25002-style" submission: mobile app + geo-fence + a blockchain-flavored ID. None found ship a second, distinct audience-side app for rescuers, nor a verification step that gates case closure |
| [Meghalaya's GPS + OTP tourist-taxi app](https://www.thetraveler.org/meghalayas-tourist-taxi-app-sets-new-safety-benchmark/) *(real, in-development state government initiative, not a hackathon project)* | Verified driver/vehicle registration, SOS buttons, GPS tracking, OTP-based rides | Solves transport-leg safety specifically, for one state; not itinerary-wide, not connectivity-independent, no digital identity or rescue-coordination layer |
| [Zone8](https://play.google.com/store/apps/details?id=com.kalyanmoyborah.zone8) *(real, live app, Android + iOS)* | A published NE India travel-planning and booking app, tagline "Travel Safe" | Genuinely live and used, but is a discovery/booking product — no SOS, no DMS, no government or rescuer-facing counterpart despite the safety-adjacent tagline |

Nobody involved in this project has access to the actual winning SIH25002 submission from SIH
2025 — that information isn't public, and this README won't pretend otherwise by naming a
specific team's build. What *is* verifiable, from the search above, is the recognizable shape
every public SIH25002 implementation and every real market alternative in this space shares: a
single-audience mobile app, a safety feature that assumes signal, and no real second audience that
has to *operate* the system, not just use it. That's the bar this comparison is written against:

| The recognizable pattern this problem space keeps producing | What Aaraksha ships instead |
|---|---|
| A static "call police" button | A rule-based Travel Safety Index recalculated **hourly from live weather**, scored per destination |
| Safety features that assume signal | **Offline SOS over raw SMS** — no data connection required, a Twilio webhook does the rest |
| One app, one audience | **Four cooperating portals** — tourist, government, a no-login family tracking link, and Aaraksha Sahayak (one shared login for rescue volunteers/official teams *and* govt-verified local businesses) — sharing one real-time data model |
| A mocked/seeded demo that falls apart under a second click | A backend that went through **13 adversarial QA phases** after the first build was "done" — rate-limit bypass attempts, SQLi payloads, concurrent double-resolve races, forced transaction rollbacks, real-time session bugs — each one found, fixed, and re-verified live, not just tested once (full record: [`docs/testing/`](./docs/testing/)) |
| Safety as an isolated feature | Safety **woven into planning** — every trip gets a TSI score before it's even booked, every destination card carries a live risk badge |
| Rescue dispatch as a phone call | A **unified Rescuer network** — official teams and govt-verified citizen volunteers in one assignable pool, live GPS, real OSRM road routing, plus a **Rescue Handoff Verification Code**: a 6-digit, HMAC-hashed, 3-attempt-lockout code only the tourist holds, checked against a 250m GPS proximity gate — a rescuer has to actually be standing next to the tourist to close the case, not just claim it by radio |
| "Blockchain-based Digital ID" as a marketing phrase over a static ID card image | A real **SHA-256 hash chain** over every trip's itinerary, check-ins, SOS events, *and* government checkpoint scans — tamper-evident, independently recomputable from platform records, verifiable live with one API call |
| "AI" meaning an LLM call with a prompt attached | A **genuine trained model** for predictive risk — real gradient descent, a printed loss curve, held-out test accuracy, and per-prediction explainability — sitting *alongside* (not instead of) an honestly rule-based TSI, each clearly labeled as what it is |
| Safety that only reacts once someone presses a button | A **rule-based anomaly detector** running every minute against every active trip — flags a tourist who's gone quiet or drifted off-route *before* anyone presses SOS, no opt-in required |
| "Report a crime" ends at a crowd-sourced warning post | A real **E-FIR triage workflow** — a formal, case-numbered report routed to a role-scoped officer queue (only the roles that actually investigate can even open it) with an investigation ladder (Filed → Assigned → Under Investigation → Resolved), not a community bulletin board |
| "We tested it" meaning the happy path worked once | A dedicated security pass that found and closed a **live unauthenticated privilege-escalation path** to govt SUPER\_ADMIN, an unauthenticated SMS webhook that could forge a real emergency alert, a missing role gate on a govt endpoint, pinned every JWT verification against algorithm-confusion attacks, and fixed a rate-limiter that silently ignored its own configuration |
| Flat 2D maps vs. competitors' VR/3D showpieces, or a rescue queue sorted by raw distance alone | **Real 3D elevation terrain** on the govt map (free, keyless, no CesiumJS bloat) so a dispatcher can see the mountain ridge between a rescuer and an SOS, plus **weighted dispatch scoring** that ranks a rescuer by category fit and reputation, not distance alone |
| "Govt ID verified" meaning a regex checked the digit count | The actual **Verhoeff checksum** — the real algorithm UIDAI uses to generate an Aadhaar number's 12th digit — run client-independent, server-side, at registration |
| Privacy as a paragraph in a slide deck | Working **DPDP Act 2023 data rights** — a tourist can view exactly what's collected and why, export every record held about them as a real file download, and request deletion, which anonymizes their row in place (never a raw `DELETE`, so legally-retainable SOS/E-FIR history survives) and is refused automatically while an open SOS or E-FIR exists |
| A UI that works until an accessibility or screen-reader pass is requested | A **WCAG 2.1 AA / GIGW 3.0 accessibility pass** on the government dashboard, not left as an afterthought for a public-sector system |

</details>

---

## 🧩 Four portals, one system

```
                     ┌──────────────────┐
                     │   PostgreSQL      │  39 tables — raw pg, no ORM
                     │   parameterized   │  see docs/architecture/database-schema.md
                     │   SQL only        │
                     └────────▲──────────┘
                              │
                     ┌────────┴──────────┐
                     │  Express API       │  Route → Middleware → Controller
                     │  (backend/)        │  → Service → Repository
                     │  JWT + RBAC        │  168 endpoints · 19 route groups
                     └─┬───────┬───────┬──┘
              Socket.IO│       │       │  REST (JSON)
              real-time│       │       │
        ┌──────────────┘       │       └──────────────┐
        │              ┌───────┴────────┐              │
        ▼              ▼                ▼              ▼
┌────────────┐ ┌───────────────┐ ┌─────────────┐ ┌─────────────┐
│ 🧭 Tourist  │ │ 🖥️ Govt Command│ │ 👪 Guardian  │ │ 🚑 Sahayak   │
│    PWA      │ │  Center        │ │  Portal      │ │    App       │
│  :5173      │ │  :5174         │ │  :5175       │ │  :5176       │
│  amber ·    │ │  emerald ·     │ │  token-in-   │ │  teal ·      │
│  mobile ·   │ │  desktop ·     │ │  URL, zero   │ │  live GPS ·  │
│  offline    │ │  live ops map  │ │  login       │ │  road routes │
└────────────┘ └───────────────┘ └─────────────┘ └─────────────┘
```

| Portal | Who | What they see |
|---|---|---|
| **Tourist PWA** | The traveler | Plan trips with a real Travel Safety Index, one-tap and gesture-triggered SOS, a Dead Man's Switch, curated destination news, community reviews, a printable Digital Journey Passport with a tamper-evident integrity hash, and a way to file a formal E-FIR for a non-emergency incident |
| **Govt Command Center** | District officers, dispatchers, checkpoint officers | A live map of every active tourist — plus rule-based anomaly markers for tourists who've gone quiet or drifted off-route — SOS triage with a combined team-or-volunteer dispatch panel, an E-FIR officer queue, volunteer identity verification, district risk overview, QR checkpoint scanning, and incident analytics with PDF export |
| **Guardian Portal** | Family and friends | A single shared link — no account, no app install — showing live location, SOS state, the assigned rescuer's live position on a real road route, battery, and medical info, auto-refreshing every 30 seconds |
| **Aaraksha Sahayak** | Official rescue teams, govt-verified citizen volunteers, and govt-verified local businesses (homestays, guides, tour operators) | For rescuers: nearby-SOS alerts, a full-screen live map with a real OSRM road route to the person in need, one-tap "Start navigation," and EN\_ROUTE/ARRIVED self-status reporting. For businesses: a self-service listing (story, sustainability tags, insider tips), a booking-request inbox, and Explorer-perk management — one shared login, gated by account type |

<table>
<tr>
<td width="25%"><img src="./docs/screenshots/tourist-dashboard.png" alt="Tourist PWA dashboard"></td>
<td width="25%"><img src="./docs/screenshots/govt-risk-overview.png" alt="Govt Command Center risk overview"></td>
<td width="25%"><img src="./docs/screenshots/guardian-portal.png" alt="Guardian Portal live SOS view"></td>
<td width="25%"><img src="./docs/screenshots/rescuer-active-job.png" alt="Aaraksha Sahayak live navigation"></td>
</tr>
<tr>
<td align="center"><sub>Tourist PWA — dashboard</sub></td>
<td align="center"><sub>Govt Command Center — risk overview</sub></td>
<td align="center"><sub>Guardian Portal — live SOS state</sub></td>
<td align="center"><sub>Aaraksha Sahayak — live road route</sub></td>
</tr>
</table>

---

## ⭐ Feature walkthrough

### 🧭 Planning
- **Multi-stop itineraries** — 19 NE India destinations, all 8 states, live weather/altitude/connectivity/ILP/hospital data
- **Destination Detail Pages** — photo gallery, live weather, highlights, verified providers, reviews, curated itineraries
- **AI Travel Assistant ("Build My Journey")** — plain-language trip → deterministic-scorer itinerary, Gemini only narrates → [details](#-ai-travel-assistant--plan-adjust-and-track-a-journey)
- **AI-assisted trip adjustment** — propose-then-apply before/after; server always recomputes cost itself
- **Per-stop detail + mark-visited + progress timeline**, with curated train/bus/shared-taxi routes between stops
- **Pause/resume trips** — activating a second trip auto-pauses the first instead of blocking it
- **AI-generated packing lists** (Gemini, static offline fallback) · **Budget tracking** with running spend
- **Group trips** — invite codes, shared itinerary, member roster
- **Group expense splitting** — log who paid, get a computed "who owes whom" settle-up (Splitwise's own greedy algorithm)
- **ILP/PAP permit guidance** — real portal/fee/processing time per state, plus the Dec 2024 foreign-national PAP reinstatement, plus a document checklist
- **Digital Journey Passport** — PDF trip summary with a tamper-evident SHA-256 hash chain → [details](#verifiable-digital-id--the-journey-integrity-hash)

### 🏨 Local Tourism Providers
- **Government-verified directory** — hotels, homestays, guides, artisans across all 8 states, each with a checkable citation and govt sign-off → [full pillar](#-local-tourism-providers--the-tourism-industry-pillar)
- **Surfaced inside the trip** — every stop's detail sheet shows verified providers directly, not a separate app
- **Two-sided trust shown honestly** — "✓ Government Verified" and "Source: {citation}" always two separate facts
- **Call or WhatsApp directly** — no directory middleman
- **Operator Self-Service Portal** — verified businesses manage their own listing, story, tips, booking inbox, Explorer perks
- **Live Tourism Ecosystem Coverage dashboard** for government operators
- **16 government-approved itineraries**, 2 per NE state, 3 with a real government-tourism-board citation — the rest honestly labeled Aaraksha-assembled, never a fabricated approval

### 🚨 Safety
- **One-tap SOS** — hold-to-confirm, 7 categories, GPS-first with last-known-location fallback
- **Voice-triggered SOS** — Web Speech API wake phrase → confirm dialog; never fires automatically from voice alone
- **Dead Man's Switch** — miss a check-in interval, the system auto-fires SOS with your last known location
- **Travel Safety Index (TSI)** — 0–100 per destination, rule-based, hourly live-weather recalc, pushed over Socket.IO
- **Offline SOS** — structured SMS over a Twilio inbound webhook, zero data coverage needed
- **Emergency contact OTP verification** · **Verhoeff-validated Aadhaar** (real UIDAI checksum, not regex)
- **Privacy & Data Rights page** → [DPDP compliance](#legal--compliance)
- **Rescue team ETA**, **weather-triggered risk alerts**, **web push notifications**
- **AI Safety Briefing** — Gemini explains an already-computed TSI score, never scores anything itself
- **Digital Tourist ID** — rotating 5-min-expiry checkpoint QR, not a screenshottable static image
- **Geo-fencing zone alerts** for HIGH_RISK / RESTRICTED / ILP_REQUIRED stops
- **Rule-based anomaly detection** — flags gone-quiet (6h+) or off-route (60km+) trips before anyone presses SOS
- **File an E-FIR** — formal case-numbered report for something already happened, distinct from live-emergency SOS
- **On-device photo evidence** — COCO-SSD (TensorFlow.js) tags an E-FIR photo in-browser; never leaves the device until filed

### 🚑 Unified Rescue Network
- **One assignable rescuer pool** — official teams + verified volunteers, weighted-score-ranked, operator makes the final call
- **Govt-side volunteer onboarding** — identity confirmation, or a walk-in one-time-password provision
- **Real OSRM road routing** on every portal, with a straight-line fallback
- **Live GPS streaming** — ~9s position updates over Socket.IO across tourist/guardian/govt maps
- **Anti-fraud handoff verification** — DB-blocked close until a 6-digit HMAC code + 250m GPS proximity match; force-resolve requires a logged reason
- **Self-service status, govt-owned resolution** — rescuer reports EN_ROUTE/ARRIVED, only govt closes the case
- **Honest decline/cancel** — DECLINED vs CANCELLED, SOS reverts to ACTIVE for reassignment, real-time to all sides
- **In-app messaging** scoped to the live assignment only

### 🖥️ Government Operations
- **Live ops map** — every tourist/SOS/rescuer/anomaly in real time, plus a toggleable Risk Density layer
- **Real 3D terrain view** — free elevation tiles (MapLibre GL), no paid API key
- **SOS triage & assignment**, tracked EN_ROUTE → ARRIVED → RESOLVED
- **Auto-generated SOS incident PDFs** on resolution
- **E-FIR Queue** — role-based triage, FILED → ASSIGNED → UNDER_INVESTIGATION → RESOLVED, real-time both sides
- **Anomaly review**, **volunteer verification & roster**
- **District risk overview** — live counts, weather, TSI, plus the trained Predictive Risk Model score
- **Checkpoint QR scanning**, chained into the Journey Integrity Hash
- **CCTNS/BNS-aligned E-FIR reference**, **analytics + PDF export**, **role-scoped access** (6 govt roles)

### 🌐 Community & Live Content
- **Rich destination reviews** — cost, crowd level, felt-safe flag, transport/food/accessibility, photos
- **Scam/safety reports**, filterable · **Community Safety Hotspots** — most-reported destinations, last 90 days
- **Curated rotating destination news** — ~45 hand-written items, time-slot rotation
- **Real News & Alerts feed** — filterable, paginated, active trip's news pinned at top
- **Risk overview in the tourist app**, same live view government sees

### 👪 Guardian Portal
- **Zero-friction access** — random token in the URL, no login
- **Five status states** — safe, check-in-due, SOS active, help-dispatched, no-signal
- **Live rescuer tracking** once dispatched, same picture govt sees
- **In-app messaging**, always available, not gated on an active SOS
- Live location, battery, medical info, auto-refresh 30s

### 📴 Offline-first
- **IndexedDB (Dexie.js)** queues SOS/location when offline, syncs on reconnect
- **Cached safety guides** — hospital/police/rescue contact available with no signal
- Every safety mechanism degrades gracefully rather than failing outright

---

## 🔗 Verifiable Digital ID — the Journey Integrity Hash

<details>
<summary><b>How the chain is built, and why it's real</b> — click to expand</summary>

"Blockchain-based Digital ID" is where this project started — SIH25002's own phrasing — and it
stayed in scope even after moving to the self-defined Student Innovation category, because the
research above turned up the same pattern repeatedly: most public implementations of that exact
phrase turn out to be a QR code pointing at a static profile — nothing chained, nothing
tamper-evident, nothing a third party could actually verify without trusting the app's word for
it. Aaraksha implements the actual primitive blockchain is built on — a cryptographic hash
chain — over every fact that makes up a tourist's verified journey, without the operational
overhead of standing up a real distributed ledger for a single-organization system that doesn't
need one.

**How the chain is built**, straight from `passport.service.js`:

1. **Genesis block** — a SHA-256 hash of the trip's own unchanging facts: destinations, dates,
   travel type, budget, and the TSI score at booking time.
2. **Every check-in, SOS event, and government checkpoint scan**, merged into one true
   chronological sequence (they live in three separate tables and are fetched pre-sorted in
   different directions, so the merge itself is re-verified by timestamp — not trusted as
   already-interleaved) and folded one at a time: `hash(n) = SHA256(hash(n-1) + event(n))`.
3. **The final hash** is printed on the Journey Passport PDF and independently recomputable at
   any time from live platform records via `GET /journey-passport/:tripId/hash` — a bad actor
   would need to alter platform data itself and get every downstream hash to still match, not
   just edit a PDF.

```mermaid
flowchart LR
    G["Genesis block\nSHA-256 of trip facts\n(destinations, dates, TSI@booking)"] --> H1
    subgraph Chain["hash(n) = SHA256(hash(n-1) + event(n))"]
        H1["hash 1\n+ check-in"] --> H2["hash 2\n+ SOS event"]
        H2 --> H3["hash 3\n+ govt checkpoint scan"]
        H3 --> H4["hash 4\n+ ..."]
    end
    H4 --> F["finalHash\nprinted on Passport PDF +\nGET /journey-passport/:id/hash"]
    style G fill:#fffbeb,stroke:#f59e0b
    style F fill:#ecfdf5,stroke:#059669
```

**Why the checkpoint-scan link matters most.** A government checkpoint scan is the one event in
this chain that a citizen doesn't control — it's a police or ILP officer's own physical
verification of the tourist, at a specific place and time. Chaining it into the same hash as the
tourist's self-reported check-ins means the *government's own record* becomes part of the
tourist's cryptographic identity trail, not a separate, disconnected log table nobody
cross-checks. That's the "Digital ID" claim actually made concrete.

**Verified live**, not just claimed — this is a table any judge can watch you reproduce in front of
them:

| Step | `finalHash` | `eventCount` | `checkpointScanCount` |
|---|---|---|---|
| Before scan | `9952f113…c8947` | 3 | 0 |
| Officer scans the tourist's checkpoint QR | `e4e3b7d8…125bf` | 4 | 1 |
| Re-fetched again, nothing changed | `e4e3b7d8…125bf` *(identical)* | 4 | 1 |

The hash changes exactly once, exactly when a real event happens, and is byte-for-byte
deterministic on every subsequent fetch — the two properties that make a hash chain actually
mean something instead of just sounding like it does.

</details>

---

## 🤖 A real trained model — the Predictive Risk Score

> **Not a prompt. Not an API call to someone else's model. A model *we* wrote, *we* trained, and
> *we* can show you the loss curve for.**

<details>
<summary><b>The model, the training run, and the benchmark</b> — click to expand</summary>

Gemini in this platform is deliberately never asked to score or decide anything — it only
explains an already-computed number in plain language (see the AI Safety Briefing below), the
same "AI never makes the call, only explains it" honesty stance TSI is built on. That leaves a
fair question: where's the actual machine learning? Here:

`backend/scripts/trainRiskModel.js` trains a real binary logistic regression —
`backend/src/ml/logisticRegression.js` is the entire model, about 90 lines of batch gradient
descent on L2-regularized cross-entropy loss, **no scikit-learn, no TensorFlow, no ML framework
in between — the math is ours.** No public, destination-level tourist-incident dataset exists for
India to train against, so rather than falsely claim one, the trainer generates a labeled corpus
from a probabilistic incident-rate function over real, already-collected destination risk factors
(connectivity, difficulty, altitude, zone classification, hospital distance, monsoon season) —
stated plainly in both the training output and the live UI tooltip, not hidden. The training
pipeline itself doesn't change the moment real incident records exist to train on instead; only
the label source would.

**📊 Benchmark — a real training run, from the actual console output:**

| Metric | Score | | Metric | Score |
|---|---|---|---|---|
| 🎯 Test accuracy | **75.6%** | | 🧪 Training corpus | 4,000 examples |
| 🔍 Precision | **69.0%** | | ✂️ Train / test split | 3,200 / 800 |
| 📡 Recall | **48.5%** | | 🔁 Reproducibility | Seeded — bit-identical every run |
| ⚖️ F1 score | **0.57** | | 🧩 Engineered features | 17 |

| Sanity check | Predicted incident probability |
|---|---|
| 🟢 Kaziranga *(safest seeded destination)* | 22.5% |
| 🔴 Dzukou Valley *(most extreme seeded destination)* | 74.7% |

The learned weights are directionally sane on inspection — `monsoon_season`, `connectivity_NONE`,
and `difficulty_EXTREME` are the three largest positive contributors, `difficulty_EASY` and
`connectivity_GOOD` the largest negative ones — which is exactly what a real fit against
risk-grounded labels should produce, not a random or overfit result. Every prediction shown in
the govt Risk Overview page is explainable down to its top four contributing features, live, not
just a bare percentage — reproduce the whole run yourself with `npm run train:risk-model`.

</details>

---

## 🧭 AI Travel Assistant — plan, adjust, and track a journey

> **The same honesty boundary the Predictive Risk Score is built on, applied to trip planning: AI
> explains, it never decides.** Every cost, duration, and safety number a tourist sees came out of
> a deterministic scorer this team wrote — Gemini's only job is to narrate a number that already
> exists, in plain language, never to invent or adjust one itself.

<details>
<summary><b>The full six-step pipeline, dataset provenance, and the deterministic-cost guarantee</b> — click to expand</summary>

A floating assistant (bottom-right, every tourist screen) turns "plan a Northeast India trip" from
a multi-hour research task — the actual problem this feature targets — into a single conversation,
without ever hiding the real numbers behind the AI's prose.

**1. Describe a trip, and confirm it — the form is a fallback, not the default path** — free text
("6 days in Meghalaya from Delhi, under ₹20,000, mostly nature") pre-fills
origin/region/days/budget/interests via Gemini intent extraction and lands directly on a
read-only confirm screen, not the raw structured form. From there: **Edit details** drops into
the full field-by-field form for anything the extraction missed, or a chat-style box underneath
takes a follow-up ("make it 3 days shorter") and re-scores before anything is built — the same
propose-then-apply discipline point 4 below uses for an already-committed trip, applied one step
earlier, to the plan itself.

**2. A deterministic scorer builds the itinerary** — `travelScoring.service.js` is pure,
synchronous, and network-free: it greedily orders candidate destinations by geographic proximity,
then scores the whole itinerary on budget fit, duration fit, interest-keyword match, a
backtracking-distance penalty, verified-local-provider coverage per stop, and a real Travel Safety
Index pass (`tsi.service.js`) per stop. Real curated `typical_routes` legs are used where they
exist; an uncurated pair falls back to a haversine-distance estimate, **always flagged
`estimated: true`** in the response, never presented as a measured fact.

**Verified local providers are now a real planning signal, not just a display-time count** — a
stop with government-verified hotels/homestays/guides/artisans contributes to the itinerary's
overall score (saturating at 3 verified operators per stop, so one dense district can't dominate
the whole score), at a deliberately modest 10% weight so it nudges toward better-served
destinations without overriding budget, safety, or a tourist's stated interests. This was held back
from the first pass that stood up the provider dataset — done only once there was enough verified
depth (44 real operators across all 8 states) for the signal to mean something, with its own test
coverage added alongside it, not bolted on after.

**3. Gemini narrates the result** — `generateJourneyNarrative` receives the already-computed
itinerary and writes the "why this route" bullets and journey story; it cannot alter the stops,
cost, or score it's describing. If the Gemini call fails, a templated fallback narrative takes
over and says so (`narrativeSource: 'TEMPLATED_FALLBACK'`) — the number underneath never changes
either way.

**4. Adjusting an already-committed trip is propose-then-apply, never direct** — a natural-language
edit ("remove Cherrapunji", "I have ₹4,000 less now") returns a full before/after comparison the
tourist reviews first. Applying it sends only destination **identity** (stop IDs + day count) back
to the server, which recomputes `totalCostInr` itself via the same deterministic scorer — a
client-supplied cost number is never trusted or persisted, closing the exact kind of gap that lets
a tampered request silently under-report a trip's real cost. A real bug lived here until it was
traced and fixed: a relative phrase like "₹4,000 less" asked Gemini to both *understand* the
change and *do the arithmetic* against the current budget in one step, and LLM sampling variance
on that second part is exactly why it "sometimes worked" — Gemini now only reports a signed delta
or an absolute value, never the arithmetic result, and `gemini.service.js#resolveDeltas` (with its
own unit tests, no live API call needed) applies it deterministically server-side.

**5. Once committed, a stop becomes a real place to explore** — tapping it opens full destination
info (description, best season, government advisory, nearest hospital) plus every curated route to
reach it from the previous stop, train/bus/shared-taxi options included where the dataset has them.
Marking a stop visited pre-fills an honest, editable spend estimate (an even share of the trip's
planned budget — there's no bank/UPI integration behind this, so it's disclosed as an estimate, not
a claim of a known real number) and updates a real progress timeline and a running "spent so far"
total, not a static itinerary that never changes once booked. Marking the last stop visited prompts
to close the trip out — a real gap this closed: a trip used to stay `ACTIVE` forever with nothing
ever detecting "every stop is done," since that transition was manual and undiscoverable.

**6. A trip can be paused and resumed, not just abandoned** — activating a second trip while one is
already active no longer throws an error; it auto-pauses the first (a real `PAUSED` status, its own
tab on the trips list) so a tourist genuinely juggling two plans — a short detour while a longer
trip is paused, say — can switch between them without cancelling either one.

```mermaid
flowchart LR
    A["🗣️ Free text"] --> B["Gemini: intent\nextraction only"]
    B --> C["Confirm screen —\nEdit details or\nrefine by chat"]
    C --> D["travelScoring.service.js\n(pure, deterministic)"]
    D --> E["Gemini: narrate the\nALREADY-COMPUTED result"]
    E --> F["Interactive journey card\n— real cost, real routes"]
    F -- "commit" --> G["Real trip — stop detail,\nmark-visited, timeline"]
    F -- "later: adjust" --> H["Propose full before/after"]
    H -- "apply" --> I["Server recomputes cost\nfrom stop IDENTITY only —\nnever trusts client cost"]
```

**The dataset behind it is curated, not scraped or invented.** `typical_routes` and
`destination_reviews` grow through a supervised multi-agent process documented in
[Data Curation](./docs/data-curation.md) — every route requires a `source` (a named government/OSM reference,
a cited article, or `destination_reviews` real traveller data; proprietary booking platforms are
explicitly off-limits), reviewed before insertion, with every session logged. All 8 Northeast
states currently have 2–3 sourced destinations and at least one sourced intra-state route.

| Layer | What it does | Where |
|---|---|---|
| 🧮 Deterministic scorer | Budget/duration/interest fit, backtracking penalty, verified-provider coverage, per-stop TSI — pure function, unit-tested, no network | `travelScoring.service.js` |
| 🗣️ Intent extraction | Free text → structured form fields; never bypasses tourist confirmation | `gemini.service.js#extractPlanningIntent` / `#extractTripIntent` |
| ✍️ Result narration | Explains numbers already computed; offline-fallback narrative if the AI call fails | `gemini.service.js#generateJourneyNarrative` |
| 🔁 Propose-then-apply | Adjustment is scored and shown before any write; apply recomputes cost server-side from stop identity only | `travelPlanner.service.js#adjustTrip` / `#applyTripAdjustment` |
| 🛣️ Route data | Curated legs between destinations, multiple modes per pair where sourced; uncurated pairs get a flagged haversine estimate | `typical_routes`, `travelPlanner.repository.js#findRoutesBetween`/`#findRoutesAmong` |
| 📚 Dataset provenance | Multi-agent curation spec, Tier A/B/C source policy, required `source` column | [Data Curation](./docs/data-curation.md), migration `026_travel_data_provenance` |

</details>

---

## 🏨 Local Tourism Providers — the tourism-industry pillar

<details>
<summary><b>The trust pipeline, the numbers, and the PS 26204 answer</b> — click to expand</summary>

SIH PS 26204 asks for a solution that can *"boost the current situation of the tourism industries
including hotels, travel and others."* The AI Travel Assistant above answers "travel." This is
the direct answer to "hotels ... and others" — and it was built the same way everything else in
this README was: with a real trust boundary, real sourced data, and an explicit decision about
what *not* to build.

**The decision, stated plainly:** this is a **discovery and trust layer, not a booking platform.**
No payments, no inventory, no availability calendar — building an OTA clone would be a different,
much larger product, and isn't what an open-innovation PS asking to *boost* an industry is
requesting. What Aaraksha adds instead is the thing that's actually missing: a way for a real
local hotel, homestay, guide, or artisan cooperative to be **discoverable and trustworthy** inside
the exact moment a tourist is planning their trip.

**The trust model is borrowed on purpose, not invented from scratch** — a "local provider" needs
the same shape of trust this platform already proved out for **citizen rescue volunteers**: a
real-world identity with a checkable citation that is *not* safe to surface to a tourist until a
government reviewer has verified it. Same reasoning, same review queue pattern, same "citation
alone isn't enough" discipline — just a different actor.

| Stage | What happens | Where |
|---|---|---|
| 🔎 Sourced | A real hotel/homestay/guide/artisan cooperative, cited from an official state tourism/handicrafts/cooperative department page or an OpenStreetMap node — never a booking aggregator (OYO, MakeMyTrip, Airbnb, TripAdvisor, Booking.com are explicitly banned as sources) | [Data Curation](./docs/data-curation.md), `local_operators.source` (`NOT NULL` at the DB level) |
| ⏳ Pending | Inserted `is_verified = false` — real and cited is not yet the same as safe-to-surface | `local_operators` table, migration `027_local_operators` |
| ✅ Verified | A government operator reviews the citation and approves it in the Command Center — the same identity-confirmation discipline as volunteer onboarding | `POST /govt/local-operators/:id/verify`, `LocalOperatorsPage.tsx` |
| 📲 Visible | Only verified, active providers are ever returned to a tourist — enforced as a hard-coded `WHERE is_verified = true` in the repository layer, not a frontend filter | `localOperator.repository.js#findByDestinationId`, `StopDetailSheet.tsx`, `JourneyResultCard.tsx` |
| 🔑 Account issued | Optionally, a govt reviewer can also generate a login for the verified business — reuses the existing volunteer/rescuer auth table via a distinct `account_type` (`RESCUER` vs `OPERATOR`) and a role-scoped JWT, rather than a second parallel auth system | `POST /govt/local-operators/:id/create-account`, `requireAccountType()` middleware, `OperatorDashboardPage.tsx` |
| 📊 Discovery measured, not assumed | Every real, *committed* trip (not a preview) logs which verified providers its itinerary actually surfaced — a real "did this boost visibility" count per operator for the tourism department, not a vanity number, and it fails silently (logged, never blocking) if the write itself ever has a problem | `provider_itinerary_impressions` table, `travelPlanner.service.js#commitJourney`, `GET /govt/local-operators/analytics`, `LocalOperatorsPage.tsx` |

**Two distinct facts, always shown as two distinct lines** — every provider card carries a
"✓ Government Verified" badge (who confirmed it) and a separate "Source: {citation}" line (where
the underlying fact came from). They're deliberately never merged into one sentence: a citation
being real isn't the same claim as a government reviewer having signed off on it, and this
platform doesn't blur the two just to make a card read cleaner.

**Real numbers, not a seed script's placeholder count** — as of this build: **71 real, cited
providers across all 8 Northeast Indian states** (15 hotels, 14 homestays, 9 registered guides,
6 artisan/handicraft cooperatives, 21 tour operators, 6 vehicle rentals) — including an
independently-confirmed individual guide in every single state, not just an association — 68
already government-verified, a handful deliberately left pending as a genuine, uncoached
verify-it-live moment rather than a staged demo. 27 of the 71 also carry a sourced, human-written
story and self-reported sustainability tags, added across two independently spot-checked curation
rounds. Every citation is independently checkable — official OSM node/way IDs, or a named
government department page — the full sourcing discipline, including one caught and corrected
fabrication left in the record rather than quietly fixed, is in [Data Curation](./docs/data-curation.md).

</details>

<p align="center">
  <img src="./docs/screenshots/govt-local-operators.png" alt="Govt Command Center Local Tourism Providers page" width="80%">
</p>
<p align="center"><sub>Govt Command Center — verified-provider roster and live Tourism Ecosystem Coverage dashboard</sub></p>

<p align="center">
  <img src="./docs/screenshots/tourist-local-providers.png" alt="Tourist app showing verified local tourism providers on a stop's detail sheet" width="40%">
</p>
<p align="center"><sub>Tourist PWA — verified local providers surfaced directly on a trip stop</sub></p>

---

## 🚑 The unified Rescuer network

Two kinds of rescuer used to be structurally separate systems: official rescue teams (a shared
phone number, manually dispatched by a govt operator) and citizen volunteers (individually
logged in, only reachable by an automatic proximity broadcast — no manual assignment path
existed, and no live location ever left their registered base). Neither had a real road route or
a live position. This is the actual flow now, end to end — every arrow below is a real Socket.IO
event or API call, not an aspirational diagram:

```mermaid
sequenceDiagram
    participant T as 🧭 Tourist
    participant B as ⚙️ Backend
    participant G as 🖥️ Govt Operator
    participant R as 🚑 Rescuer
    participant F as 👪 Guardian

    T->>B: SOS (online API or offline SMS)
    B-->>G: SOS_RECEIVED (live ops map)
    B-->>F: GUARDIAN_SOS_ALERT
    G->>B: Assign rescuer (team or volunteer)
    B-->>R: VOLUNTEER_SOS_ALERT / VOLUNTEER_ASSIGNED
    B-->>F: GUARDIAN_STATUS_CHANGE (help dispatched)
    loop every ~9s while en route
        R->>B: Live GPS position
        B-->>T: RESCUER_LOCATION_UPDATE
        B-->>F: GUARDIAN_LOCATION_UPDATE
        B-->>G: live map marker moves
    end
    T->>T: Reveal handoff code (never leaves the device until shown)
    R->>B: Verify handoff code + GPS proximity
    B-->>T: HANDOFF_VERIFIED
    B-->>F: "Help arrived and was verified"
    G->>B: Resolve SOS (blocked until handoff verified)
    B-->>T: SOS_RESOLVED
```

**1. A volunteer gets an account** — either they register themselves in Aaraksha Sahayak, or a
district officer provisions one directly for a walk-in local responder, generating a one-time
password on the spot.

<p align="center">
  <img src="./docs/screenshots/rescuer-auth.png" alt="Aaraksha Sahayak registration and login" width="340">
</p>

**2. A district officer verifies their identity** before they're eligible for dispatch — an
explicit confirm step, not a one-click rubber stamp, since verifying grants access to a
tourist's exact live location the moment they're assigned.

<p align="center">
  <img src="./docs/screenshots/govt-volunteers.png" alt="Govt Volunteers page — account provisioning and credentials" width="700">
</p>

**3. An SOS comes in, and the govt operator picks a rescuer** — official team or verified
volunteer, in one distance-sorted panel, badge-differentiated so the operator always knows
which kind of rescuer they're sending.

<p align="center">
  <img src="./docs/screenshots/govt-assign-rescuer.png" alt="Govt SOS Management — combined team/volunteer assign panel" width="700">
</p>

**4. Aaraksha Sahayak opens straight into a live, full-screen map** — a real OSRM road route to
the person in need (not a straight line), live distance/ETA, one-tap handoff to Google Maps
turn-by-turn, and self-reported `EN_ROUTE` → `ARRIVED` progress.

<p align="center">
  <img src="./docs/screenshots/rescuer-active-job.png" alt="Aaraksha Sahayak — live navigation to an SOS" width="340">
</p>

**5. The family sees the exact same live picture** — the assigned rescuer's real-time position
and road route, on the same no-login Guardian link they already had open.

<p align="center">
  <img src="./docs/screenshots/guardian-rescuer-live.png" alt="Guardian Portal — live rescuer tracking" width="340">
</p>

The rescuer's position streams over Socket.IO into three rooms at once — tourist, guardian, govt
— so all three views move in near-real-time off the same GPS ticks, not three separate polling
loops drifting out of sync.

---

## 🗺️ Routing Engine — OSRM & Contraction Hierarchies

> **Named honestly, not oversold.** The road-routing algorithm is [OSRM](http://project-osrm.org/)'s
> own — we call it, we don't reimplement it. What *is* ours is the resilience and honesty layer
> wrapped around a free public service: throttled requests, a straight-line degrade path, and a
> disclosed answer for the one thing OSRM's public instance genuinely can't see — live traffic.

<details>
<summary><b>How the throttling, fallback, and delay-detection actually work</b> — click to expand</summary>

Every live map in this system — tourist, rescuer, guardian — calls the public OSRM demo server
directly from the browser (`router.project-osrm.org/route/v1/driving/...`, no API key, nothing to
configure) and asks for the `driving` profile. OSRM answers that query using **Contraction
Hierarchies**: the road graph is pre-processed offline into a layered shortcut network, so a
route that would take a naive Dijkstra search seconds to compute over the full OpenStreetMap graph
resolves in single-digit milliseconds at query time. That's genuinely "the best possible path" for
a static road network — this system calls a real, production-grade routing engine, not a
from-scratch shortest-path implementation.

```mermaid
flowchart LR
    A["📍 Rescuer GPS tick"] --> B{"Moved ≥30m or\n≥8s since last fetch?"}
    B -- No --> C["Skip — reuse last route"]
    B -- Yes --> D["OSRM: Contraction\nHierarchies query"]
    D -- "route found" --> E["✅ Real road polyline\ndistance · ETA"]
    D -- "unreachable / no route" --> F["↔️ Straight-line fallback\nmap never breaks"]
    E --> G{"Elapsed time ≫\noriginal ETA?"}
    F --> G
    G -- Yes --> H["🧭 Delay nudge —\nsuggest Google Maps\nlive traffic"]
    G -- No --> I["Keep navigating\nin-app"]
```

**What's disclosed, not hidden**: OSRM's public instance routes purely on road geometry — it has
no live-traffic layer. Rather than silently present a possibly-stale ETA as gospel, the system
tracks each assignment's *original* computed ETA as a baseline and compares it against real
elapsed time. If a rescuer is still en route at 1.6× their original estimate — a deliberately
generous margin for single-lane mountain terrain, not routine noise — every screen watching that
assignment (rescuer, tourist, guardian) surfaces an honest, actionable nudge: *"Taking longer than
expected — check for a detour, or open Google Maps for live traffic conditions,"* one tap into
Google's own traffic-aware routing. The system never pretends to out-route Google on live
conditions it structurally cannot see — it detects when that's likely happening and hands off.

| Layer | What it does | Where |
|---|---|---|
| 🛣️ Route computation | Contraction Hierarchies over the OSM road graph | OSRM's own public server |
| 🐢 Client-side throttle | Skip a refetch unless ≥30m moved *and* ≥8s elapsed | `lib/osrm.ts`, all 3 live-tracking portals |
| ↔️ Resilience | Any failure (timeout, no route, malformed response) degrades to a straight line, never a crash | `lib/osrm.ts#getRoute` — verified live by blocking the endpoint entirely mid-session |
| 🧭 Delay honesty | Elapsed time vs. original ETA, 1.6× margin, triggers a Google Maps handoff suggestion | `ActiveJobPage.tsx`, `RescueTrackingCard.tsx`, guardian `TrackingPage.tsx` |
| 📡 Live cross-portal signal | Rescuer's "Navigate" toggle broadcasts a real-time pill to tourist + guardian | `RESCUER_NAVIGATING_STATE` socket event |

</details>

---

## 🛰️ NTN — a satellite fallback transport

> **Named honestly, not oversold.** Aaraksha does not have a satellite modem, and no browser can
> talk to one — there's no web API for it. What this is: a **software channel simulator** for
> 3GPP Release-17 NTN (Non-Terrestrial Network / direct-to-device satellite), sitting behind the
> exact same SOS pipeline the manual button uses, so the system can demonstrate — honestly, today —
> how it would behave if a real NTN modem existed on the device.

<details>
<summary><b>What's real vs. simulated, and the pipeline it shares with a manual SOS</b> — click to expand</summary>

NE India and Kashmir have real terrestrial dead zones — the entire reason Aaraksha exists. 3GPP
Release-17 direct-to-device NTN is a real, near-term answer to that: Apple's Emergency SOS via
satellite, Qualcomm Snapdragon Satellite, and BSNL's own announced Viasat-powered direct-to-device
service for India are all instances of the same idea reaching consumer devices. Aaraksha's SOS
pipeline is built **transport-agnostic** — it doesn't care whether an emergency arrived over the
internet, SMS, or a satellite hop, only that it arrived — so when real NTN hardware lands on
mainstream Indian devices, it's a new adapter behind an existing boundary, not a rewrite.

```mermaid
flowchart LR
    A["🛰️ Demo: send via\nsimulated NTN"] --> B["Channel simulator:\nsample signal/latency/loss"]
    B -- "satellite visible\n+ packet not lost" --> C["sos.service.js#createSOS\ntriggerType: NTN_SATELLITE"]
    B -- "no visibility\nor packet lost" --> D["❌ FAILED — audited,\nno SOS created"]
    C --> E["Same canonical fan-out as\na manual SOS: guardian alert,\ncluster check, volunteer alert"]
    C --> F["ntn_messages audit row\n(linked to the SOS)"]
    D --> F
    F --> G["🖥️ Govt dashboard —\nNTN_CHANNEL_STATUS tick"]
```

**What's real vs. simulated, stated plainly**: the channel model (signal strength, latency, packet
loss across three named conditions — clear sky, mountain valley, no visibility) is a deterministic
software simulator, with parameters *informed by* documented 3GPP NTN system characteristics and
propagation assumptions — not measured satellite telemetry, and not a claim that 3GPP publishes one
universal real-world number for every terrain type. What's real: the moment a simulated uplink is
marked delivered, it runs through the *exact same* SOS pipeline a manual trigger does — the same
transaction, the same guardian alert, the same proximity-cluster check, the same volunteer
fan-out — recorded end-to-end in an append-only `ntn_messages` audit table and visible live on the
government dashboard's NTN panel.

**Why this and not a real 5G/NTN stack for the prototype**: bringing up OpenAirInterface + Open5GS
in RF-simulation mode is a real integration path (documented below), but it's a multi-week effort
even for teams experienced with telecom stacks, and a browser-based PWA has no way to reach it
directly regardless — any real integration needs a native app or bridge process, a separate project
in its own right. None of that unseen complexity is verifiable in a short demo slot anyway; what's
verifiable is the pipeline shown above, working end-to-end, live.

| Layer | What it does | Where |
|---|---|---|
| 🎛️ Channel simulator | Three named conditions (clear sky / mountain valley / no visibility), each sampling signal/latency/packet-loss within a documented range | `simulators/ntnChannel.js` |
| 📡 Uplink attempt | Simulates the delay, rolls the packet-loss odds, always records the outcome | `services/ntn.service.js#sendViaNTN` |
| ♻️ Pipeline reuse | A delivered uplink calls the same `createSOS` every manual trigger uses — no second, partial copy of the fan-out logic | `services/sos.service.js` (one additive `triggerType` param) |
| 🗂️ Audit trail | Every attempt, delivered or failed, is an append-only row | `ntn_messages` (migration `024_ntn_messages`) |
| 🖥️ Live ops visibility | Signal/latency/loss and recent activity, ticking off a socket event | `NTN_CHANNEL_STATUS`, `NTNPanel.tsx` on the govt dashboard |
| 🔮 Real-hardware integration path | Documented future work, not attempted here: OpenAirInterface + Open5GS in RFsimulator mode, behind the same `ntn.service.js` boundary | Out of scope for this pass |

</details>

---

## 📸 Screenshots

All captured live from the running app — real seeded data, not mockups. Full-resolution files
are in [`docs/screenshots/`](./docs/screenshots/), free to drop straight into slides.

**Tourist PWA**

<table>
<tr>
<td width="50%"><img src="./docs/screenshots/tourist-landing.png" alt="Tourist landing page"><p align="center"><sub>Landing page — terrain-themed hero</sub></p></td>
<td width="50%"><img src="./docs/screenshots/tourist-trip-detail.png" alt="Trip detail with TSI and news"><p align="center"><sub>Trip detail — live TSI + destination news</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="./docs/screenshots/tourist-community.png" alt="Community reviews"><p align="center"><sub>Community — rich destination reviews</sub></p></td>
<td width="50%"><img src="./docs/screenshots/tourist-dashboard.png" alt="Tourist dashboard"><p align="center"><sub>Dashboard — SOS, DMS, active trips</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="./docs/screenshots/tourist-local-providers.png" alt="Verified local tourism providers on a trip stop"><p align="center"><sub>Stop detail — verified local providers, badge + source shown separately</sub></p></td>
<td width="50%"><img src="./docs/screenshots/tourist-group-expenses.png" alt="Group trip expense splitter with computed settle-up"><p align="center"><sub>Group tab — expense splitter with a computed "who owes whom" settle-up</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="./docs/screenshots/tourist-permit-assistant.png" alt="ILP and PAP permit guidance for Tawang, Arunachal Pradesh"><p align="center"><sub>Real, state-specific ILP/PAP permit guidance and document checklist</sub></p></td>
</tr>
</table>

**Govt Command Center**

<table>
<tr>
<td width="50%"><img src="./docs/screenshots/govt-login.png" alt="Govt Command Center login"><p align="center"><sub>Restricted-access authentication</sub></p></td>
<td width="50%"><img src="./docs/screenshots/govt-dashboard.png" alt="Govt dashboard"><p align="center"><sub>Dashboard — live stats at a glance</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="./docs/screenshots/govt-live-map.png" alt="Live ops map"><p align="center"><sub>Live Map — every active tourist, real time</sub></p></td>
<td width="50%"><img src="./docs/screenshots/govt-sos-management.png" alt="SOS management"><p align="center"><sub>SOS Management — incident triage list</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="./docs/screenshots/govt-assign-rescuer.png" alt="Combined team/volunteer assign panel"><p align="center"><sub>Assign Rescuer — official team or verified volunteer</sub></p></td>
<td width="50%"><img src="./docs/screenshots/govt-volunteers.png" alt="Volunteer onboarding and credentials"><p align="center"><sub>Volunteers — provisioning + one-time credentials</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="./docs/screenshots/govt-risk-overview.png" alt="Risk overview"><p align="center"><sub>Risk Overview — per-destination live risk</sub></p></td>
<td width="50%"><img src="./docs/screenshots/govt-analytics.png" alt="Analytics dashboard"><p align="center"><sub>Analytics — incident trends + PDF export</sub></p></td>
</tr>
<tr>
<td width="50%" colspan="2"><img src="./docs/screenshots/govt-local-operators.png" alt="Local Tourism Providers roster and coverage dashboard"><p align="center"><sub>Local Tourism Providers — verified roster + Tourism Ecosystem Coverage</sub></p></td>
</tr>
</table>

**Guardian Portal** — mobile view, since this is the link a family member opens on their phone

<table>
<tr>
<td width="50%"><img src="./docs/screenshots/guardian-portal.png" alt="Guardian Portal live SOS tracking, mobile view"><p align="center"><sub>SOS active — no rescuer dispatched yet</sub></p></td>
<td width="50%"><img src="./docs/screenshots/guardian-rescuer-live.png" alt="Guardian Portal live rescuer tracking, mobile view"><p align="center"><sub>Help dispatched — live rescuer + road route</sub></p></td>
</tr>
</table>

**Aaraksha Sahayak** — the newest portal, teal to stay visually distinct from the other three; serves rescuers and govt-verified local businesses under one shared login

<table>
<tr>
<td width="33%"><img src="./docs/screenshots/rescuer-auth.png" alt="Aaraksha Sahayak login"><p align="center"><sub>Log in / register</sub></p></td>
<td width="33%"><img src="./docs/screenshots/rescuer-home.png" alt="Aaraksha Sahayak home screen"><p align="center"><sub>Home — availability toggle, nearby alerts</sub></p></td>
<td width="33%"><img src="./docs/screenshots/rescuer-active-job.png" alt="Aaraksha Sahayak live navigation"><p align="center"><sub>Active job — live route + status</sub></p></td>
</tr>
</table>

---

## 🏗️ Architecture at a glance

<p align="center">
  <img src="./docs/architecture/system-architecture.png" alt="Aaraksha system architecture — four portals, one Express/PostgreSQL backend, realtime Socket.IO spine, offline SMS path, simulated NTN path" width="100%">
</p>

**Backend stack:** Node.js ≥20 · Express · PostgreSQL (raw `pg`, zero ORM) · JWT + bcrypt ·
Socket.IO · node-cron (DMS checks every minute, anomaly detection every minute, weather+TSI
hourly, news rotation every 20 min) · Twilio (outbound SMS + inbound webhook) · Google Gemini ·
PDFKit · multer (photo uploads) · Zod validation · pino structured logging.

**Frontend stack** (all four apps, independently deployable Vite projects sharing one design
system — see [Design System](./docs/design-system.md)): Vite 8 · React 19 · TypeScript 6 · Tailwind CSS
3.4 · shadcn/ui (Radix primitives) · Zustand · TanStack Query v5 · Dexie.js (tourist offline
sync) · react-leaflet (govt live map, Guardian/tourist/Rescuer live-route maps) · MapLibre GL JS
(govt 3D terrain view, free elevation tiles, no API key) · OSRM (real road routing, no API key) ·
TensorFlow.js + COCO-SSD (on-device E-FIR photo tagging) · react-hook-form + Zod · Socket.IO
client · jsQR (checkpoint camera scanning).

Every layer is intentionally narrow: controllers hold no SQL or business logic, all queries live
in repositories, and every multi-table write that must be atomic goes through a single
`withTransaction()` helper. The full mechanism, traced from the actual source, is diagrammed in
[`system-architecture.svg`](./docs/architecture/system-architecture.svg).

---

## 📈 By the numbers

| | |
|---|---|
| **Portals** | 4 (Tourist PWA, Govt Command Center, Guardian Portal, Aaraksha Sahayak) |
| **API endpoints** | 168, across 19 route groups |
| **Database tables** | 39 |
| **Migrations** | 41, applied incrementally — every schema change is a reviewable, named diff, never a hand-edited table |
| **Destinations seeded** | 19, across all 8 Northeast Indian states (Assam, Meghalaya, Nagaland, Arunachal Pradesh, Sikkim, Manipur, Mizoram, Tripura) — each with real altitude, connectivity, ILP, hospital, and police-station data |
| **Verified local tourism providers** | 68 government-verified (71 total, real and cited) — hotels, homestays, registered guides, artisan cooperatives, tour operators, and vehicle rentals across all 8 states, 27 with a sourced story/sustainability profile — see [Local Tourism Providers](#-local-tourism-providers--the-tourism-industry-pillar) |
| **Curated `typical_routes` legs** | 24, each with a required, reviewed `source` — see [AI Travel Assistant](#-ai-travel-assistant--plan-adjust-and-track-a-journey) |
| **Government-approved / curated itineraries** | 16, two real routes per NE state — 3 carrying an actual government-tourism-board citation (Meghalaya, Sikkim, Assam), the rest honestly self-assembled rather than a fabricated approval — see [Local Tourism Providers](#-local-tourism-providers--the-tourism-industry-pillar) |
| **Destinations with curated highlights** | 17 of 19 — sourced "what makes this place unique" facts (Wikipedia, UNESCO, Britannica, official tourism sites), the 2 non-Northeast seed rows excluded |
| **Curated news items** | ~45, hand-written per destination, auto-rotating |
| **Tourist app screens** | 19 routes (landing, auth + forgot-password, dashboard, trip planning + detail with 6 tabs including group expenses, a real destination detail page with real-time permit guidance, check-in, SOS, checkpoint pass, a filterable news feed, incident reporting, community, advisory, profile + edit + privacy, help) |
| **Govt app screens** | 9 (login, dashboard, SOS management, E-FIR queue, volunteers, live map, risk overview, analytics, checkpoint scan) |
| **Aaraksha Sahayak screens** | 4 (auth, home, active job — live map, operator dashboard) — the same app also serves govt-issued local-operator accounts, RBAC-gated from rescuer routes |
| **Cron jobs** | 4 (Dead Man's Switch monitoring, anomaly detection, weather + TSI refresh, destination news rotation) |
| **Real-time events** | 37 distinct Socket.IO event types |
| **SOS incident categories** | 7 (medical, lost, trapped, disaster, missing, crime, other) |
| **E-FIR incident categories** | 8 (theft, harassment, assault, fraud, lost document, vehicle accident, property damage, other) |
| **Rescuer types** | 2 (official rescue teams, govt-verified citizen volunteers) — one assignable pool |
| **Languages** | 3 (English, Hindi, Assamese) — full key parity enforced at dev-time, not just an `en.json` with gaps |
| **Predictive Risk Model** | 1 real trained logistic regression · 4,000-example corpus · 75.6% test accuracy · 17 explainable features |

---

## 📁 Repository layout

> The layout below is the private source repository's, referenced throughout this doc for
> context — not this public repo's own layout (see [📚 Documentation map](#-documentation-map)
> for what's actually here).

<details>
<summary><b>Full directory tree</b> — click to expand</summary>

```
Aaraksha/                            (private source repo)
├── README.md                        this file
├── Architecture.md                  locked tech stack, naming, directory conventions
├── API_GUIDE.md                     HTTP verbs, error codes, response envelope
├── DB_GUIDE.md                      table definitions, relationships, query rules
├── UI_GUIDE.md                      design tokens, components, offline strategy
├── chatbot.md                       supervised multi-agent dataset-curation spec — see
│                                     AI Travel Assistant above
├── docs/testing/                    12-phase adversarial QA pass — see docs/testing/README.md
│
├── backend/
│   ├── src/
│   │   ├── app.js                   Express app: middleware chain, routes, error handler
│   │   ├── server.js                HTTP server, Socket.IO init, graceful shutdown
│   │   ├── config/                  env validation, CORS, Gemini/Twilio/push clients
│   │   ├── constants/                enums, error messages, socket event names
│   │   ├── routes/                  19 route modules → controllers (incl. travelPlanner.routes.js,
│   │   │                             ntn.routes.js, incident.routes.js)
│   │   ├── controllers/             thin HTTP handlers
│   │   ├── services/                business logic, transaction boundaries — incl.
│   │   │                             anomaly.service.js, incident.service.js,
│   │   │                             efirReport.service.js, passport.service.js
│   │   │                             (Journey Integrity Hash chain), travelPlanner.service.js
│   │   │                             + travelScoring.service.js (deterministic itinerary scorer)
│   │   ├── repositories/            all SQL, parameterized, one per table cluster
│   │   ├── middleware/              auth (JWT, algorithm-pinned), validate (Zod),
│   │   │                             rate limiting, errors
│   │   ├── validators/              Zod schemas per domain
│   │   ├── socket/                  Socket.IO init + typed emitters
│   │   ├── cron/                    DMS, anomaly detection, weather+TSI,
│   │   │                             destination-news rotation jobs
│   │   ├── data/                    curated destination news bank +
│   │   │                             riskModel.weights.json (frozen trained model)
│   │   ├── ml/                      logisticRegression.js (from-scratch trainer)
│   │   │                             + features.js (shared train/serve encoding)
│   │   ├── database/                connection pool, transaction helper
│   │   └── migrations/              node-pg-migrate schema — 39 tables across 41 migrations
│   ├── scripts/
│   │   ├── preflight.js             env/DB connectivity check before setup
│   │   ├── seed.js                  idempotent demo data (--reset flag available)
│   │   ├── seedDemoContent.js       trips/reviews/scam reports across every demo account
│   │   ├── seedAnalyticsHistory.js  30-day realistic incident history for the analytics dashboard
│   │   ├── seed_destination_highlights.js  real, sourced "what makes this place special" bullets
│   │   ├── seed_curated_itineraries.js     real, sourced govt-approved/curated multi-day routes
│   │   └── trainRiskModel.js        trains the Predictive Risk Model, writes riskModel.weights.json
│   ├── tests/
│   │   ├── unit/, integration/      vitest unit + integration suite
│   │   └── eval/                    travelPlanner.benchmark.js — 6 fixed queries against the
│   │                                 real dev DB, checked for sane scores/safety/backtracking
│   ├── postman/                     Postman collection + environment
│   ├── .env.example                 every required env var, documented
│   └── package.json
│
└── frontend/
    ├── tourist/                     Tourist PWA — :5173
    │   ├── src/pages/               landing, auth, dashboard, trips (create/detail/list),
    │   │                             destinations (real, documentary-style detail page),
    │   │                             safety (SOS/check-in/checkpoint pass/E-FIR filing/news feed),
    │   │                             community, advisory, profile
    │   └── src/components/shared/   TravelAssistantFAB.tsx (Build My Journey / adjust),
    │                                 StopDetailSheet.tsx + DestinationInfo.tsx (shared
    │                                 destination-info rendering — the sheet and the standalone
    │                                 page both use it, not two copies of the same content)
    ├── govt/                        Government Command Center — :5174
    │   └── src/pages/               login, dashboard, SOS management, E-FIR queue,
    │                                 volunteers, live map (incl. anomaly markers),
    │                                 risk overview, analytics, checkpoint scan
    ├── guardian/                    Guardian Portal — :5175
    │   └── src/pages/               tracking page (token in URL, no auth)
    └── volunteer/                   Aaraksha Sahayak — :5176 (folder name predates two
        │                             rebrands; serves two account types under one login —
        │                             RESCUER (home: availability + nearby alerts, active
        │                             job) and OPERATOR (business: listing, story, tips,
        │                             booking requests, perks) — see migration
        │                             034_operator_accounts)
        └── src/pages/               auth, home (availability + nearby alerts),
                                      active job (live map + road route), business
                                      (govt-verified local-operator self-service dashboard)
```

</details>

---

## 🚀 Getting started

> **The source lives in a private repository, not this one.** This public repo is a curated
> evidence and documentation package for judge evaluation — real screenshots, real architecture
> docs, real testing records — not a source-code mirror. The steps below describe how the team
> itself runs the project locally; a judge evaluating this submission should use the **live
> deployed links** in [🌐 Live links](#-live-links) instead, which need no setup and are exactly
> what every fix and feature in this README has been verified against.

<details>
<summary><b>Local setup steps</b> (team reference) — click to expand</summary>

### Prerequisites
- Node.js ≥ 20
- PostgreSQL ≥ 15 (needs `pgcrypto` for `gen_random_uuid()` — the migration enables it)
- npm

### 1. Clone and install
```bash
git clone https://github.com/aryanf192811-eng/Aaraksha.git
cd Aaraksha/backend
npm install
```

### 2. Configure environment
```bash
cp .env.example .env
```
Fill in `DATABASE_URL` at minimum. `JWT_SECRET`, `GOVT_ID_SECRET`, and `GUARDIAN_SECRET` need
real random values even for local development. Twilio, Gemini, OpenWeatherMap, and Web Push
(VAPID) keys are **optional** — every integration degrades gracefully when unset.

### 3. Set up the database
```bash
npm run preflight     # verifies DATABASE_URL is reachable before anything else runs
npm run migrate       # applies the full 39-table schema
npm run seed          # idempotent demo data — safe to re-run
```
Or all three in one shot: `npm run setup`.

Two optional scripts add richer demo content on top of the base seed:
```bash
node scripts/seedDemoContent.js       # more trips, reviews, and scam reports per account
node scripts/seedAnalyticsHistory.js  # 30 days of realistic resolved-incident history
```

The Predictive Risk Model ships pre-trained (`src/data/riskModel.weights.json` is checked in), but
the training run is fully reproducible — `npm run train:risk-model` retrains it from scratch and
prints the full report (loss curve, accuracy, learned feature weights) to the console.

### 4. Run the backend
```bash
npm run dev            # nodemon, auto-restart
```
Starts on `PORT` (default `5000`), logs `GET /health → {"status":"ok"}` once ready.
Socket.IO and all four cron jobs start automatically.

### 5. Run the frontends
Each app is a separate Vite project on a fixed port. In four more terminals:
```bash
cd frontend/tourist   && cp .env.example .env && npm install && npm run dev   # → :5173
cd frontend/govt      && cp .env.example .env && npm install && npm run dev   # → :5174
cd frontend/guardian  && cp .env.example .env && npm install && npm run dev   # → :5175
cd frontend/volunteer && cp .env.example .env && npm install && npm run dev   # → :5176 (Aaraksha Sahayak)
```
The `.env.example` defaults work out of the box against a local backend. To test from another
device on the same network, point each `VITE_API_URL` / `VITE_SOCKET_URL` at your machine's LAN
IP instead of `localhost` (all four dev servers already bind to `0.0.0.0`). Road routing calls
the free public OSRM demo server directly from the browser — no API key, nothing to configure.

</details>

---

## 🌐 Live links

**Deployed (permanent — this is what anyone else testing the project should use):**

| App | URL |
|---|---|
| Tourist PWA | https://aaraksha-tourist.vercel.app |
| Government Command Center | https://aaraksha-govt.vercel.app |
| Aaraksha Sahayak (Rescuer / Local-Operator app) | https://aaraksha-rescuer.vercel.app |
| Guardian Portal | https://aaraksha-guardian.vercel.app |
| Backend API | https://aaraksha-backend-znb6.onrender.com |

These are the real, always-on links backed by Render + Vercel — they do not depend on any
machine being on, and are what every fix and feature in this README has been verified against.

**Temporary local tunnel (session-only, 2026-09-13 — for one demo recording, not a standing
link):** the same backend and all four frontends were also run locally and exposed via
Cloudflare quick tunnels, purely so the recording machine's own CPU/RAM could be used instead of
Render's free tier. These stop working the moment that local session ends — treat the deployed
links above as the real, durable ones.

| App | Temporary tunnel URL |
|---|---|
| Backend API | https://honey-volt-thirty-flood.trycloudflare.com |
| Tourist PWA | https://discussions-continuity-resident-unless.trycloudflare.com |
| Government Command Center | https://developer-ethics-tree-mumbai.trycloudflare.com |
| Aaraksha Sahayak | https://dogs-tile-calendars-tuition.trycloudflare.com |
| Guardian Portal | https://border-observed-donations-antarctica.trycloudflare.com |

This backend runs against a separate **local** database (seeded independently of production), so
not every account below exists on it — confirmed working here: govt Super Admin
(`admin@aaraksha.gov.in` / `Admin@123`), Priya Deka the volunteer (`9000055503` / `DemoPass123`),
and tourist Aryan Demo (`9999999999` / `Demo@123`, use this one instead of Meera Shah on these
tunnel links specifically — Meera Shah only exists in the production database).

---

## 🔑 Demo accounts

Seeded, mid-scenario accounts — not blank slates. SOS/DMS scenarios are one-time snapshots (may
already be resolved by the time you look); every flow is reproducible in under a minute, see
[`docs/testing/README.md`](./docs/testing/README.md). Meera Shah / Rajesh Solanki below is seeded
most recently and least likely to have been trampled.

| Account | Login | Scenario |
|---|---|---|
| Aryan Demo | `9999999999` / `Demo@123` | Active trip, 1 check-in, 1 resolved SOS |
| Priya Sharma | `9876500001` / `Demo@123` | Completed trip, passport-ready |
| Meera Shah | `9099911001` / `Demo@123` | Active trip (Assam) — pairs with rescuer Priya Deka for a live SOS→rescue walkthrough |
| Rahul Verma | `9876500002` / `Demo@123` | Re-trigger for a live unresolved-SOS scenario |
| Sneha Das | `9876500003` / `Demo@123` | Re-arm Dead Man's Switch from the Safety Center for a live scenario |
| Karan Mehta | `9000055501` / `DemoPass123` | SOS-assigned-to-volunteer scenario (Meera/Rajesh pairing is the more reliable live version) |

| Govt role | Login |
|---|---|
| Super Admin | `admin@aaraksha.gov.in` / `Admin@123` |
| District Admin | `district.officer@aaraksha.gov.in` / `District@123` |
| Police (E-FIR investigator) | `police.officer@aaraksha.gov.in` / `Police@123` — seeded with three E-FIR cases across the investigation ladder (Filed / Assigned / Under Investigation) |
| Checkpoint Officer | `checkpoint.officer@aaraksha.gov.in` / `Checkpoint@123` |

| Aaraksha Sahayak login | Scenario |
|---|---|
| Rajesh Solanki — `9099911002` / `7PSDH7CWE9MN` | Official rescue team account (Parul University Response Team, Vadodara) — pairs with Meera Shah above |
| Priya Deka — `9000055503` / `DemoPass123` | Verified citizen volunteer — assign her a fresh SOS to see the live-navigation screen |

The Guardian Portal needs no login — copy any tourist's guardian token (visible on their Profile
page) into `/track/:token` on the guardian app.

---

## 🔌 API surface

168 REST endpoints across 19 route groups, all under `/api`. Full contracts in
[API Reference](./docs/api/api-reference.md).

<details>
<summary><b>Every route group, what it covers</b> — click to expand</summary>

| Prefix | Covers |
|---|---|
| `/auth` | Tourist + govt registration/login, forgot-password OTP flow (with a visible in-app fallback if Twilio delivery fails), phone verification — govt registration is role-gated, no self-service SUPER\_ADMIN |
| `/tourists` | Profile, emergency-contact OTP verification, checkpoint QR code, public guardian view, DPDP data rights (privacy notice, data export, deletion request + history) |
| `/trips` | Itinerary CRUD, stops (incl. mark-visited status/spend), group trips (join/invite/members/leave), per-trip news, TSI, AI safety-advisory briefing |
| `/sos` | Create SOS, history, active rescue info, mark false alarm |
| `/dms` | Dead Man's Switch create/reset/status |
| `/ntn` | Simulated satellite (NTN) SOS uplink attempt — see [NTN](#-ntn--a-satellite-fallback-transport) |
| `/travel-planner` | Build My Journey, natural-language intake, ask-a-follow-up, commit, propose/apply trip adjustment, routes between two stops — see [AI Travel Assistant](#-ai-travel-assistant--plan-adjust-and-track-a-journey) |
| `/checkins` | Manual check-ins |
| `/destinations` | Catalog (incl. curated highlights), weather cache, risk overview, a real filterable/paginated cross-destination news feed, per-destination news, reviews, government-approved curated multi-day itineraries by region |
| `/local-operators` | Tourist-facing reviews for a verified local operator (get/create) — the Trust Economy loop, awards "Vocal for Local" points, see [Local Tourism Providers](#-local-tourism-providers--the-tourism-industry-pillar) |
| `/scam-reports` | Community-reported safety incidents, 90-day hotspot summary |
| `/incidents` | Tourist-facing E-FIR filing and status tracking (`POST /`, `GET /me`, `GET /:id`) |
| `/packing` | AI-generated packing checklists |
| `/journey-passport` | PDF trip summary generation **plus a standalone `GET /:tripId/hash`** — recomputes the Journey Integrity Hash chain live, independent of the PDF |
| `/govt` | Dashboard, live tourists, risk overview (with coordinates for the map's risk-density layer, and each destination's Predictive Risk Model score) **plus `GET /risk-model/info` for the model's training report**, open safety anomalies + resolve, SOS assignment/resolution to a team *or* volunteer, nearby-rescuer search, resolved-incident PDF report, rescue teams, E-FIR queue (list/assign/status-update/PDF/officers), volunteer provisioning/verification/roster, local-operator account creation for a verified business, local-operator itinerary-impression analytics (which verified providers real committed trips actually surfaced), checkpoint scan, analytics + PDF export, destination news posting |
| `/volunteers` | Volunteer register/login (`account_type: RESCUER`), status + live location updates, active-assignment lookup, EN\_ROUTE/ARRIVED self-status — plus a rescuer's own "I'm responding" now creates the real assignment (first-responder-wins) instead of only a broadcast record; `/volunteers/me/business*` (`account_type: OPERATOR`) for a verified provider to view/update their own listing and reviews |
| `/webhooks` | Twilio inbound SMS (offline SOS) |
| `/push` | Web push subscribe/unsubscribe, VAPID public key |
| `/help` | In-app Help & FAQ chatbot — answers grounded in the app's real nav-guide/FAQ content, Gemini-backed with a zero-AI keyword-match fallback |

</details>

---

## ✅ Testing

**87 backend + 95 frontend vitest tests · 157 Postman requests / 345 assertions · 6-query scoring
benchmark · 12-phase live Playwright QA.** CI runs the backend suite against a real ephemeral
Postgres and matrixes the frontend suite across all four apps on every push.

<details>
<summary><b>Commands and what each layer covers</b> — click to expand</summary>

**Unit + integration (vitest)**
```bash
cd backend && npm test   # 87 tests, 8 files — TSI scoring, crypto, expense settlement, integration flows
cd frontend/<app> && npm test   # 95 tests total across tourist/govt/guardian/volunteer
```

**API contract tests (Postman/Newman)**
```bash
cd backend
npx newman run postman/aaraksha-collection.json -e postman/aaraksha-environment.json
```
157 requests, 345 assertions, 30 folders — auth, trips, SOS, DMS, govt ops, security guards,
validation, edge cases, the full unified-rescuer flow. Newer endpoints (community, group trips,
push, incidents, anomaly detection, E-FIR, checkpoint hash-chain, AI Travel Assistant) are instead
verified through live Playwright end-to-end testing — real logins, real DB rows confirmed, real
PDF output checked with `pdftotext`, a real checkpoint scan confirmed to change `finalHash`.

**Scoring-quality benchmark**
```bash
cd backend && node tests/eval/travelPlanner.benchmark.js   # needs a running backend + real dev DB
```
6 fixed real queries (different cities/budgets/interests/states, one deliberately unseeded region
to confirm a clean `422`) assert on sane scorer output — the "right answer" depends on whatever's
actually seeded, so this can't be a fixed unit-test fixture.

</details>

---

## 🛡️ Production readiness

**8 real defects found and fixed** across two adversarial passes (real payloads at a live server,
not code review) — rate-limit bypass, SQL injection attempts (held), a concurrency race on SOS
resolution, transaction rollback, graceful degradation when Twilio/Gemini/OpenWeatherMap are
unconfigured, an unauthenticated `SUPER_ADMIN`-creation path, JWT `alg:none` confusion, and an OTP
rate limiter ignoring its own config. Full write-up: [`docs/testing/README.md`](./docs/testing/README.md)
· [`09-security-audit.md`](./docs/testing/09-security-audit.md).

<details>
<summary><b>Each defect, in detail</b> — click to expand</summary>

- **Rate limiting** — burst traffic against `/login`; found the limiter was defined but never
  wired to a route, then found a second bug (a shared limiter instance draining budget across
  unrelated routes). Both fixed.
- **SQL injection** — `' OR 1=1 --`, `DROP TABLE`, `UNION SELECT` against login/search/profile
  fields. Held — parameterized queries throughout.
- **Concurrency** — two parallel resolve requests on the same SOS both returned 200 before the
  fix, silently clobbering each other's resolution notes. Fixed with an atomic DB-level guard.
- **Transaction rollback** — deliberately forced a mid-transaction foreign-key violation;
  confirmed the preceding insert did not survive the rollback.
- **External service failure** — Twilio, Gemini, and OpenWeatherMap all unconfigured; confirmed
  every integration degrades gracefully rather than failing the request.
- **Malformed input** — a SQLi-shaped string in a phone field crashed with an unhandled 500
  before the fix; now a clean 400.
- **Unauthenticated privilege escalation** — `POST /auth/govt/register` let anyone create a
  `SUPER_ADMIN` account with no auth at all. Now gated behind `authenticateGovt` +
  `requireGovtRole(SUPER_ADMIN)`, and the endpoint no longer hands the caller a session token for
  the account it just created.
- **JWT algorithm confusion** — every `jwt.verify()` call across auth middleware, Socket.IO auth,
  and checkpoint-token verification now pins `algorithms: ['HS256']` explicitly, closing the
  classic "attacker picks `alg: none`" class of attack.
- **OTP rate limiter ignoring its own config** — the OTP-specific limiter had a second, hardcoded
  15-minute/3-request budget completely independent of the configurable window used everywhere
  else. Now reads the same configurable values, plus a new `debugOtp` fallback that surfaces the
  OTP directly in the UI (dev-only) when Twilio can't deliver it.

</details>

---

## ⚖️ Legal & Compliance

**DPDP Act 2023 · GIGW 3.0 / WCAG 2.1 AA · Verhoeff-validated Aadhaar** — real regulatory
requirements, not slide bullets, since this platform handles government ID numbers and runs a
public-sector command center.

<details>
<summary><b>The details</b> — click to expand</summary>

**DPDP Act 2023** (India's Digital Personal Data Protection Act, in force since 13 November 2025)
governs every tourist record this platform holds. The tourist app's **Privacy & Data Rights page**
gives each of its statutory rights a real, working control:

| Right | What it does here |
|---|---|
| Right to notice | A plain-language breakdown of exactly what's collected, per category, and why |
| Right to access | **Export My Data** — a real file download of every trip, check-in, SOS event, E-FIR, and checkpoint scan tied to the account |
| Right to correction | Edit your own profile at any time |
| Right to erasure | **Delete My Account** — anonymizes the row in place (name, phone, blood group, medical notes, and the government-ID hash and suffix are all scrubbed, `is_active` set false) rather than a raw `DELETE`, so legally-retainable audit records (resolved SOS history, closed E-FIRs) survive without still identifying the person. Automatically **refused** while an open SOS or E-FIR exists, with the reason stated back to the requester |
| Right to grievance redressal | A named contact point on the same page |

The government ID hash itself gets the same treatment on deletion: a bare SHA-256 of a 12-digit
number is brute-forceable in hours, so "anonymizing" a row without also replacing that hash would
leave a supposedly-deleted account re-identifiable to anyone with database access. It's replaced,
not left behind.

**GIGW 3.0** (Guidelines for Indian Government Websites) mandates WCAG 2.1 Level AA for government
portals — directly applicable to the Govt Command Center, which is exactly that. An accessibility
pass covers icon-only controls (`aria-label`), keyboard focus visibility, text-contrast tokens that
were failing AA's 4.5:1 minimum, modal keyboard handling (Escape to close, focus-on-open), image
alt text, and form labeling across every govt screen.

**Aadhaar validation** goes one level past format checking: registration runs the real **Verhoeff
checksum algorithm** — the actual arithmetic UIDAI uses to generate an Aadhaar number's 12th digit
— against the submitted number. This is honestly scoped: it catches a mistyped digit the way the
real system would, but it is *not* live UIDAI eKYC verification, and nothing in the product claims
otherwise.

</details>

---

## 📚 Documentation map

| Document | Read it when |
|---|---|
| [Architecture](./docs/architecture/architecture.md) | You're making a stack, naming, or directory-structure decision |
| [API Reference](./docs/api/api-reference.md) | You're calling or adding an endpoint |
| [Database Schema](./docs/architecture/database-schema.md) | You're writing a query or touching the schema |
| [Design System](./docs/design-system.md) | You want the real design tokens (color, type, spacing) behind all four frontends |
| [Data Curation](./docs/data-curation.md) | You want the sourcing/verification discipline behind the curated destinations, routes, and local providers |
| [`system-architecture.svg`](./docs/architecture/system-architecture.svg) | You want the architecture diagram |
| [Testing evidence](./docs/testing/README.md) | You want the adversarial-testing record — 12 phase reports covering every portal, the backend, security, real-time consistency, and a full regression pass |
| [Full documentation index](./docs/README.md) | You want everything — portals, safety/resilience, AI systems, deployment, and more |

---

## 🛤️ Roadmap

Everything in this README is live on the deployed backend, not stubbed for demo — verified in a
[12-phase adversarial QA pass](./docs/testing/README.md) plus a full Postman/Newman contract regression.

<details>
<summary><b>What's next</b> — click to expand</summary>

- [ ] **Official rescue team login + live GPS** — teams are dispatched/tracked through the unified
      rescuer pool but don't yet have their own standalone session the way volunteers do
- [ ] **Guardian ↔ Rescuer messaging** — deliberately out of scope today; an anonymous link-holder
      messaging a rescuer is a different trust boundary, worth its own design pass
- [x] ~~Provider relevance as a scoring signal~~ — **shipped**, see [AI Travel Assistant](#-ai-travel-assistant--plan-adjust-and-track-a-journey)
- [x] ~~Provider enquiry/lead analytics~~ — **shipped**, see [Local Tourism Providers](#-local-tourism-providers--the-tourism-industry-pillar)
- [x] ~~More than one curated itinerary per state~~ — **shipped**, 16 routes now; still only 3 of 8
      states carry a real government citation — a real search came up empty rather than guessed
      (see [Data Curation](./docs/data-curation.md))

</details>

---

*Built for Smart India Hackathon 2026 — Student Innovation category, Travel & Tourism theme.*
