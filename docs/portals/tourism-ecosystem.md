# Tourism & Local Operator Ecosystem — Aaraksha

## Why This Matters for PS 26204

The problem statement explicitly asks for "information services including hotels, travel and others."
Aaraksha implements a full verified local operator discovery layer — not just a list of businesses,
but a trust-gated ecosystem with govt verification, tourist reviews, and operator accounts.

---

## The Local Operator Pipeline

### Phase 1: Data Curation (Backend)

Operators are seeded through a careful curation process:
- Every operator row requires a mandatory `source` field (citation, not optional)
- The schema enforces this: `source TEXT NOT NULL`
- No unsourced operator can be inserted — this prevents plausible-looking fabricated entries

### Phase 2: Govt Verification

```
Operator data seeded with source citation
        ↓
Govt officer opens LocalOperatorsPage in Command Center
        ↓
Reviews: business name, category, destination, contact, description, source citation
        ↓
Clicks VERIFY:
  UPDATE local_operators SET
    is_verified = true,
    verified_by = {govtUserId},
    verified_at = NOW()
  WHERE id = $1
```

### Phase 3: Tourist Discovery

```
Tourist opens trip planner or destination detail
        ↓
Backend fetches verified operators:
  SELECT * FROM local_operators
  WHERE destination_id = $1
    AND is_verified = true
    AND is_active = true
  ORDER BY created_at DESC
        ↓
Operators appear in trip planner with:
  - Business name + category badge
  - Average rating (from local_operator_reviews)
  - Contact phone
  - Description
  - Price range
```

### Phase 4: Tourist Reviews & Points

```
Tourist uses/interacts with an operator
        ↓
Files review: 1–5 stars + text comment
        ↓
Review stored in local_operator_reviews
        ↓
Tourist earns points (tourist_local_points)
        ↓
Average rating updates on operator card
```

---

## Operator Categories

| Category | Description | Seeded Examples |
|----------|-------------|-----------------|
| HOTEL | Registered accommodation | Heritage hotels in Shillong, eco-resorts in Kaziranga |
| HOMESTAY | Family homestay operators | Root bridge area homestays in Cherrapunji |
| GUIDE | Licensed trek guides | Registered guides for Dzukou Valley, Tawang treks |
| EXPERIENCE | Cultural / immersion activities | Weaving workshops in Nagaland, cooking classes |
| ARTISAN | Handicraft workshops | Bamboo craft workshops, traditional textile |

---

## Government Verification UI (LocalOperatorsPage)

The verification queue in the Govt Command Center:

```
┌─────────────────────────────────────────────────────────────────┐
│  LOCAL OPERATORS — Verification Queue             Pending: 3   │
├─────────────────────────────────────────────────────────────────┤
│ 🏠 Tawang Mountain Homestay        [HOMESTAY] Tawang, Arunachal │
│    Contact: +91 9876543210                                       │
│    Source: TripAdvisor listing + district tourism dept register  │
│    Rating: No reviews yet                                        │
│    [VERIFY] [REJECT]                                             │
├─────────────────────────────────────────────────────────────────┤
│ 🏔️  Snow Leopard Trek Guide         [GUIDE]    Tawang, Arunachal │
│    Contact: +91 9876543211                                       │
│    Source: State tourism board licensed guide database 2025      │
│    Rating: ★4.7 (12 reviews)                                     │
│    [VERIFY] [REJECT]                                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Operator Account (OperatorDashboardPage)

Local operators can log in to the Rescuer App's operator dashboard to:
- View their verification status
- See their average rating and reviews
- Update their business description
- View how many tourists have viewed their listing

This gives operators a feedback loop and stake in the ecosystem.

---

## Curated Itineraries (New in Migration 032)

Beyond AI-generated plans, Aaraksha includes **curated itineraries** — pre-built,
expert-reviewed routes for common Northeast India trip types:

| Type | Examples |
|------|---------|
| Living Roots Circuit | Shillong → Cherrapunji → Nongriat → Dawki |
| High Altitude Sikkim | Gangtok → Lachung → Gurudongmar Lake |
| Nagaland Cultural | Dimapur → Kohima → Dzukou Valley |
| Assam Wildlife | Guwahati → Kaziranga → Majuli Island |

Curated itineraries are seeded with real sourced data and filtered by interest tags.

---

## Destination News Feed (Migration 005)

Each destination has a news feed (`destination_news` table):
- Trail closure advisories
- Weather warnings (beyond TSI)
- Local events
- Safety advisories from district authorities

Tourists subscribe to destinations and receive push notifications on new news.

---

## Typical Routes (Migration 025)

`typical_routes` table stores sourced inter-destination route data:

```
source: "IRCTC booking + State Tourism website (verified 2026-01)"
from: Guwahati
to: Shillong
mode: BUS
duration_minutes: 210
cost_min_inr: 100
cost_max_inr: 450
```

Every route has a `source` citation — same provenance discipline as local operators.
These routes power the itinerary planner's transportation cost estimates.

---

## Tourist Points System (Migration 030)

`tourist_local_points` table tracks points from local ecosystem engagement:

| Action | Points |
|--------|--------|
| Review a local operator | 5 pts |
| Verified check-in at destination | 2 pts |
| Accepted incident report | 10 pts |
| Trip completion (with DMS active) | 15 pts |

Points are displayed on the tourist profile and encourage repeated app engagement.

---

## Scam Reporting (Community Safety)

`scam_reports` table:

| Category | Description |
|----------|-------------|
| OVERCHARGING | Prices significantly above published rates |
| FAKE_GUIDE | Unregistered or impersonating licensed guides |
| THEFT | Reported theft incident |
| OTHER | Other tourist-affecting scam |

Scam reports are:
1. Attributed to a destination (not an operator — protection against false targeting)
2. Visible to other tourists in the destination detail page
3. Reviewed by govt officers in the incident queue

This creates a community-driven safety layer on top of the govt verification system.
