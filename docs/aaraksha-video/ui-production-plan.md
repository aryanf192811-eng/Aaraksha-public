# Aaraksha Video: UI Production Plan

For the side-by-side scenes, the right half of the screen will display the actual Aaraksha UI to prove the implementation.

### UI Frame 1: AI Travel Assistant (Scene 2)
- **Portal:** Tourist PWA
- **Theme:** Amber Primary, Light Mode
- **Feature:** Build My Journey
- **Visual:** The chat interface showing the prompt "6 days in Meghalaya, nature focused." Below it, the generated itinerary cards with `totalCostInr` and the deterministic safety score. Ensure the `estimated: false` tag is visible for curated routes.

### UI Frame 2: Local Tourism Provider (Scene 3)
- **Portal:** Tourist PWA
- **Theme:** Amber Primary
- **Feature:** Verified Directory
- **Visual:** A destination detail sheet displaying Tenzing's Homestay. The green "✓ Government Verified" badge must be prominently separated from the "Source: Meghalaya Tourism" citation. Both the tap-to-call and WhatsApp deep links should be visible.

### UI Frame 3: Destination Intelligence (Scene 4)
- **Portal:** Tourist PWA
- **Theme:** Amber Primary
- **Feature:** Travel Safety Index (TSI)
- **Visual:** The circular TSI meter spinning down from an 80 (Green) to a 45 (Orange/Red). A weather-triggered risk alert toast notification at the top of the screen.

### UI Frame 4: Offline SOS Trigger (Scene 5)
- **Portal:** Tourist PWA
- **Theme:** Amber / Red Alert
- **Feature:** Offline SMS Fallback
- **Visual:** The "Hold to Confirm" SOS button being pressed. A simulated "No Internet" banner at the top, followed by a system modal showing "Sending Emergency SMS...".

### UI Frame 5: Govt Command Center (Scene 6)
- **Portal:** Govt Command Center
- **Theme:** Slate-900 (Dark Mode)
- **Feature:** 3D Live Ops Map & Rescue Dispatch
- **Visual:** MapLibre GL JS 3D elevation terrain. A red pulsing SOS marker. The rescue assignment panel on the right showing Dev (Volunteer) with a high weighted score, and the operator clicking "Dispatch".

### UI Frame 6: Rescuer App Tracking (Scene 6)
- **Portal:** Rescuer App
- **Theme:** Teal Primary
- **Feature:** OSRM Road Routing
- **Visual:** A full-screen live map with a real road route traced from the rescuer's GPS ping to the SOS marker. The "Start Navigation" button is active.

### UI Frame 7: Journey Integrity Hash (Scene 7)
- **Portal:** Tourist PWA (Digital Journey Passport)
- **Theme:** Amber / Document
- **Feature:** Hash Chain Verification
- **Visual:** A PDFKit-style summary showing the genesis block, check-in, and checkpoint scan, concluding with a long SHA-256 alphanumeric string `9952f113…c8947` changing dynamically.
