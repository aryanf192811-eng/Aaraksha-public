# Deployment & Demo Guide — Aaraksha

## Live Deployment

| Portal | URL | Host |
|--------|-----|------|
| Tourist PWA | https://aaraksha-tourist.vercel.app | Vercel |
| Government Command Center | https://aaraksha-govt.vercel.app | Vercel |
| Guardian Portal | https://aaraksha-guardian.vercel.app | Vercel |
| Rescuer App | https://aaraksha-rescuer.vercel.app | Vercel |
| Backend API | Render (Singapore) | Render |
| Database | PostgreSQL (Render, Singapore) | Render |

---

## Demo Day Preparation

### Before Going on Stage

1. **Warm up the backend** — Render free tier cold-starts after idle.
   Open the backend health endpoint ~2 minutes before your demo:
   ```
   GET /health → {"status":"ok"}
   ```
   If you see a 502, wait 20–30 seconds and retry. This is normal Render free-tier behavior.

2. **Verify demo accounts** are in the expected states (see Demo Accounts below).

3. **Pre-load each portal** on separate browser tabs.

4. **Silence browser notifications** — push notifications can interrupt the demo.

---

## Demo Accounts (Vadodara / Parul University Scenario)

Full details in [`VADODARA-DEMO-DATA.md`](../testing/VADODARA-DEMO-DATA.md).

| Role | Account | State |
|------|---------|-------|
| Tourist | Meera Shah | Active trip, DMS enabled, guardian link set |
| Rescuer | Rajesh Solanki | Govt-verified, available |
| Rescue Team | Parul University Response Team | Active in system |

---

## Recommended Demo Flow (SOS → Resolution)

### Total time: ~5–7 minutes

**Step 1 — Tourist Portal (2 min)**
- Log in as Meera Shah
- Show Dashboard → TSI badge (Moderate Risk)
- Show Active Trip → built itinerary with Tawang stops
- Show Guardian Link → copy and open in new tab

**Step 2 — Guardian Portal (30 sec)**
- Open Guardian URL
- Enter PIN → shows live map + check-in timeline

**Step 3 — Trigger SOS (1 min)**
- Return to Tourist app
- Tap SOS → select MEDICAL → confirm
- Show "SOS Triggered" confirmation

**Step 4 — Government Command Center (2 min)**
- Log in as govt officer (separate browser or incognito)
- SOS pin appears on Live Ops Map (Socket.IO real-time)
- Click pin → triage panel: tourist's blood group, hospital distance
- Assign rescue team: "Parul University Response Team"
- Optionally assign Rajesh Solanki (volunteer)

**Step 5 — Rescuer App (1 min)**
- Log in as Rajesh Solanki
- Dispatch notification appears
- Accept → ActiveJobPage opens with MapLibre route to SOS location

**Step 6 — Resolution (30 sec)**
- Back in Govt portal: mark SOS Resolved
- Tourist app: shows "Rescue completed"
- Guardian portal: status updates in real-time

---

## Demo: AI Trip Planner

**Prompt to use:**
```
Plan a 7-day solo trek to Meghalaya and Arunachal starting from Delhi.
I love waterfalls and living root bridges. Budget around Rs 15,000.
```

**Expected flow:**
1. Loading → Gemini extracts intent (SOLO, ADVENTURE, NATURE, Meghalaya, Arunachal, Delhi gateway, 7 days)
2. Deterministic scorer ranks destinations by interest match
3. OSRM-based routing for inter-destination legs
4. Gemini writes prose narrative
5. Review and accept → trip created

---

## Demo: Offline SOS Path

**To demonstrate (use a real device):**
1. Enable Airplane Mode
2. Open pre-filled SMS in tourist app → "Send SOS via SMS"
3. SMS content: `AARAKSHA_SOS|ID:{id}|LAT:{lat}|LNG:{lng}|CAT:MEDICAL|BATT:34|TIME:{ts}`
4. Send to Twilio number
5. Show that SOS appears on Govt dashboard (via Twilio webhook)

---

## Demo: Dead Man's Switch

**Live demo using demo-seconds mode:**
1. Enable DMS with 60-second demo interval
2. Wait 60 seconds without checking in
3. System sends warning SMS
4. Wait another configured window
5. SOS auto-fires with `trigger_type = DMS`
6. Appears on govt dashboard automatically

---

## CI/CD Pipeline

```
Git push to main
    │
    ├── GitHub Actions: backend vitest (against ephemeral Postgres)
    ├── GitHub Actions: tsc -b (all 4 frontends)
    │
    ├── Render: auto-deploy backend
    │   startCommand: npm run migrate && npm start
    │   → migrations apply on every deploy
    │   → health check at /health
    │
    ├── Vercel: auto-deploy tourist portal
    ├── Vercel: auto-deploy govt portal
    ├── Vercel: auto-deploy guardian portal
    └── Vercel: auto-deploy rescuer portal
```

---

## Environment Variables

**No secrets appear in this public repository.**

See `.env.example` in the private backend repo for the full list. Minimum required:

| Variable | Required | Purpose |
|----------|----------|---------|
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `JWT_SECRET` | Yes | Must be ≥32 chars |
| `PORT` | No | Defaults to 5000 |
| `GEMINI_API_KEY` | No | AI features fall back to static content |
| `OWM_API_KEY` | No | Weather factor drops out of TSI |
| `TWILIO_*` | No | SMS path disabled; SOS still works via DB + Socket.IO |
| `VAPID_*` | No | Push notifications silently disabled |

All external service keys are optional — each degrades gracefully when absent.

---

## Known Platform Limitations (Not App Bugs)

1. **Render free tier cold starts** — 20–30 second delay after idle. Ping `/health` before demo.
2. **Database state drift** — Demo SOS records should be freshly triggered if you want to show live rescue assignment. Run `npm run seed:reset` to restore original demo states.
3. **Vercel build cache** — First deploy after a schema change may need a cache clear.
