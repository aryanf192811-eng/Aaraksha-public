# Project Overview — Aaraksha

## Problem Statement: SIH PS 26204

> Design a comprehensive travel safety and information platform for tourists visiting Northeast India,
> integrating real-time safety alerts, emergency response coordination, local tourism promotion and
> information services including hotels, travel and others.

## What Makes Northeast India Uniquely Challenging

Northeast India (the "Seven Sisters" + Sikkim) presents a unique combination of hazards
that no existing platform addresses holistically:

| Factor | Impact |
|--------|--------|
| Connectivity | Large blackspots — zero signal in parts of Arunachal, Nagaland, Sikkim |
| Terrain | Altitude sickness risk >3,000m; landslide zones in monsoon; dense forest |
| Permits | Inner Line Permit required for multiple districts (foreigners + some Indian states) |
| Medical | Nearest hospital can be 50+ km from remote trekking routes |
| Monsoon | June–September: landslides, flash floods, road closures are common |
| Languages | 8 states, 200+ dialects — communication barrier for distress signaling |

## Three Pillars of Aaraksha

### Pillar 1 — Planning & Intelligence
*"Know before you go"*

- AI-powered itinerary builder (Gemini + deterministic scoring)
- Travel Safety Index (TSI) — rule-based risk score per trip
- Destination database: 30 NER destinations with connectivity, altitude, zone type, medical proximity
- Curated itineraries by interest tags (ADVENTURE, CULTURE, PILGRIMAGE, NATURE)
- Typical routes with sourced travel time and cost data
- Destination news feed (safety advisories, trail closures)
- AI packing list generator
- Journey Passport PDF (PDFKit, 9 sections, QR code)

### Pillar 2 — Safety & Response
*"Stay safe, get rescued"*

- One-tap SOS with GPS (5 categories)
- Dead Man's Switch (auto-SOS on timeout — even without app open)
- Manual check-ins with GPS + battery
- Offline SOS via structured SMS (works in zero-internet zones)
- Guardian portal (PIN-gated family tracking)
- Real-time rescue tracking (MapLibre GL + OSRM)
- Trust score system (anti-abuse without blocking emergency path)
- Incident reporting with photo evidence
- Scam reporting

### Pillar 3 — Government & Local Ecosystem
*"Connect the institutions"*

- Government Command Center: live ops map, SOS triage, rescue assignment
- Volunteer/Rescuer network: govt-verified local responders
- Local operator ecosystem: hotels, homestays, guides, artisans — govt-verified before tourist visibility
- District risk overview with anomaly detection
- Analytics: resolution times, SOS trends, operator verification rate
- DPDP Act 2023 compliance: data export, erasure, appeals

## Target Users

| User | Portal | Primary Goal |
|------|--------|-------------|
| Domestic/foreign tourist | Tourist PWA | Plan safely, get rescued if needed |
| Tourist's family/friend | Guardian Portal | Know loved one is safe |
| District Officer | Govt Command Center | See live ops, coordinate rescue |
| Rescue Coordinator | Govt Command Center | Assign teams efficiently |
| Trained local volunteer | Rescuer App | Respond to nearby emergencies |
| Local tourism operator | Rescuer App (operator view) | Get verified, get discovered |

## Northeast India Destinations (Seeded — 30 locations)

Covering all 8 states:
- **Meghalaya:** Living root bridges (Cherrapunji), Dawki, Mawsynram
- **Assam:** Kaziranga, Majuli (world's largest river island), Kamakhya
- **Arunachal Pradesh:** Tawang (4,000m+), Ziro, Mechuka
- **Nagaland:** Dzukou Valley, Kohima, Hornbill village
- **Sikkim:** Gurudongmar Lake (5,100m+), Lachung, Pelling
- **Manipur:** Loktak Lake, Kangla Fort, Moreh
- **Mizoram:** Phawngpui (Blue Mountain), Aizawl, Tam Dil
- **Tripura:** Unakoti, Neermahal, Jampui Hills

## Innovation Highlights

1. **Worst-stop-wins TSI logic** — a trip's risk is never averaged; the most dangerous stop
   drives the score. A safe Guwahati start doesn't dilute a Tawang winter trek.

2. **Offline SOS via structured SMS** — GPS coords from satellite radio, transmitted via
   SMS on 2G, parsed by Twilio webhook. Works when the app has no internet.

3. **AI-as-narrator, not AI-as-judge** — Gemini only provides prose and intent extraction.
   All routing, ranking, cost and safety decisions are deterministic code that can be audited.

4. **Government-gated trust chain** — volunteers, local operators, checkpoint scans all
   require govt officer approval before they have any effect on tourists.

5. **Non-blocking emergency path** — the trust score system can restrict convenience features
   but can never block a real SOS trigger. Anti-abuse logic never gates the emergency path.
