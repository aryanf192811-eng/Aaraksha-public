# Data Curation & Sourcing Discipline

Every curated dataset in Aaraksha — destination highlights, `typical_routes` legs,
government-approved itineraries, and local tourism provider stories — follows the same rule:
**a `source` column is required at the database level**, not just a convention. An entry with no
checkable citation cannot be inserted, full stop.

## The source policy

Three tiers, in order of preference:

1. **Official government/institutional sources** — a state tourism department's own published
   route or package, a district administration's registered operator listing, an OpenStreetMap
   node/way ID, UNESCO/Wikipedia/Britannica for destination facts.
2. **Real traveller data already in the platform** — `destination_reviews` rows from actual
   seeded accounts, treated as a legitimate source for "what's it really like" content.
3. **Aaraksha's own hand-assembled routes** — explicitly labeled `Source: Aaraksha —
   hand-assembled from this project's own verified destination data`, never dressed up as a
   government endorsement when one doesn't exist.

**Explicitly banned as sources**: OYO, MakeMyTrip, Airbnb, TripAdvisor, Booking.com, and other
booking aggregators. A local provider or route sourced from a proprietary booking platform's
listing isn't independently verifiable the way a government page or an OSM node is — and this
project's local-operator directory is a trust layer, not a scrape of someone else's inventory.

## A real fabrication, caught and fixed

The clearest evidence this discipline is actually enforced, not just stated: during the first
round of local-operator story curation, an entry claimed a guesthouse had "hosted Rabindranath
Tagore" — a specific, checkable historical claim. An independent web search before the entry was
committed found every real listing for that property describing it as roughly 12 years old,
against Tagore's death in 1941. The claim was **caught before insertion, not after** and the
entry was rewritten without it. The lesson from that catch became a standing rule for every round
since: any curated claim naming a specific person, date, or event gets an independent search
verification pass before it's ever written to the database, regardless of how confident the
sourcing process felt.

A second round of provider-story curation (13 more operators, bringing verified story content to
27 of 71 total providers) applied that same rule — five of the highest-risk claims (named
individuals, founding years, a cross-border MoU) were independently spot-checked before running;
all five held up.

## What this looks like in the schema

- `local_operators.source` — `NOT NULL`, migration `027_local_operators`
- `typical_routes.source` — required, migration `026_travel_data_provenance`
- Curated itineraries: 16 total, two per Northeast Indian state — 3 carrying an actual
  government-tourism-board citation (Meghalaya Tourism's own Shillong–Cherrapunji route, Sikkim
  Tourism's own Gangtok–Pelling package, Assam Tourism Development Corporation's "Circuit 1"
  through Majuli–Jorhat–Kaziranga), the rest honestly labeled Aaraksha-assembled rather than a
  fabricated approval. A real search for citations on the other five states' official tourism
  sites came up empty — that stayed the honest answer instead of being guessed around.

## Real numbers, not a seed script's placeholder count

**71 real, cited local tourism providers** across all 8 Northeast Indian states — hotels,
homestays, registered guides, artisan/handicraft cooperatives, tour operators, and vehicle
rentals — **68 already government-verified**, a small number deliberately left pending as a
genuine, uncoached verify-it-live moment for a demo rather than a fully staged roster. Every
citation is independently checkable: a real OSM node/way ID, or a named government department
page.
