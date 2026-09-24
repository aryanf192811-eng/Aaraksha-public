# API Reference — Aaraksha Backend

**Base URL:** `https://{render-backend}.onrender.com/api`  
**Endpoints:** 168 total across 19 route groups — the core flows below cover the routes most
relevant to tracing how a feature works end-to-end; the full route list lives in the private
source repo's `backend/src/routes/`.
**Auth:** `Authorization: Bearer <jwt>` (tourist or govt JWT, depending on route)

---

## Authentication Routes (`/auth`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/auth/register` | None | Register tourist with phone, email, password, govt ID |
| POST | `/auth/login` | None | Login with phone/email + password |
| POST | `/auth/otp/send` | Tourist | Send OTP to tourist phone |
| POST | `/auth/otp/verify` | Tourist | Verify OTP |
| POST | `/auth/govt/login` | None | Govt officer login |
| POST | `/auth/govt/register` | Govt (SUPER_ADMIN) | Create govt user account |
| POST | `/auth/volunteer/login` | None | Volunteer login |

---

## Tourist Routes (`/tourists`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/tourists/me` | Tourist | Get own profile |
| PATCH | `/tourists/me` | Tourist | Update profile |
| GET | `/tourists/me/export` | Tourist | Export all personal data (DPDP) |
| POST | `/tourists/me/delete-request` | Tourist | Request account deletion |
| GET | `/tourists/me/trust` | Tourist | Get trust score + events |
| POST | `/tourists/me/trust/appeal` | Tourist | File trust appeal |
| GET | `/tourists/:id/guardian` | Token | Guardian data (no auth, token in URL) |

---

## Trip Routes (`/trips`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/trips` | Tourist | List own trips |
| POST | `/trips` | Tourist | Create trip |
| GET | `/trips/:id` | Tourist | Get single trip |
| PATCH | `/trips/:id` | Tourist | Update trip fields |
| DELETE | `/trips/:id` | Tourist | Cancel trip |
| GET | `/trips/:id/tsi` | Tourist | Get TSI score for trip |
| GET | `/trips/:id/members` | Tourist (owner or member) | Group roster |
| POST | `/trips/:id/invite` | Tourist (owner) | Generate/fetch the trip's invite code |
| POST | `/trips/join` | Tourist | Join a group trip by invite code |
| DELETE | `/trips/:id/leave` | Tourist (member) | Leave a group trip |
| POST | `/trips/:id/expenses` | Tourist (owner or member) | Log a shared expense, optionally split among a subset of the group |
| GET | `/trips/:id/expenses` | Tourist (owner or member) | List a trip's raw expense rows |
| GET | `/trips/:id/expenses/settlement` | Tourist (owner or member) | Computed net balances + minimal "who owes whom" settle-up transactions |
| DELETE | `/trips/:id/expenses/:expenseId` | Tourist (who logged it) | Remove an expense |

---

## SOS Routes (`/sos`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/sos` | Tourist | Trigger SOS (GPS + category required) |
| GET | `/sos` | Tourist | List own SOS history |
| GET | `/sos/:id` | Tourist | Get SOS detail |
| PATCH | `/sos/:id/resolve` | Tourist | Mark own SOS resolved |
| PATCH | `/sos/:id/false-alarm` | Tourist | Mark own SOS false alarm |

---

## Dead Man's Switch Routes (`/dms`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/dms` | Tourist | Create DMS for active trip |
| GET | `/dms` | Tourist | List own DMS records |
| PATCH | `/dms/:id/checkin` | Tourist | Reset DMS via check-in |
| PATCH | `/dms/:id/pause` | Tourist | Pause DMS |
| PATCH | `/dms/:id/cancel` | Tourist | Cancel DMS |

---

## Check-in Routes (`/checkins`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/checkins` | Tourist | Submit check-in (GPS + battery) |
| GET | `/checkins` | Tourist | List own check-ins |

---

## Destination Routes (`/destinations`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/destinations` | Tourist | List all active destinations |
| GET | `/destinations/:id` | Tourist | Get destination detail + operators + reviews + news |
| GET | `/destinations/:id/tsi` | Tourist | TSI score for this destination |
| GET | `/destinations/:id/news` | Tourist | News feed for destination |
| POST | `/destinations/:id/reviews` | Tourist | Post review |

---

## Local Operator Routes (`/local-operators`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/local-operators` | Tourist | List verified operators (filterable by destination, category) |
| GET | `/local-operators/:id` | Tourist | Operator detail + reviews |
| POST | `/local-operators/:id/reviews` | Tourist | Review an operator |

---

