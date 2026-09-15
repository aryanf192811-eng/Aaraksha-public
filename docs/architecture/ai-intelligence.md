# AI & Intelligence — Aaraksha

## Design Philosophy

> AI is the narrator, not the judge.

All safety-critical decisions in Aaraksha are made by deterministic, auditable code.
Gemini handles only tasks where hallucination has no safety consequence: prose narration,
intent extraction, packing suggestions, and chatbot responses.

---

## What Uses AI (Gemini API)

### 1. Trip Planner — Intent Extraction

When a tourist types a natural language prompt ("7-day solo trek to Meghalaya, I love waterfalls"),
Gemini extracts structured intent:

```json
{
  "destinations": ["Meghalaya", "Arunachal Pradesh"],
  "interests": ["NATURE", "ADVENTURE"],
  "budget_inr": 15000,
  "duration_days": 7,
  "travel_style": "SOLO",
  "transport_pref": "TRAIN"
}
```

This extracted intent is passed to the **deterministic scorer** — Gemini does not choose
the destinations or rank them.

### 2. Trip Planner — Journey Narrative

After the deterministic scorer ranks and orders stops, Gemini writes prose:

> "Your journey begins in Guwahati, the gateway to Northeast India.
> On Day 1, board the Howrah-Kamakhya Vande Bharat for ₹475 (sleeper)...
> Cherrapunji awaits on Day 3 — the living root bridges of Nongriat require
> a 2-hour descent but reward you with a UNESCO-candidate sight..."

The narrative describes a plan whose route, cost, and order were already determined by code.

### 3. Packing List Generator

Gemini generates a personalized packing checklist based on trip parameters:
- Weather at each stop
- Altitude (>3000m → Diamox, layering)
- Zone type (RESTRICTED → ILP docs, registration forms)
- Travel type (SOLO → personal safety items)

**Static fallback:** If `GEMINI_API_KEY` is not configured, a curated static packing list
is returned. The feature is always available.

### 4. Help Chatbot

The in-app Help chatbot uses Gemini grounded in live data:
- Real destination data from the DB
- Verified local operators
- Current curated itineraries
- Destination news

The chatbot also answers judge/evaluator questions about the platform architecture.

### 5. Trip Adjustment via Follow-up Prompts

A tourist can refine their plan:
- "Make it more adventurous" → Gemini extracts intent delta → scorer re-ranks
- "Add Ziro to the itinerary" → destination added, scorer re-orders
- "Reduce budget by ₹5,000" → constraint tightened, scorer eliminates expensive options

The adjustment flow uses `extractTripIntent()` to identify what changed, then
applies those changes deterministically.

---

## What Does NOT Use AI (Deterministic Systems)

### TSI (Travel Safety Index) — `tsi.service.js`

100% rule-based JavaScript. Every factor has an explicit, auditable penalty table:

```js
const CONNECTIVITY_PENALTY = { NONE: 20, POOR: 10, MODERATE: 4, GOOD: 0, EXCELLENT: 0 }
const DIFFICULTY_PENALTY   = { EASY: 0, MODERATE: 5, HARD: 15, EXTREME: 25 }
const ZONE_PENALTY         = { SAFE: 0, CAUTION: 5, ILP_REQUIRED: 10, HIGH_RISK: 20, RESTRICTED: 25 }
const WEATHER_PENALTY      = { CLEAR: 0, FOG: 5, RAIN: 5, HEAVY_RAIN: 15, SNOW: 10, STORM: 20 }
```

A judge can trace exactly why a Tawang winter trek scores 42 (High Risk) and a Shillong day
trip scores 87 (Low Risk). No model weights, no unexplainable outputs.

### Dead Man's Switch — `cron/index.js`

Pure node-cron + SQL. Fires at the computed `next_trigger_at` column value.

### SOS Pipeline — `sos.service.js`

Database write → Socket.IO event → SMS dispatch. No AI involvement.

