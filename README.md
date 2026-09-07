# GlowWeb — Premium Web Agency Platform

[![Theme](https://img.shields.io/badge/Theme-Dark%20%7C%20Light-00d98f?style=flat-square)](#dual-theme-engine)
[![Responsive](https://img.shields.io/badge/Design-100%25%20Responsive-blue?style=flat-square)](#responsive-engineering)
[![Typography](https://img.shields.io/badge/Typography-Outfit%20%2B%20Plus%20Jakarta%20Sans-emerald?style=flat-square)](#typography-system)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=flat-square)](#)

A modern, high-performance web agency and digital services platform crafted with cutting-edge UI/UX aesthetics, an emerald neon design system, interactive micro-animations, and full responsive support across all device viewports.

---

## 🌟 Key Features

### 🌓 Dual-Theme Engine (Dark & Light Modes)
- **High-Contrast Dark Mode:** Deep obsidian surfaces (`#060a08`) accented by glowing emerald green (`#00d98f`) and cyan highlights (`#4febfd`).
- **Clean Light Mode:** Crisp, warm neutral backgrounds (`#f4f7f5`) with deep forest green accents (`#008f58`) for maximum daylight readability.
- **Instant Toggle & Persistence:** Reactive theme switch knob in the navbar with automatic state persistence via `localStorage`.

### 📐 Master Typography & Hierarchy
- **Display Headings:** **Outfit** (Weights 700 / 800) with tight tracking (`-0.02em` to `-0.038em`) and strict multi-tier fluid responsiveness (`clamp()`).
- **Body & Subtitles:** **Plus Jakarta Sans** (Weights 400 / 500 / 600) with balanced line-heights (`1.6`–`1.68`) and inverted-pyramid responsive spans.
- **Technical Badges:** **JetBrains Mono** with wide letter-tracking (`0.08em`–`0.12em`) for technical micro-labels and section numbering (`01 / Direct Studio`, etc.).

### 📱 Responsive Engineering
- Rigorously tested across 6 device viewports:
  - Large Desktop ($\ge 1441\text{px}$)
  - Standard Desktop / Laptop ($1025\text{px} - 1440\text{px}$)
  - Small Laptop / Tablet Landscape ($769\text{px} - 1024\text{px}$)
  - Tablet Portrait ($481\text{px} - 768\text{px}$)
  - Mobile ($321\text{px} - 480\text{px}$)
  - Small Mobile ($\le 320\text{px}$)
- Mobile drawer navigation with accordion sub-menus, smooth backdrop-filter blur, and quick contact details.

### ✨ Interactive UI & Micro-Animations
- **Reactive Custom Cursor:** Dual-layer magnetic cursor follower with acceleration smoothing.
- **Soundline Scroll Indicator:** Vertical interactive rail displaying current reading percentage.
- **Isometric Geometric Wireframe Blocks:** Dynamic SVG geometry illustrating technical innovation.
- **Continuous Marquee Testimonials:** Dual-row infinite horizontal review cards featuring real executive portrait photography and verified Google review badges.
- **Floating Quick Connect Bar:** Fixed bottom corner interactive actions — WhatsApp live chat with unread message counter badge + one-touch direct phone call.

---

## 🗂 Project Architecture

```text
GlowWeb/
├── .gitignore                      # Standard production gitignore
├── README.md                       # Comprehensive project documentation
├── favicon.svg                     # High-resolution vector favicon
├── webagency_hero_team.jpg         # Hero & OpenGraph showcase visual
│
├── index.html                      # Home Page (Services, Bento, Portfolio, Reviews)
├── about.html                      # About Us (Story, Philosophy, Leadership, Culture)
├── services.html                   # Core Services Hub & Pricing Packages
├── web-development.html            # Web Development Specialization Page
├── google-ads.html                 # Google Ads & PPC Acquisition Page
├── search-engine-optimization.html # Technical & Organic SEO Specialization Page
├── portfolio.html                  # Filterable Agency Case Studies & Work
├── blog.html                       # Searchable & Filterable Insights Hub
├── blog-post.html                  # Editorial Article Template
├── contact.html                    # Studio Map, Quick Info Ticker & Project Inquiry Form
├── cart.html                       # Shopping Cart & Checkout Interface
│
├── css/
│   └── style.css                   # Master Design System (Tokens, Themes, Breakpoints, Animations)
│
├── js/
│   ├── main.js                     # Global Navigation, Theme Engine, Animations & Scroll Triggers
│   └── blog-data.js                # Dynamic Article Repository, Category Filters & Search Index
│
└── images/
    ├── avatars/                    # Executive testimonial portrait photography (avatar-1 to 8)
    ├── about-meeting-1.jpg         # Team collaboration photography
    ├── about-meeting-2.jpg         # Strategy & planning photography
    ├── about-meeting-3.jpg         # Executive review photography
    ├── about_hero_left.jpg         # About page hero showcase image
    ├── cta-person-illustration.png # Modern 3D specialist illustration for CTA banners
    ├── google-ads-hero.png         # PPC campaign dashboard illustration
    ├── seo-hero.png                # Organic traffic growth chart illustration
    ├── web-dev-hero.png            # Web engineering UI mockup illustration
    ├── hero-1.png                  # Showcase slide visual 1
    ├── hero-2.png                  # Showcase slide visual 2
    ├── hero-3.png                  # Showcase slide visual 3
    ├── services-bg.png             # Subtle ambient texture background
    └── services_hero_img_final.png # Services header showcase composition
```

---

## 📄 Pages Overview

| Page | Filename | Description |
| :--- | :--- | :--- |
| **Home** | [`index.html`](index.html) | Agency presentation, interactive circuit hub, core services bento, portfolio marquee, verified client reviews. |
| **About Us** | [`about.html`](about.html) | Agency story, leadership pillars, company values, meeting galleries, and culture. |
| **Services** | [`services.html`](services.html) | Comprehensive capabilities breakdown, tiered agency pricing plans, and deliverable scopes. |
| **Web Dev** | [`web-development.html`](web-development.html) | Dedicated engineering service page: architecture, frameworks, and performance audits. |
| **Google Ads** | [`google-ads.html`](google-ads.html) | PPC acquisition: ROAS scaling, audience targeting, search & display campaign strategy. |
| **SEO** | [`search-engine-optimization.html`](search-engine-optimization.html) | Organic growth: technical SEO audits, keyword dominance, and content architecture. |
| **Portfolio** | [`portfolio.html`](portfolio.html) | Filterable showcase of client case studies with category switching and live impact metrics. |
| **Blog** | [`blog.html`](blog.html) | Real-time category filtering (Web, SEO, Ads), live search bar, and featured insights. |
| **Blog Post** | [`blog-post.html`](blog-post.html) | Clean editorial reading experience with author profiles, share actions, and related articles. |
| **Contact** | [`contact.html`](contact.html) | Direct studio Google map embed, live contact info marquee ticker, and validated project inquiry brief. |
| **Cart** | [`cart.html`](cart.html) | Service package summary, transparent tier pricing, and instant checkout flow. |

---

## 🎨 Design System & Color Tokens

| Token | Light Theme | Dark Theme | Purpose |
| :--- | :--- | :--- | :--- |
| `--bg` | `#f4f7f5` | `#060a08` | Primary canvas background |
| `--bg-2` | `#e6efe9` | `#0a0f0d` | Elevated containers & card surfaces |
| `--fg` | `#0a1a10` | `#ffffff` | High-contrast heading text |
| `--fg-soft` | `#4a5c50` | `rgba(255, 255, 255, 0.88)` | Subtitles, descriptions, body copy |
| `--accent-primary` | `#00d98f` | `#00d98f` | Emerald brand accent & interactive buttons |
| `--border` | `rgba(0, 217, 143, 0.08)` | `rgba(255, 255, 255, 0.05)` | Card borders & dividers |
| `--border-strong` | `rgba(0, 217, 143, 0.16)` | `rgba(255, 255, 255, 0.10)` | Prominent container borders |

---

## 🚀 Quick Start & Local Preview

No complex build steps, package installations, or external dependencies are required. The project runs directly in modern browsers.

### Option 1: Live Server (VS Code)
1. Open the project folder in VS Code.
2. Right-click [`index.html`](index.html) and select **"Open with Live Server"**.

### Option 2: Python Local HTTP Server
```bash
# In the project directory:
python -m http.server 8000
```
Then visit `http://localhost:8000` in your web browser.

### Option 3: Direct Browser Launch
Double-click any `.html` file (e.g., `index.html`) to open it directly in Chrome, Edge, Safari, or Firefox.

---

## 🌐 Browser Support

- **Google Chrome** (v90+)
- **Mozilla Firefox** (v88+)
- **Apple Safari** (v14+)
- **Microsoft Edge** (v90+)
- Full mobile browser support (iOS Safari, Chrome for Android).

---

## 📄 License

Created for **GlowWeb / Web Agency**. All rights reserved. Designed & developed for exceptional digital performance.
