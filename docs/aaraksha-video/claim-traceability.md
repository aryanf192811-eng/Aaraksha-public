# Aaraksha Video: Claim Traceability

Every factual claim in this video is mapped to the canonical facts found in the `README.md` and `SIH_FINAL_ANALYSIS.md` to ensure absolute accuracy for SIH 2026.

| Claim in Video / Screenplay | Source Document Reference | Factual Validation |
|-----------------------------|---------------------------|--------------------|
| **"Builds a costed, safety-scored itinerary based on real destination intelligence."** | `README.md` -> AI Travel Assistant | True. A deterministic scorer (`travelScoring.service.js`) builds the itinerary based on geographic proximity, budget, duration, and verified-local-provider coverage. Gemini only narrates the already-computed numbers. |
| **"Government-verified local homestays and guides."** | `README.md` -> Local Tourism Providers | True. Real hotels, homestays, and guides sourced from official registries and OSM, reviewed by a government operator before any tourist sees them. |
| **"Travel Safety Index (TSI) adapts to weather."** | `README.md` -> Safety | True. The TSI is a 0-100 rule-based score recalculated hourly via a cron job using live OpenWeatherMap data. |
| **"Offline SMS SOS ensures you are never truly alone."** | `README.md` -> Safety / SIH Final Analysis | True. The system uses a Twilio INBOUND webhook to parse structured SMS containing GPS coords, requiring zero data coverage. |
| **"Government command centers see your exact coordinates on 3D terrain."** | `README.md` -> Govt Operations | True. The Govt portal uses MapLibre GL JS + free AWS-hosted elevation tiles to render real 3D terrain. |
| **"Verified citizen volunteers are mobilized."** | `README.md` -> Unified Rescue Network | True. Official rescue teams and govt-verified citizen volunteers share one assignable pool. |
| **"Real OSRM road route."** | `README.md` -> Unified Rescue Network | True. Uses the OSRM public demo server to provide actual road routing rather than straight-line distance. |
| **"Verifiable cryptographic identity... SHA-256 Hash."** | `README.md` -> Verifiable Digital ID | True. A SHA-256 hash chain is maintained over every check-in, SOS, and checkpoint scan. |

**Strict Anti-Hallucination Guardrails Maintained:**
- Did not claim guaranteed rescue.
- Did not describe TSI as an "AI Model" (TSI is rule-based; the Predictive Risk Model is Logistic Regression, kept separate).
- Did not claim a booking/payment marketplace.
- SMS Fallback requires cellular SMS service, correctly depicted by the "zero bars (data)" but successful SMS transmission.
