# Portal Documentation — All Four Portals

## Portal Matrix

| Portal | Path | Theme | Audience | Deployment |
|--------|------|-------|----------|------------|
| Tourist PWA | `frontend/tourist/` | White + Amber, mobile-first | Tourists | aaraksha-tourist.vercel.app |
| Govt Command Center | `frontend/govt/` | Emerald-50, desktop-first | District Officers, Rescue Coordinators | aaraksha-govt.vercel.app |
| Guardian Portal | `frontend/guardian/` | White, status-focused, public | Family & friends | aaraksha-guardian.vercel.app |
| Aaraksha Sahayak | `frontend/volunteer/` | White + Teal, mobile-first | Verified volunteers, official rescue teams, govt-verified local businesses | aaraksha-rescuer.vercel.app |

---

## 1. Tourist PWA

### Design Philosophy
Mobile-first (375px breakpoint primary), premium amber aesthetic, installable as PWA.
Modeled as a travel companion — not a safety-only tool — to encourage habitual use before
an emergency occurs.

### Key Pages and Features

#### Landing Page
- Marketing/onboarding page with animated hero
- NER destination showcase
- Sign up / sign in CTAs

#### Dashboard
- TSI score badge with color coding (green/yellow/orange/red)
- Active trip card with DMS status
- Quick action row: SOS, Check-in, Checkpoint, Safety
- FAB (Floating Action Button) for rapid SOS
- Push notification permission prompt

#### AI Trip Planner Flow
1. `CreateTripPage` — natural language prompt or structured form
2. Gemini extracts intent (destinations, interests, budget, duration, travel style)
3. `travelScoring.service.js` deterministically scores + ranks candidates
4. Gemini writes prose narrative around the scored plan
5. `TripDetailPage` — view, edit, accept
6. Follow-up prompts: "make it more adventurous", "add Ziro", "reduce budget by 20%"

#### Safety Hub (`SOSPage`)
- Big red SOS button — one tap, GPS auto-attached
- 5 categories: MEDICAL / LOST / TRAPPED / DISASTER / OTHER
- Offline fallback: "No internet? Send SMS" with pre-filled SMS URI
- DMS card: enable, set interval, view countdown
- Recent SOS history

#### Check-in (`CheckinPage`)
- GPS auto-populated
- Battery percentage captured
- Optional note
- Resets DMS timer if active

#### Destinations
- Grid of 30 NER destinations with TSI badge
- Detail page: photos, reviews, scam reports, destination news, local operators, TSI factors

#### Community
- Community feed: scam reports, incident alerts, destination reviews
- Write review, file incident report

#### Guardian Link
- Tourist sets 4-digit PIN
- Generates shareable URL: `aaraksha-guardian.vercel.app/{token}`
- Family can view live tracking after PIN verification

#### Profile
- Edit personal info, blood group, emergency contacts
- Data rights: export data, request deletion (DPDP Act 2023)
- Push notification settings

### Offline Strategy
- Vite PWA plugin + service worker: caches app shell
- Dexie.js (IndexedDB): pending check-ins, SOS queue
- `useOfflineSync` hook: flushes pending actions on connectivity restore
- SMS fallback SOS: works with zero internet

---

## 2. Government Command Center

### Design Philosophy
Desktop-first (1440px primary), dense data layout, dark emerald theme.
Designed for sustained, high-focus use during operational hours — not occasional browsing.

### Key Pages

#### Dashboard (`DashboardPage`)
- Live stat cards: active SOS count, tourists online, rescue teams deployed
- Recent SOS activity feed with Socket.IO updates
- Quick navigation to all modules
- Recharts: SOS trend (7 days), district risk bar chart

#### Live Ops Map (`LiveMapPage`)
- Leaflet (2D) + MapLibre GL (3D toggle)
- Real-time SOS pins: animate-bounce on arrival, animate-pulse when active
- Rescue team positions
- Tourist cluster markers
- Click SOS pin → open triage panel inline

#### SOS Management (`SOSManagementPage`)
- Full triage queue: active → resolved → false alarm tabs
- Each SOS: tourist profile, blood group, govt ID suffix, GPS coords, destination, hospital distance
- Assign rescue team (dropdown of available teams by district)
- Assign verified volunteer (optional)
- In-app chat with tourist / rescuer
- Mark resolved / mark false alarm
- Audit trail (assigned_by, resolved_by, timestamps)

