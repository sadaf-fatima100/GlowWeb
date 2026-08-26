---
name: production-frontend-design
description: Use this skill whenever building, redesigning, or reviewing any web UI — landing pages, agency/portfolio sites, SaaS dashboards, marketing pages, or components. Combines distinctive art-direction principles with hard production-level rules for typography scale, responsive breakpoints, spacing/padding, orphan-word control, and animation, so output looks like a shipped premium product instead of a generic AI template.
license: Custom
---

# Production Frontend Design

Act as the design lead at a small studio known for giving every client a visual identity that could not be mistaken for anyone else's. The client has already rejected proposals that felt templated and is paying for a distinctive point of view. This document has four parts: **Part 0 — discovery** (research before any design decision), **Part A — art direction** (how to think), **Part B — visual production rules** (typography/spacing/motion hard numbers), and **Part C — architecture & responsiveness** (clean code structure + perfect behavior at every width/height). All four apply together — skipping discovery produces a pretty page that doesn't fit the market; skipping architecture produces a page that looks right on launch day and breaks by week three; skipping Part B produces amateur execution of a good idea.

The tech stack is not fixed in this document — it is supplied later via the user's prompt (React, Next.js, plain HTML/CSS, Vue, etc.). Apply these principles regardless of stack; only the syntax changes.

---

## PART 0 — Discovery & Research (before any design decision)

Production teams never open a design tool before this phase is done. Skipping it is the single most common reason a "finished" design gets reworked later — not because the execution was bad, but because it solved the wrong problem.

### 1. Define the goal first
Pin down the business objective in one sentence before anything else (generate leads, sell a product, explain a service, get sign-ups). Every later decision — layout, copy, CTA placement — is judged against this one sentence.

### 2. Research the industry and audience
- **Who uses this**: demographics, but more importantly motivations, pain points, and the specific task they came to do
- **Where they're coming from**: search intent, referral context, prior familiarity with the category — this affects how much explaining the page needs to do before asking for anything
- **Psychology/behavior cues relevant to the industry**: e.g. a fintech audience needs trust signals and low visual risk; a creative agency audience rewards visual boldness; an enterprise SaaS audience scans for proof (logos, numbers, case studies) before reading a single sentence of copy

