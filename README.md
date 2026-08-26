# Fathom & Co. — Website Build

## Structure
```
index.html       Home
about.html       About Us
services.html    Services + Pricing
portfolio.html   Portfolio (filterable)
blog.html        Blog listing
contact.html     Contact + form
css/style.css    Design system (tokens, layout, components, animations)
js/main.js       Theme toggle, scroll-reveal, counters, filters, nav
images/          Drop real photography here (see note below)
```

## Theme
This build has a full light/dark toggle (top-right of the nav, persists via localStorage).
This specific folder defaults to: **light** on first visit.
The companion zip has the same site defaulting to the opposite theme — everything else is identical.

## Images
All visuals in this build are hand-built SVG/CSS graphics (line diagrams, gauges, gradients) rather than
stock photography, since no external image assets were available while building. Drop real photos into
/images and swap them into the marked `<svg>` placeholder blocks (in the About, Home, and Services sections)
whenever you're ready — the layout, aspect ratios, and rounded frames are already sized for it.

## Content notes
Services (Web Development, SEO, Google Ads) and the three pricing tiers are carried over as requested.
Exact pricing numbers were not visible in the reference screenshots, so representative tier pricing was
added — update the numbers in services.html and index.html (search for "price-card") to match your real rates.

## Opening the site
Just open index.html in a browser — no build step or server required.