#### Risk Overview (`RiskOverviewPage`)
- District-level risk heatmap
- Anomaly flags: cluster anomalies, frequency spikes
- Per-district statistics: SOS count, avg resolution time, active tourists

#### Volunteers Page (`VolunteersPage`)
- Pending verification queue
- Verify / reject volunteers
- View volunteer details: district, govt ID suffix, availability status

#### Local Operators Page (`LocalOperatorsPage`)
- Pending verification queue for tourism providers
- Category filter: HOTEL / HOMESTAY / GUIDE / EXPERIENCE / ARTISAN
- Verify / reject with operator details
- Verified operators immediately visible in tourist app

#### Analytics (`AnalyticsPage`)
- Monthly SOS trends
- Category breakdown (MEDICAL / LOST / TRAPPED / etc.)
- Resolution time distribution
- Top districts by risk

#### Incident Queue (`IncidentQueuePage`)
- Tourist-filed incident reports
- Review, categorize, escalate to E-FIR

#### Checkpoint Scan (`CheckpointScanPage`)
- Verify tourist checkpoint scan QR codes
- Hash-chain integrity check

#### Trust Appeals (`TrustAppealsPage`)
- Review tourist appeals against trust score reductions
- Approve or reject appeals

### Auth and RBAC
- Three roles enforced server-side:
  - `ADMIN`: full access including govt user management
  - `DISTRICT_OFFICER`: own district SOS, rescue, local ops
  - `RESCUE_COORDINATOR`: rescue assignments and volunteer management
- `requireGovtRole()` middleware gates each route group

---

## 3. Guardian Portal

### Design Philosophy
Zero-login, public-facing, optimized for a worried family member checking in on a phone.
PIN-gated to prevent random URL guessing (UUID tokens + 4-digit PIN = two-factor-ish).

### Features
- PIN prompt on first visit (session-persisted after correct entry)
- Live Leaflet map: tourist's last GPS location with accuracy radius
- Battery percentage indicator
- DMS status (active / inactive / triggered)
- Check-in timeline: reverse-chronological list with GPS coords, notes, battery
- SOS alert banner: shown prominently if tourist has an active SOS
  - Category, timestamp, rescue assignment status
- Socket.IO: `CHECKIN_UPDATE` events push in real-time to `guardian-{token}` room
- Multilingual: i18n structure (English primary, regional language hooks)

---

## 4. Aaraksha Sahayak

### Design Philosophy
Mobile-first, delivery-partner app UX (modeled on Zomato/Swiggy/Rapido for familiarity
with Indian volunteer responders). Map-first, persistent contact actions, a real "start"
moment for navigation.

### Key Pages

#### AuthPage
- Register with: full name, phone, password, govt ID type + number, district, state
- Self-registration flow; account is immediately inactive until govt verifies
- Login returns JWT with `role: volunteer`

#### HomePage
- Big status toggle: AVAILABLE / OFFLINE (teal/grey)
- Live alert cards: incoming dispatch offers from govt
  - Accept → transitions to ActiveJobPage
  - Decline → case returns to pool
- Points balance + reputation badge
- Recent completed cases

#### ActiveJobPage (the core screen)
- MapLibre GL: live map showing SOS location pin + route
- OSRM routing: real road route from rescuer's current location to SOS site
- Tourist info panel: name, blood group, category, message
- Real-time chat thread with tourist
- "I'm here" button → triggers handoff flow / completion
- Live rescuer location streamed back to govt dashboard via Socket.IO
- `fitBounds` on route load (bug fixed in Phase 6 QA)

#### OperatorDashboardPage
- Local operators log in here to:
  - View verification status
  - See their reviews and rating
  - Update business description

### Volunteer Dispatch Flow
```
Govt assigns volunteer → Socket.IO alert to rescuer
Rescuer accepts → status = EN_ROUTE
Rescuer starts navigation → OSRM route computed
Govt sees rescuer's live GPS on dashboard
Rescuer arrives → clicks "I'm here"
Govt confirms resolution → COMPLETED
Volunteer: +25 points
```