## Travel Planner Routes (`/travel-planner`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/travel-planner/plan` | Tourist | Generate AI + scored itinerary from prompt |
| POST | `/travel-planner/adjust` | Tourist | Adjust existing plan via follow-up prompt |
| GET | `/travel-planner/curated` | Tourist | List curated itineraries |
| GET | `/travel-planner/curated/:id` | Tourist | Get curated itinerary detail |

---

## SOS Management — Government Routes (`/govt`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/govt/sos` | Govt | All active SOS events |
| GET | `/govt/sos/:id` | Govt | SOS detail with full tourist + rescue context |
| PATCH | `/govt/sos/:id/resolve` | Govt | Resolve SOS |
| PATCH | `/govt/sos/:id/false-alarm` | Govt | Mark false alarm |
| POST | `/govt/rescue-assignments` | Govt (RESCUE_COORD) | Assign rescue team to SOS |
| GET | `/govt/rescue-teams` | Govt | List rescue teams + status |
| POST | `/govt/rescue-teams` | Govt (ADMIN) | Create rescue team |
| PATCH | `/govt/rescue-teams/:id` | Govt | Update team status |
| GET | `/govt/risk-overview` | Govt | District risk stats + anomaly flags |
| GET | `/govt/analytics` | Govt | SOS trends, resolution times |
| GET | `/govt/tourists` | Govt | Tourist listing with active trip status |
| GET | `/govt/volunteers` | Govt | Volunteer list with verification status |
| PATCH | `/govt/volunteers/:id/verify` | Govt | Verify or reject volunteer |
| GET | `/govt/local-operators` | Govt | Operator list with verification status |
| PATCH | `/govt/local-operators/:id/verify` | Govt | Verify or reject operator |
| GET | `/govt/incidents` | Govt | Incident report queue |
| PATCH | `/govt/incidents/:id` | Govt | Update incident status |
| GET | `/govt/trust-appeals` | Govt | Trust score appeal queue |
| PATCH | `/govt/trust-appeals/:id` | Govt | Approve or reject appeal |
| GET | `/govt/checkpoint-scans` | Govt | Checkpoint scan log |

---

## Volunteer Routes (`/volunteers`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/volunteers/register` | None | Volunteer self-registration |
| POST | `/volunteers/login` | None | Volunteer login |
| GET | `/volunteers/me` | Volunteer | Own profile + stats |
| PATCH | `/volunteers/me/status` | Volunteer | Toggle AVAILABLE/OFFLINE |
| PATCH | `/volunteers/me/location` | Volunteer | Update GPS position |
| GET | `/volunteers/me/dispatches` | Volunteer | Active and past dispatches |
| PATCH | `/volunteers/dispatches/:id/accept` | Volunteer | Accept a dispatch |
| PATCH | `/volunteers/dispatches/:id/decline` | Volunteer | Decline a dispatch |
| PATCH | `/volunteers/dispatches/:id/arrive` | Volunteer | Mark arrival at scene |
| PATCH | `/volunteers/dispatches/:id/complete` | Volunteer | Mark case complete |

---

## Other Route Groups

| Group | Key Endpoints |
|-------|--------------|
| `/scam-reports` | POST (file report), GET (by destination) |
| `/incidents` | POST (file incident + photos), GET (own incidents) |
| `/packing` | POST /generate (Gemini packing list for trip) |
| `/journey-passport` | GET /:tripId (PDF download) |
| `/ntn` | POST (send NTN message), GET (inbox) |
| `/push` | POST /subscribe, DELETE /subscribe |
| `/help` | POST /chat (Help chatbot — grounded in live data) |
| `/webhooks` | POST /twilio-inbound (Twilio signature-verified) |

---

## Standard Response Shapes

```json
// Success
{
  "success": true,
  "message": "SOS triggered",
  "data": { "id": "uuid", "status": "ACTIVE", ... }
}

// Error
{
  "success": false,
  "message": "Tourist not found",
  "errors": null
}

// Paginated
{
  "success": true,
  "message": "Trips retrieved",
  "data": [ ... ],
  "pagination": {
    "total": 42,
    "page": 1,
    "limit": 10,
    "totalPages": 5
  }
}
```

## Standard HTTP Status Codes

| Code | When |
|------|------|
| 200 | Successful GET, PATCH, PUT |
| 201 | Successful POST (resource created) |
| 204 | Successful DELETE (no body) |
| 400 | Validation failed / malformed input |
| 401 | Missing or invalid JWT |
| 403 | Valid JWT but insufficient role |
| 404 | Resource not found |
| 409 | Conflict (e.g., phone already registered) |
| 429 | Rate limiter triggered |
| 500 | Unhandled exception (logged, errorHandler catches) |
