# Design System

The real design tokens behind all four frontends, verified directly from each app's
`tailwind.config.js` and `index.css` — not a style guide that drifted from the code, the code
itself. All four apps share one token *vocabulary* (`surface`, `on-surface`, `primary`, `trust`,
`sos`, `tsi`) built on shadcn/ui + Radix primitives, but each portal tunes the palette to its own
audience.

## Color tokens

A Material-style `surface`/`on-surface` scale, kept neutral (slate-based) rather than an
auto-generated blue-tinted M3 palette, so it reads consistently with the brand's own amber/teal
accents instead of competing with them.

| Token | Tourist PWA | Govt Command Center |
|---|---|---|
| `surface` (page canvas) | `#f8fafc` (slate-50) | `#f0fdf4` (emerald-50 — the "safety room" identity) |
| `surface-container-lowest` | `#ffffff` | `#ffffff` |
| `on-surface` (primary text) | `#0f172a` (slate-900) | `#0f172a` (slate-900) |
| `on-surface-variant` (secondary text) | `#64748b` (slate-500) | `#475569` (slate-600) |
| `primary` | `#f59e0b` (amber-500) | — |
| `trust` (civic-safety accent) | `#0d9488` (teal-600) | — |
| `sos` | `#ef4444` (red-500) | `#ef4444` (red-500) |
| `safe` | `#22c55e` (green-500) | `#22c55e` (green-500) |

**Why `on-surface-variant` differs between the two apps, deliberately**: `#64748b` on the
Tourist PWA's white/near-white surfaces measures roughly 4.2:1 contrast — under WCAG 2.1 AA's
4.5:1 minimum for normal text. On the Govt Command Center, which GIGW 3.0 holds to that same AA
bar as a public-sector product, the token is `#475569` instead, clearing roughly 7.6:1 while
staying visually "muted." Same design intent, a real accessibility-driven value difference, not
an inconsistency.

**TSI badge colors** — the same four-tier scale everywhere a Travel Safety Index or risk level
renders: `tsi-low` (green-700, `#15803d`), `tsi-moderate` (yellow-700, `#a16207`), `tsi-high`
(orange-700, `#c2410c`), `tsi-extreme` (red-700, `#b91c1c`).

## Typography

One family, Inter, at every weight from body copy to display headlines — matching how SF Pro is
actually used on iOS (a single grotesk varying by weight/size, not two paired display faces,
which reads as trying too hard to look designed). System-ui fallback stack throughout.

| Role | Class | Notes |
|---|---|---|
| Display | `font-display` (Inter), weight 900 | Hero headlines, TSI score numbers |
| Body | `font-sans` (Inter), weight 400 | Everything else |
| Data / tabular | `ui-monospace, SFMono-Regular, monospace` | Fixed-width figures (costs, coordinates) |

## Spacing, radius, elevation

- **Radius scale**: `rounded-xl` (1rem) for cards, `rounded-2xl`/`rounded-3xl` for larger content
  blocks and sheets, `rounded-full` for pills and primary buttons.
- **Elevation**: a custom `shadow-glass` / `shadow-glass-lg` pair (soft, layered shadow +
  inset highlight) for floating toolbars and hero overlays, standard Tailwind `shadow-sm`/`md`/`lg`
  for ordinary cards — reserved for the one element on a screen that's actually meant to look
  "lifted," not stamped on every block.
- **Motion**: `fade-in`, `slide-up`, `scale-in` (150–300ms, ease-out) for content entering the
  screen; a dedicated `pulse-ring` keyframe for SOS-active states, distinct from decorative motion.

## Component discipline

- shadcn/ui (Radix primitives) for every base element — button, dialog, sheet, tabs, dropdown —
  never modified in place; a project-specific look is always a named wrapper component around the
  shadcn primitive, not an edited `components/ui/` file.
- Collapsed-by-default, one-tap-to-expand cards (first established on the Govt Risk Overview page,
  reused for local-operator cards, itinerary cards, and permit guidance) so a list of 3–5 mixed
  cards stays scannable instead of one long card pushing everything else off-screen.
- Two distinct facts are never merged into one line — a "✓ Government Verified" badge and a
  "Source: {citation}" line, for example, always render as two separate elements, because a
  citation being real and a government reviewer having signed off on it are two different claims.