### Rescue Assignment — `rescueAssignment.service.js`

Govt officer selects the team. The system records the assignment and dispatches.
No auto-assignment, no ML-based routing.

### Itinerary Scoring — `travelScoring.service.js`

Deterministic JS scoring on multiple dimensions:
- Interest tag match (ADVENTURE, CULTURE, PILGRIMAGE, NATURE, WILDLIFE)
- Cost per day against budget
- Haversine distance between stops (minimize backtracking)
- Altitude progression (gradual ascent recommended for high-altitude routes)
- Difficulty match to travel type

---

## Gemini Integration Technical Details

### Why Direct REST, Not the SDK

```
// Measured comparison (same model, same prompt, same key):
SDK (model.generateContent()):   59 seconds
Direct REST to generativelanguage.googleapis.com: 1.2 seconds (local)

// Root cause:
// The SDK predates gemini-3.5-flash-lite's response shape (thoughtSignature field)
// and stalls on response parsing. Direct REST bypasses the SDK entirely.
```

### Timeout Strategy

```js
const GEMINI_TIMEOUT_MS = 30000 // 30 seconds
// From Render (not local): 15–22s measured for the same REST call
// 30s covers Render's outbound path to generativelanguage.googleapis.com with margin

const controller = new AbortController()
const timer = setTimeout(() => controller.abort(), GEMINI_TIMEOUT_MS)
// AbortController cancels the fetch if Gemini doesn't respond in time
```

### Model

`gemini-3.5-flash-lite` — fast, cost-effective for structured extraction and short narrations.

### Prompt Structure

All Gemini prompts follow this pattern:
1. System context (role, constraints, output format)
2. Real data context (destination list, scoring results, weather)
3. User input
4. Explicit JSON output schema (for structured extraction)

---

## Tourism Discovery Algorithm (travelScoring.service.js)

### Interest Tags

```js
const INTEREST_TAGS = {
  ADVENTURE:   ['HARD', 'EXTREME'],           // difficulty
  NATURE:      ['FOREST', 'REMOTE'],          // zone_type
  CULTURE:     ['URBAN', 'RURAL'],            // zone_type
  PILGRIMAGE:  ['PILGRIMAGE'],               // destination_type
  WILDLIFE:    ['FOREST'],                   // zone_type
}
```

### Scoring Dimensions per Candidate

1. **Interest match score:** how many of the destination's tags match the tourist's interests
2. **Cost fit:** daily cost vs. budget per day (penalty for over/under budget)
3. **Routing efficiency:** Haversine distances between selected stops (minimize total km)
4. **Safety fit:** TSI score of the stop (penalizes extreme-risk stops for non-adventure travelers)
5. **Altitude progression:** penalizes rapid altitude gain (>1,500m jump between consecutive stops)

### Final Output

Scored + ranked stops → passed to Gemini for narrative → returned to tourist with:
- Day-by-day itinerary
- Per-stop cost estimates
- Transport mode between stops (TRAIN/FLIGHT/BUS)
- TSI score per stop
- Rescuer Readiness checklist pre-filled

---

## Benchmark Evidence

`backend/tests/eval/travelPlanner.benchmark.js` runs 6 fixed real-world queries
against the live scorer + dev database and asserts expected score ranges:

| Query | Expected Score Range |
|-------|---------------------|
| Solo ADVENTURE trek, Meghalaya 7 days | 55–75 (Moderate Risk) |
| Family NATURE trip, Sikkim 5 days | 65–85 (Low–Moderate) |
| PILGRIMAGE, Manipur + Assam 10 days | 60–80 |
| ADVENTURE solo, Arunachal winter | 40–60 (High Risk) |
| CULTURE day trip, Guwahati | 75–95 (Low Risk) |
| Mixed group trip, all 8 states 14 days | 45–65 (High–Moderate) |

All 6/6 passing.