### 3. Competitor research (3–5 direct competitors, not more)
For each competitor, look at:
- How they position themselves and structure their homepage narrative
- Their information architecture — menu structure, categorization, how many clicks to the key action
- Visual patterns they all share (these are the category's baseline expectations — deviate deliberately, not accidentally) and gaps where all of them are weak (this is the opportunity)
- Their tech stack if relevant (informs feasibility, not required for pure design work)

The goal isn't to copy the category average — it's to know it well enough to deliberately match it where it builds trust and break it where it creates differentiation.

### 4. Translate research into structure
Only after 1–3 are done: build the sitemap / information architecture (what pages/sections exist and how they connect), then wireframe the content skeleton (structure and hierarchy, no visual styling yet). Visual design (Part A/B) is the *last* step, not the first — a beautiful layout built before the content hierarchy is settled gets rebuilt, not adjusted.

### 5. Output of this phase (carry into Part A)
- One-sentence business goal
- One-paragraph audience profile (who + what they need from this page + what would make them trust it)
- 2–3 things every competitor does (match these — they're expected) and 1–2 gaps none of them cover (this is the differentiation opportunity, and often the seed of the "signature element" in Part A)

---

## PART A — Art Direction

### Ground it in the subject
If the brief doesn't pin down the product/subject, pin it yourself before designing: name one concrete subject, its audience, and the page's single job, and state the choice. Build with the brief's real content and subject matter throughout — the subject's own world, materials, vernacular is where distinctive choices come from.

### Design principles
- **Hero is a thesis.** Open with the most characteristic thing in the subject's world — headline, image, animation, live demo, interactive moment. A big number + small label + gradient accent is the template answer; only use it if it's genuinely the best option for this brief.
- **Typography carries personality.** Pair display and body faces deliberately — not the defaults you'd reach for on any project. Ban Inter, Roboto, Arial, plain system-ui, and Space Grotesk as the *display* face — they read as AI-default. Set a clear type scale with intentional weights, widths, and spacing (see Part B for the numbers).
- **Structure is information.** Numbering, eyebrows, dividers, labels should encode something true about the content, not decorate it. Numbered markers (01/02/03) only belong where the content is a real sequence.
- **Motion is deliberate.** One well-orchestrated moment (page-load sequence, scroll-triggered reveal) lands harder than scattered micro-interactions everywhere. Sometimes less is more — excess animation itself reads as AI-generated.
- **Match complexity to the vision.** Maximalist directions need elaborate execution; minimal directions need precision in spacing, type, detail.
- **Color and theme.** Commit to a cohesive 4–6 hex-value palette using CSS variables. Dominant color + sharp accent beats a timid, evenly distributed palette. Avoid the cliché near-#F4F1EA cream + #D97757 terracotta combo, near-black + single neon accent, and broadsheet hairline-rule layouts — these are the three current AI-design defaults. Follow the brief exactly where it specifies a direction; don't spend free axes on these defaults.
- **Backgrounds/detail.** Gradient meshes, noise textures, geometric patterns, layered transparency, dramatic shadows, decorative borders, grain overlays — used with restraint, in service of the signature element only.

### Process
1. **Brainstorm a compact token system**: Color (4–6 named hex values), Type (2+ roles: characterful display face used with restraint, complementary body face, utility face for captions/data), Layout (one-sentence concept + ASCII wireframe), Signature (the one unique element this page will be remembered by).
2. **Critique against the brief**: if any part reads like the generic default for any similar brief, revise it and note what changed.
3. **Build** exactly to the revised plan, applying every rule in Part B.
4. **Self-critique**: responsive down to mobile, visible keyboard focus, `prefers-reduced-motion` respected. Spend boldness in one place; cut decoration that doesn't serve the brief.

### Writing in the design
Words are design material. Write from the end user's side of the screen — name things by what people control, not how the system is built. Active voice: "Save changes," not "Submit." Keep the button's label consistent through the whole flow (Publish → "Published"). Errors explain what happened and how to fix it, never vague, never apologetic. Empty states are an invitation to act.

---

## PART B — Production Rules (hard numbers)

### 1. Breakpoints (mobile-first)
```
Mobile:        320px – 480px    (default/base styles start here)
Mobile-L:      481px – 767px
Tablet:        768px – 1023px
Laptop:        1024px – 1279px
Desktop:       1280px – 1439px
Large Desktop: 1440px+
```
Write CSS mobile-first: base styles for mobile, then `min-width` media queries scale up. Container `max-width: 1280px`–`1440px`, centered with `margin: 0 auto`.

### 2. Typography scale
Prefer fluid `clamp()` over fixed per-breakpoint sizes — no visual jumps on resize.

```css
h1 { font-size: clamp(2.25rem, 1.9rem + 2vw, 4.5rem); }    /* 36px → 72px */
h2 { font-size: clamp(1.75rem, 1.5rem + 1.2vw, 3rem); }    /* 28px → 48px */
h3 { font-size: clamp(1.375rem, 1.2rem + 0.8vw, 2rem); }   /* 22px → 32px */
h4 { font-size: clamp(1.125rem, 1rem + 0.5vw, 1.5rem); }   /* 18px → 24px */
body, p { font-size: clamp(1rem, 0.95rem + 0.2vw, 1.125rem); } /* 16px → 18px */
small, .caption { font-size: 0.875rem; }                    /* 14px fixed */
```
Scale ratio: 1.25 (Major Third) or 1.333 (Perfect Fourth) between heading levels for consistent hierarchy.

Fixed-breakpoint reference (if not using clamp):

| Element | Mobile ≤767px | Tablet 768–1023 | Desktop 1024+ |
|---|---|---|---|
| H1 (hero) | 32–40px | 44–56px | 56–80px |
| H2 (section) | 26–30px | 32–38px | 40–48px |
| H3 | 20–22px | 24–26px | 28–32px |
| H4 | 18px | 18–20px | 20–22px |
| Body | 16px | 16–17px | 17–18px |
| Small/caption | 13–14px | 14px | 14px |

**Line-height & weight:**
- Headings: `line-height: 1.1–1.25` (tight)
- Body: `line-height: 1.5–1.7` (readable)
- H1/H2 → `font-weight: 700`, H3/H4 → `600`, body → `400`
- Large headings: `letter-spacing: -0.02em` to `-0.04em` for a tight, premium feel

### 3. Orphan/widow control — no lone word wrapping to the next line
```css
h1, h2, h3, h4 {
  text-wrap: balance;   /* evenly balances lines, headings up to ~6 lines */
}
p, li, blockquote {
  text-wrap: pretty;    /* prevents a single word stranded on the last line */
}
```
`balance` → headings/subheadings. `pretty` → body paragraphs (only adjusts the tail). Supported in Chrome/Edge/Safari 17.5+; Firefox falls back gracefully to normal wrap, no breakage. Extra safety net for headings: `max-width: 20ch`–`30ch` so natural breaks land in sensible places.

### 4. Spacing — 8pt grid
```
Base unit = 8px
Scale: 4, 8, 16, 24, 32, 40, 48, 64, 80, 96, 128
```
Use 4px only for fine adjustments (icon spacing, tight gaps). Every margin/padding/gap must be picked from this scale — never arbitrary values like 13px or 15px.

**Rule: internal ≤ external.** Padding inside an element should be ≤ the margin/gap separating it from other elements — this keeps grouping visually clear (Gestalt proximity).

| Context | Mobile | Desktop |
|---|---|---|
| Section vertical padding | 48–64px | 96–160px |
| Container side padding | 16–24px | 64–120px (or centered max-width) |
| Heading → body gap | 16–24px | 24–32px |
| Card/grid item gap | 16–24px | 24–40px |
| Button internal padding | 12px 20px | 14px 28px |

### 5. Layout & grid
- Container: `max-width: 1280–1440px`, `margin: 0 auto`
- Grid gutters: 16px mobile → 24–32px desktop
- Columns: 1 (mobile) → 2 (tablet) → 3–4 (desktop); prefer `grid-template-columns: repeat(auto-fit, minmax(...))` over hardcoded breakpoints where content allows
- Body copy reading width: `max-width: 60–75ch`

### 6. Motion & responsiveness — full system

**Performance rule (non-negotiable):** animate only `transform` and `opacity`. These bypass layout/paint and go straight to the GPU compositor — smooth 60fps even on mid-range mobile. Animating `width`, `height`, `top`, `left`, or `margin` forces layout recalculation every frame — the fastest way to produce visible jank. Use `translateX/Y`, not `left/top`.

**Duration bands — pick by what the motion needs to communicate, not by taste:**

| Category | Duration | Use for |
|---|---|---|
| Micro-interactions | 100–200ms | Button press, toggle flip, checkbox check, tap feedback |
| Standard UI transitions | 200–350ms | Hover states, dropdowns, tab switches, card lift |
| Dramatic entrances | 350–600ms | Modal open, hero reveal, page transition |
| Anything over 600ms | avoid unless justified | Only for a genuinely cinematic, one-time moment |

Rule of thumb for the whole system: **60% of animations use one workhorse ease-out curve** (reliable, invisible, correct) · **30% use secondary curves** (a sharper "snap" curve for micro-interactions, ease-in for exits) · **10% can be dramatic** (springs, overshoots, custom curves) — reserved for the signature moment only.

**Named easing curves (cubic-bezier) — pick by intent, not by "looks nice":**

```css
/* Entering elements — fast start, decelerates smoothly into place */
--ease-out:        cubic-bezier(0.16, 1, 0.3, 1);      /* premium, Stripe/Linear-style "settle" */
--ease-out-cubic:   cubic-bezier(0, 0, 0.58, 1);

/* Exiting elements — gentle start, accelerates out */
--ease-in:          cubic-bezier(0.42, 0, 1, 1);

/* Standard UI workhorse — symmetric, used for hover/dropdown/most transitions */
--ease-standard:    cubic-bezier(0.4, 0, 0.2, 1);       /* Material's default — safe, professional, 250–300ms */

/* Snap / button press — quick, decisive feedback */
--ease-snap:        cubic-bezier(0.4, 0, 0.2, 1);       /* pair with 80–150ms duration */

/* Playful pop / success confirmation — slight overshoot past 100% then settles */
--ease-back:         cubic-bezier(0.34, 1.56, 0.64, 1); /* add-to-cart, like button, checkmark — use sparingly, overuse reads "toy-like" */

/* Elastic / error shake — oscillates to draw the eye without being aggressive */
--ease-elastic:      cubic-bezier(0.68, -0.55, 0.27, 1.55);
```
Never use `linear` for anything user-facing except continuous loops (spinners) — it reads mechanical. Never pair a short duration (<150ms) with a bouncy/back-out curve — there isn't enough time for the overshoot to read, it just looks glitchy.

**Practical examples:**
```css
/* Card hover lift */
.card { transition: transform 200ms var(--ease-back), box-shadow 200ms var(--ease-back); }
.card:hover { transform: translateY(-4px); }

/* Button press feedback */
.button { transition: transform 200ms var(--ease-back); }
.button:active { transform: scale(0.95); transition-duration: 80ms; transition-timing-function: var(--ease-standard); }

/* Mobile drawer / bottom sheet entrance */
@keyframes slideUp { from { opacity: 0; transform: translateY(100%); } to { opacity: 1; transform: translateY(0); } }
.slide-up { animation: slideUp 300ms var(--ease-out) forwards; }
```

**Stagger patterns (lists, grids, galleries):**
```css
.stagger-item { animation: fadeInUp 400ms var(--ease-out) backwards; }
.stagger-item:nth-child(1) { animation-delay: 0ms; }
.stagger-item:nth-child(2) { animation-delay: 60ms; }
.stagger-item:nth-child(3) { animation-delay: 120ms; }
/* or generate via JS/SCSS loop: delay = index * 50–100ms, cap total sequence under ~800ms */
```
Stagger delay per item: `50–100ms`. Beyond ~8–10 items, cap the total sequence length rather than keep incrementing delay — a 40-item list shouldn't take 4 seconds to finish revealing.

**Scroll-driven animation — two approaches:**

1. **Native CSS (no JS, 2026 baseline support in Chrome/Edge/Safari)** — use `animation-timeline` for scroll-linked motion with zero main-thread JS:
```css
@keyframes reveal { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: translateY(0); } }
.reveal-on-scroll {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}
```
2. **Intersection Observer + class toggle** — for broader browser support or when JS control is needed; add a class on intersect, let CSS transition handle the animation, keep threshold around `0.15–0.25` so the reveal triggers naturally as content enters view, not right at the edge.

For truly complex orchestrated sequences (parallax layers, pinned sections, timeline scrubbing), a library like GSAP + ScrollTrigger is the practical choice — but reserve it for the one signature moment on the page, not every section.

**Micro-interaction categories — every animation must fall into one of these, or cut it:**
- **Anticipation** — subtle response before a click registers (button scales slightly on `:active` before the action fires)
- **Confirmation** — form checkmark, button label changes to "Sent!", toggle flips — confirms the action was registered
- **Progress** — skeleton screens, progress bars, spinners that communicate "working," never a silent freeze
- **Transition** — page transitions, dropdown open/close, mobile nav slide — removes jarring jumps between states
- **Attention** — a subtle pulse on a CTA, a gentle bounce on a scroll indicator — guides the eye, use max once per screen

If an animation doesn't serve one of these five purposes, it's decoration, not design — cut it.

**Mobile-specific rules:**
- Respect `100dvh` / `100svh` over `100vh` for full-height sections — avoids mobile browser chrome jump on scroll
- Remove default tap highlight, replace with an intentional `:active` state: `-webkit-tap-highlight-color: transparent;`
- Hover-only effects (`:hover`) must have a touch-equivalent (`:active` or `:focus-visible`) — touch devices never trigger `:hover` reliably
- Keep touch targets ≥ 44×44px regardless of visual size

**Accessibility — always ship both:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
Don't just disable — provide a simplified fallback (e.g. a slide becomes a plain fade) so the reduced-motion experience isn't jarringly static either.

**Golden rule:** one well-orchestrated signature moment (hero load sequence, one scroll-triggered set-piece) beats animation scattered across every element. If you can't explain in one sentence *why* an element animates, remove the animation.

---

## PART C — Architecture, Clean Code & Perfect Responsiveness

Before writing the first line of visual CSS, production developers settle the *structure* the same way Part 0 settles the *content*. A gorgeous component in a messy codebase gets rewritten within a sprint; get this right once and every future page/feature slots in without a rebuild.

### 1. Clean architecture — first thing a developer thinks about
- **Organize by feature/domain, not by file type.** A flat split like `components/`, `hooks/`, `utils/` at the root looks clean at 5 components and becomes unmanageable at 50. Group everything related to one feature together:
```
src/
  features/
    auth/
      components/
      hooks/
      services/
      types.ts
    dashboard/
      components/
      services/
    shared/
      components/   ← generic, reusable across features (Button, Modal, Input)
      hooks/
      utils/
  app/ or pages/     ← routing layer only
  lib/               ← third-party config, API clients
```
This applies regardless of framework — the same feature-first grouping works in Next.js, Vue, or plain multi-page HTML (group by page/section instead of by CSS-file-type).
- **Every feature/module exposes a public API** (an `index` file or clear entry point). Code outside the feature imports only from that entry point, never reaches into internal files. Test: imagine deleting one feature folder — if that breaks unrelated folders, the boundaries have leaked.
- **Consistent naming.** `authSlice.ts`, `authApi.ts`, `AuthPage.tsx`, `useAuth.ts` — not random names that force a developer to open the file to know what it does.
- **Don't mix concerns in one file**: no API calls inside a UI component, no styling logic inside a data-fetching function. Each file has one clear responsibility.
- **Shared vs. feature-specific**: if a component/hook is used by 2+ features, promote it to `shared/`. If it's used by one, keep it inside that feature — premature abstraction is as costly as no abstraction.

### 2. Perfect responsiveness at every width AND height — not just standard breakpoints
Standard breakpoints (Part B, section 1) handle *width* checkpoints, but production sites must hold up at every value in between and at every height too:

- **Never assume a fixed height.** Use `min-height` instead of `height` for sections so content can grow without clipping. For full-viewport sections use `min-height: 100dvh` (dynamic viewport height) instead of `100vh` — `vh` doesn't account for mobile browser chrome (address bar) appearing/disappearing on scroll, which causes visible jumps; `dvh` does.
- **Test the gaps between breakpoints, not just at them.** Slowly resize from 320px to 1920px — the design must not have a "dead zone" width where content is too wide for one column but too cramped for two. If a gap breaks, that width becomes a new content-based breakpoint (odd values like 642px or 860px are normal and correct if that's where the real content breaks).
- **Test both orientations.** A phone in landscape has viewport dimensions similar to a small tablet — if tablet styles assume portrait, they'll misfire in landscape. Check both.
- **Fluid units over fixed breakpoints where possible**: `clamp()`, `%`, `fr`, `vw`/`vh` reduce the number of hard jumps needed. Combine fluid scaling with breakpoints rather than choosing only one approach.
- **Use container queries (`@container`) for reusable components** — not just viewport media queries. A card component should adapt to the width of its parent container (sidebar vs. full-width grid), not just the page's viewport, so the same component behaves correctly everywhere it's dropped.
- **Never assume a specific screen width in component styles.** Use Flexbox/Grid to let content reflow naturally; add a breakpoint only when the layout visibly breaks, not preemptively for every device name.
- **Images/media**: always fluid (`max-width: 100%; height: auto;`) or with explicit `aspect-ratio` set, never a hardcoded pixel height that causes overflow or squashing on narrow screens.
- **Test on real devices, not just resizing the browser.** Emulators miss iOS Safari's handling of viewport units, momentum scrolling, and touch-target quirks — verify on at least one real iOS and one real Android device before calling a build done.
- **Respect user-preference media features** as seriously as viewport breakpoints: `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast` — these are breakpoints too, just for accessibility instead of screen size.

### 3. Pre-code checklist (run before touching visual styling)
- [ ] One-sentence goal, audience profile, and competitor gap list exist (Part 0 output)
- [ ] Sitemap/information architecture and content wireframe done before any visual styling
- [ ] Folder structure is feature-based, not type-based; naming is consistent
- [ ] Every shared/reusable piece lives in `shared/`; nothing feature-specific leaks into it
- [ ] No component assumes a fixed height or a specific viewport width
- [ ] `dvh`/`svh` used for full-height sections, not raw `vh`

---

## PART D — Design Tokens, Components, SEO & Performance

This part covers the system-level tokens and production checks that sit underneath everything in Parts A–C: the named tokens a design system needs beyond typography/spacing (already covered in Part B), the component inventory, interaction states, naming discipline, and the SEO/performance work that makes a page production-ready, not just good-looking.

### 1. Color system — semantic tokens, not raw hex sprinkled everywhere
Beyond the 4–6 brand hex values (Part A), define semantic roles so every color use has a reason:
```
--color-primary       /* main brand action color */
--color-secondary     /* supporting brand color */
--color-accent        /* the sharp highlight from Part A's palette */
--color-surface       /* card/panel backgrounds */
--color-background    /* page background */
--color-border         
--color-text-primary
--color-text-muted
--color-success / --color-error / --color-warning   /* status colors, consistent across all forms/toasts/badges */
```
Every component pulls from these tokens — never a one-off hex value inline. This is what lets a whole site re-theme (e.g. dark mode) by swapping token values instead of hunting through files.

### 2. Radius, shadow & elevation system
Pick one radius scale and one shadow scale for the whole project — don't let each component invent its own:
```
--radius-sm: 6px;   --radius-md: 12px;  --radius-lg: 20px;  --radius-full: 999px;
--shadow-sm: 0 1px 2px rgba(0,0,0,.05);
--shadow-md: 0 4px 12px rgba(0,0,0,.08);
--shadow-lg: 0 12px 32px rgba(0,0,0,.12);
```
Elevation should communicate hierarchy: resting cards get `--shadow-sm`, hovered/active cards or modals get `--shadow-md`/`--shadow-lg`. Don't reach for arbitrary shadow values per component.

### 3. Interaction states — every interactive element needs all of these, not just default + hover
`default → hover → active/pressed → focus (visible outline, not just browser default) → disabled → loading → success → error`. Skipping loading/error/success states is the most common reason a form or button feels unfinished — the visual design being "done" for the default state isn't the same as the component being production-ready.

### 4. Core reusable component inventory
Plan these as a shared library before building individual pages, so no two pages reinvent the same pattern differently: navbar, footer, hero, cards, buttons (primary/secondary/ghost variants), form inputs, pricing table, testimonials, FAQ accordion, CTA section, portfolio/case-study grid, modal/dialog, badge/tag, toast/notification. Each gets built once against the token system above and reused — never duplicated with slightly different spacing or colors per page.

### 5. Naming conventions
Class/component/file names should describe what the thing *is*, not be a placeholder: `hero-section`, `service-card`, `pricing-grid`, `primary-button` — not `box1`, `div2`, `style-new`, `final-final`, `test`. This matters as much for maintainability as the folder architecture in Part C — a well-organized folder full of meaninglessly-named files is still hard to navigate.

### 6. SEO essentials (every page, not just the homepage)
- One `<h1>` per page, clear heading hierarchy after it (no skipped levels)
- Meta title + meta description unique per page
- Open Graph tags for social previews, canonical URL to avoid duplicate-content issues
- `robots.txt` / meta robots set intentionally (index vs noindex)
- Structured data (schema.org JSON-LD) where the content type supports it — articles, products, FAQs, local business
- Sitemap generated/updated as pages are added

### 7. Performance & Core Web Vitals
- Images: correct format (AVIF/WebP with fallback), responsive `srcset`, lazy-loaded below the fold, explicit `width`/`height` or `aspect-ratio` set to prevent layout shift (CLS)
- Fonts: subset where possible, `font-display: swap`, preload the critical display font only
- JS/CSS: ship only what the page needs — no unused component libraries bundled in; defer/async non-critical scripts
- Avoid render-blocking resources in `<head>`; critical CSS inlined for above-the-fold content on marketing pages is a common production technique
- Target: good Largest Contentful Paint, minimal Cumulative Layout Shift, fast Interaction to Next Paint — treat image/font loading and animated-layout-shift (Part B, section 6) as the two biggest levers on these

---

## FINAL Pre-ship Checklist (all parts combined)
- [ ] Responsive down to 320px, no horizontal scroll, tested at intermediate widths too — not just at standard breakpoints
- [ ] Tested at real device heights and both orientations; no fixed `height`/`vh` on full-screen sections (`dvh`/`min-height` used instead)
- [ ] Reusable components use container queries where they appear in more than one layout context
- [ ] Visible keyboard focus states on every interactive element
- [ ] Headings use `text-wrap: balance`, body uses `text-wrap: pretty`
- [ ] All spacing values are 8pt-grid multiples (4px exception allowed)
- [ ] Contrast ratio ≥ 4.5:1 for body text, ≥ 3:1 for large text (WCAG AA)
- [ ] `prefers-reduced-motion` respected, with a simplified fallback (not just "off")
- [ ] Every animation maps to one of: anticipation / confirmation / progress / transition / attention
- [ ] Only `transform`/`opacity` are animated — no layout-triggering properties
- [ ] Hover effects have a touch-device equivalent (`:active`/`:focus-visible`)
- [ ] No layout uses the three AI-default looks (cream+terracotta / near-black+neon / broadsheet hairline) unless the brief asked for it
- [ ] One signature element is identifiable and it's the boldest thing on the page
- [ ] Folder/component structure is feature-based with consistent naming, not a flat dump of files
- [ ] Design decisions trace back to the Part 0 discovery output (goal, audience, competitor gap) — not made in a vacuum
- [ ] Colors, radius, and shadows pulled from defined tokens — no one-off inline hex/shadow values
- [ ] Every interactive element handles all states: default/hover/active/focus/disabled/loading/success/error
- [ ] No placeholder class/file names (`box1`, `test`, `final-final`) anywhere in the codebase
- [ ] One `<h1>` per page, meta title/description, OG tags, and canonical URL set
- [ ] Images have explicit dimensions or `aspect-ratio` (no CLS), lazy-loaded below the fold, modern format used