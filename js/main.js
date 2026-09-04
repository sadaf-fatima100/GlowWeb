(() => {
  'use strict';

  /* =========================================================
     20-Year Veteran UI/UX Animation Expert Implementation
     ========================================================= */

  /* ---------- Theme Handling ---------- */
  const root = document.documentElement;
  const THEME_KEY = 'webagency-theme';
  const DEFAULT_THEME = root.getAttribute('data-default-theme') || 'dark';

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    document.querySelectorAll('.theme-toggle').forEach(btn => {
      btn.setAttribute('aria-pressed', theme === 'dark');
    });
  }
  
  function getStoredTheme() {
    try { return localStorage.getItem(THEME_KEY); } catch(e) { return null; }
  }
  
  function storeTheme(t) {
    try { localStorage.setItem(THEME_KEY, t); } catch(e) {}
  }

  const initialTheme = getStoredTheme() || DEFAULT_THEME;
  applyTheme(initialTheme);

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.theme-toggle');
    if (!btn) return;
    const current = root.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    storeTheme(next);
  });

  /* ---------- Page Loader ---------- */
  window.addEventListener('load', () => {
    const loader = document.querySelector('.loader');
    if (loader) {
      setTimeout(() => loader.classList.add('done'), 400);
    }
  });

  /* ---------- Mobile Drawer ---------- */
  document.addEventListener('click', (e) => {
    if (e.target.closest('.burger')) {
      document.querySelector('.mobile-drawer')?.classList.add('open');
    }
    
    // Accordion Toggle Logic
    const accordionToggle = e.target.closest('.accordion-toggle');
    if (accordionToggle) {
      e.preventDefault();
      const accordion = accordionToggle.closest('.mobile-drawer-accordion');
      if (accordion) {
        accordion.classList.toggle('open');
      }
      return; // Stop here so it doesn't close the drawer
    }

    // Close drawer on overlay click or when a standard link is clicked
    if (e.target.closest('.mobile-close') || (e.target.closest('.mobile-drawer') && e.target.tagName === 'A' && !e.target.closest('.accordion-toggle'))) {
      document.querySelector('.mobile-drawer')?.classList.remove('open');
    }
  });

  /* ---------- Magnetic Hover & LERP Damping ---------- */
  const magneticEls = document.querySelectorAll('.magnetic');
  magneticEls.forEach(el => {
    let targetX = 0, targetY = 0;
    let currentX = 0, currentY = 0;
    
    el.addEventListener('mousemove', (e) => {
      const r = el.getBoundingClientRect();
      // Calculate delta from center
      const mx = e.clientX - (r.left + r.width / 2);
      const my = e.clientY - (r.top + r.height / 2);
      // Magnetic pull factor
      targetX = mx * 0.35;
      targetY = my * 0.45;
    });

    el.addEventListener('mouseleave', () => {
      targetX = 0;
      targetY = 0;
    });

    function update() {
      // Linear interpolation (LERP) for smooth ease-back
      currentX += (targetX - currentX) * 0.12;
      currentY += (targetY - currentY) * 0.12;
      el.style.transform = `translate3d(${currentX.toFixed(2)}px, ${currentY.toFixed(2)}px, 0)`;
      requestAnimationFrame(update);
    }
    update();
  });

  /* ---------- Scroll-Triggered Reveal & Split-Text Line Wrappers ---------- */
  const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .services-circle');
  reveals.forEach((el, index) => {
    el.style.setProperty('--i', index % 6);
    
    // Automatically split headings into slide-up wrappers for high-end text reveal
    if (el.tagName === 'H1' || el.tagName === 'H2') {
      const text = el.innerHTML;
      if (!text.includes('split-line-wrapper') && !el.querySelector('em')) {
        el.innerHTML = text.split('<br>').map(line => {
          return `<span class="split-line-wrapper"><span class="split-line-child">${line}</span></span>`;
        }).join('<br>');
      }
    }
  });

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });

    reveals.forEach(el => revealObserver.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('is-in'));
  }

  /* ---------- Vanilla JS Portfolio Filtering ---------- */
  const filterPills = document.querySelectorAll('.filter-pill');
  const portCards = document.querySelectorAll('.port-card.mix');

  if (filterPills.length > 0 && portCards.length > 0) {
    const applyFilter = (filterValue) => {
      portCards.forEach(card => {
        const cardCat = card.getAttribute('data-cat');
        if (filterValue === 'all' || filterValue === cardCat) {
          card.classList.remove('mix-hidden-layout');
          requestAnimationFrame(() => {
            card.classList.remove('mix-hide');
          });
        } else {
          card.classList.add('mix-hide');
          setTimeout(() => {
            if (card.classList.contains('mix-hide')) {
              card.classList.add('mix-hidden-layout');
            }
          }, 350);
        }
      });
    };

    // Initialize with whatever pill is marked active by default (e.g. web)
    const initialActive = document.querySelector('.filter-pill.active');
    if (initialActive) {
      const initFilter = initialActive.getAttribute('data-filter') || 'web';
      applyFilter(initFilter);
    }

    filterPills.forEach(pill => {
      pill.addEventListener('click', () => {
        filterPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const filterValue = pill.getAttribute('data-filter');
        applyFilter(filterValue);
      });
    });
  }

  /* ---------- Sounding Line Scroll Progress ---------- */
  const scrollLine = document.querySelector('.sounding-line');
  if (scrollLine) {
    const fill = scrollLine.querySelector('.fill');
    const reading = scrollLine.querySelector('.reading');
    const maxScroll = 100;

    const onScroll = () => {
      const doc = document.documentElement;
      const scrolled = doc.scrollTop || document.body.scrollTop;
      const total = doc.scrollHeight - doc.clientHeight || 1;
      const pct = Math.min(1, Math.max(0, scrolled / total));
      fill.style.height = (pct * 100) + '%';
      if (reading) {
        reading.textContent = Math.round(pct * maxScroll) + '% SCROLLED';
      }
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Dynamic Header Scroll Animation ---------- */
  const header = document.querySelector('.site-header');
  if (header) {
    const handleHeaderScroll = () => {
      const isMobile = window.innerWidth <= 960;
      if (isMobile) {
        header.style.top = ''; // Clean CSS control on mobile
        return;
      }
      header.style.top = '10px';
    };
    window.addEventListener('resize', handleHeaderScroll, { passive: true });
    handleHeaderScroll();
  }

  /* ---------- Animated Statistics Counters ---------- */
  const countElements = document.querySelectorAll('[data-count]');
  if (countElements.length && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        if (el.dataset.animated) return;
        el.dataset.animated = 'true';

        const target = parseFloat(el.getAttribute('data-count'));
        const suffix = el.getAttribute('data-suffix') || '';
        const duration = 1000; // Reduced from 1800ms to 1000ms for quick counting
        const startTime = performance.now();

        function step(now) {
          const elapsed = now - startTime;
          const progress = Math.min(1, elapsed / duration);
          // Ease out cubic
          const easeProgress = 1 - Math.pow(1 - progress, 3);
          const current = Math.floor(target * easeProgress);

          el.textContent = current + suffix;
          if (progress < 1) {
            requestAnimationFrame(step);
          }
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.05 }); // Lowered from 0.3 to 0.05 to trigger instantly as it enters screen

    countElements.forEach(el => counterObserver.observe(el));
  }

  /* ---------- Card Tilt Cursor Motion ---------- */
  if (window.matchMedia('(hover:hover)').matches) {
    document.querySelectorAll('.tilt').forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        // Mouse coordinate mapping from -0.5 to 0.5
        const px = (e.clientX - r.left) / r.width - 0.5;
        const py = (e.clientY - r.top) / r.height - 0.5;
        // Damping and applying 3D rotation matrix
        card.style.transform = `perspective(1000px) rotateY(${(px * 12).toFixed(2)}deg) rotateX(${(py * -12).toFixed(2)}deg) translateY(-8px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0px)';
      });
    });

    /* ---------- Spotlight Gradient Hover effect ---------- */
    document.querySelectorAll('.spotlight-card').forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });

    /* ---------- 3D Glass Chrome Fluid Interaction ---------- */
    const viz = document.querySelector('.visualizer-container');
    if (viz) {
      const fluidChrome = viz.querySelector('.fluid-chrome');
      const fluidGlass = viz.querySelector('.fluid-glass');
      const fluidRing = viz.querySelector('.fluid-ring');
      const orbCoords = viz.querySelector('#orbCoords');
      
      let targetRx = 0, targetRy = 0;
      let currentRx = 0, currentRy = 0;
      
      viz.addEventListener('mousemove', (e) => {
        const r = viz.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - 0.5;
        const py = (e.clientY - r.top) / r.height - 0.5;
        targetRx = py * -40;
        targetRy = px * 40;
        
        if (orbCoords) {
          orbCoords.textContent = `LAT: ${(py * 90).toFixed(4)}° N | LNG: ${(px * 180).toFixed(4)}° W`;
        }
      });

      viz.addEventListener('mouseleave', () => {
        targetRx = 0;
        targetRy = 0;
        if (orbCoords) {
          orbCoords.textContent = "LAT: 34.0522° N | LNG: 118.2437° W";
        }
      });

      function updateVisualizer() {
        currentRx += (targetRx - currentRx) * 0.1;
        currentRy += (targetRy - currentRy) * 0.1;
        
        if (fluidGlass) {
          fluidGlass.style.transform = `scale(1.02) rotateX(${currentRx}deg) rotateY(${currentRy}deg)`;
        }
        if (fluidChrome) {
          fluidChrome.style.transform = `translate3d(${(currentRy * 0.5).toFixed(2)}px, ${(currentRx * 0.5).toFixed(2)}px, 0)`;
        }
        if (fluidRing) {
          fluidRing.style.transform = `rotate3d(1, 1, 0, ${(currentRx * 0.3).toFixed(2)}deg)`;
        }
        requestAnimationFrame(updateVisualizer);
      }
      updateVisualizer();
    }
  }

  /* ---------- Interactive Custom Particle Swarm Cursor ---------- */
  const oldCc = document.getElementById('customCursor');
  const oldCcf = document.getElementById('customCursorFollower');
  if (oldCc) oldCc.style.display = 'none';
  if (oldCcf) oldCcf.style.display = 'none';

  if (window.matchMedia('(min-width: 960px)').matches) {
    const canvas = document.createElement('canvas');
    canvas.id = 'cursorParticleCanvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '999999';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }, { passive: true });

    let mx = width / 2;
    let my = height / 2;
    let lastMx = mx;
    let lastMy = my;
    let smoothSpeed = 0;
    let isHovered = false;

    const particles = [];
    const particleCount = 45;

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: mx,
        y: my,
        vx: 0,
        vy: 0,
        angle: (i / particleCount) * Math.PI * 2,
        angularSpeed: 0.02 + Math.random() * 0.03,
        baseRadius: Math.random() * 6,
        scatterMultiplier: 1.2 + Math.random() * 2.8,
        ease: 0.05 + Math.random() * 0.05,
        friction: 0.82 + Math.random() * 0.06,
        size: 1.2 + Math.random() * 2.2,
        opacity: 0.35 + Math.random() * 0.5
      });
    }

    document.addEventListener('mousemove', (e) => {
      mx = e.clientX;
      my = e.clientY;
    }, { passive: true });

    function tick() {
      ctx.clearRect(0, 0, width, height);

      // Calculate instant velocity
      const dMx = mx - lastMx;
      const dMy = my - lastMy;
      const speed = Math.sqrt(dMx * dMx + dMy * dMy);
      smoothSpeed += (speed - smoothSpeed) * 0.12;

      lastMx = mx;
      lastMy = my;

      // Extract colors from CSS variables dynamically
      const docStyle = getComputedStyle(document.documentElement);
      const accent = docStyle.getPropertyValue('--accent-primary').trim() || '#2563EB';

      particles.forEach((p) => {
        // Dynamic target radius based on speed and hover state
        let targetRadius = p.baseRadius;
        let speedScatter = smoothSpeed * p.scatterMultiplier;

        if (isHovered) {
          // Hover state: assemble into a gorgeous expanding circular orbital halo
          targetRadius = 24 + Math.sin(p.angle * 2) * 4;
          speedScatter *= 0.3; // dampen scatter during hover snaps
        }

        const targetX = mx + Math.cos(p.angle) * (targetRadius + speedScatter);
        const targetY = my + Math.sin(p.angle) * (targetRadius + speedScatter);

        // Physics LERP
        p.vx += (targetX - p.x) * p.ease;
        p.vy += (targetY - p.y) * p.ease;

        p.vx *= p.friction;
        p.vy *= p.friction;

        p.x += p.vx;
        p.y += p.vy;

        // Orbit rotation speed increases slightly when hovered for high-end look
        p.angle += isHovered ? p.angularSpeed * 1.6 : p.angularSpeed;

        // Draw particle
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = accent;
        ctx.globalAlpha = p.opacity;
        ctx.shadowBlur = isHovered ? 8 : 4;
        ctx.shadowColor = accent;
        ctx.fill();
      });

      // Draw active center dot
      ctx.beginPath();
      ctx.arc(mx, my, isHovered ? 2 : 3, 0, Math.PI * 2);
      ctx.fillStyle = accent;
      ctx.globalAlpha = 0.9;
      ctx.shadowBlur = 4;
      ctx.shadowColor = accent;
      ctx.fill();

      ctx.globalAlpha = 1.0;
      ctx.shadowBlur = 0;

      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);

    // Interactive hover triggers
    const updateHoverables = () => {
      const hoverables = document.querySelectorAll('a, button, .draggable-tag, .port-card, .price-card, .webagency-accordion');
      hoverables.forEach(item => {
        // Prevent duplicate binds
        if (item.dataset.cursorBound) return;
        item.dataset.cursorBound = 'true';
        
        item.addEventListener('mouseenter', () => {
          isHovered = true;
        });
        item.addEventListener('mouseleave', () => {
          isHovered = false;
        });
      });
    };
    updateHoverables();
    
    // Periodically re-bind dynamic elements
    setInterval(updateHoverables, 2000);
  }

  /* ---------- Constellation Canvas Background Animation ---------- */
  class ParticleConstellation {
    constructor(canvasId, colorVar, lineOpacity = 0.08) {
      this.canvas = document.getElementById(canvasId);
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.colorVar = colorVar;
      this.lineOpacity = lineOpacity;
      this.particles = [];
      this.numberOfParticles = 45;
      this.mouse = { x: null, y: null, radius: 130 };

      this.init();
      this.setupEvents();
      this.animate();
    }

    init() {
      this.resize();
      this.particles = [];
      for (let i = 0; i < this.numberOfParticles; i++) {
        this.particles.push({
          x: Math.random() * this.canvas.width,
          y: Math.random() * this.canvas.height,
          vx: (Math.random() - 0.5) * 0.6,
          vy: (Math.random() - 0.5) * 0.6,
          size: Math.random() * 2 + 1.5
        });
      }
    }

    resize() {
      const rect = this.canvas.parentElement.getBoundingClientRect();
      this.canvas.width = rect.width;
      this.canvas.height = rect.height;
    }

    setupEvents() {
      window.addEventListener('resize', () => this.resize());
      this.canvas.parentElement.addEventListener('mousemove', (e) => {
        const rect = this.canvas.getBoundingClientRect();
        this.mouse.x = e.clientX - rect.left;
        this.mouse.y = e.clientY - rect.top;
      });
      this.canvas.parentElement.addEventListener('mouseleave', () => {
        this.mouse.x = null;
        this.mouse.y = null;
      });
    }

    animate() {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      const styles = getComputedStyle(document.documentElement);
      const baseColor = styles.getPropertyValue(this.colorVar).trim();
      
      // Parse Hex or RGB into values
      let rgb = "46, 61, 35";
      if (baseColor.startsWith('#')) {
        const hex = baseColor.slice(1);
        const r = parseInt(hex.substring(0, 2), 16);
        const g = parseInt(hex.substring(2, 4), 16);
        const b = parseInt(hex.substring(4, 6), 16);
        rgb = `${r}, ${g}, ${b}`;
      } else if (baseColor.startsWith('rgb')) {
        const match = baseColor.match(/\d+/g);
        if (match && match.length >= 3) {
          rgb = `${match[0]}, ${match[1]}, ${match[2]}`;
        }
      }

      this.particles.forEach((p, idx) => {
        // Move particle
        p.x += p.vx;
        p.y += p.vy;

        // Bounce walls
        if (p.x < 0 || p.x > this.canvas.width) p.vx *= -1;
        if (p.y < 0 || p.y > this.canvas.height) p.vy *= -1;

        // Interactive cursor gravity pull
        if (this.mouse.x !== null && this.mouse.y !== null) {
          const dx = this.mouse.x - p.x;
          const dy = this.mouse.y - p.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < this.mouse.radius) {
            const force = (this.mouse.radius - dist) / this.mouse.radius;
            p.x -= dx * force * 0.02;
            p.y -= dy * force * 0.02;
          }
        }

        // Draw dot
        this.ctx.fillStyle = `rgba(${rgb}, 0.16)`;
        this.ctx.beginPath();
        this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        this.ctx.fill();

        // Connect lines
        for (let j = idx + 1; j < this.particles.length; j++) {
          const p2 = this.particles[j];
          const dx = p.x - p2.x;
          const dy = p.y - p2.y;
          const distance = Math.sqrt(dx * dx + dy * dy);

          if (distance < 110) {
            const opacity = (1 - (distance / 110)) * this.lineOpacity;
            this.ctx.strokeStyle = `rgba(${rgb}, ${opacity})`;
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            this.ctx.moveTo(p.x, p.y);
            this.ctx.lineTo(p2.x, p2.y);
            this.ctx.stroke();
          }
        }
      });

      requestAnimationFrame(() => this.animate());
    }
  }

  new ParticleConstellation('heroCanvas', '--accent-primary', 0.1);
  new ParticleConstellation('contactCanvas', '--accent-primary', 0.08);

  /* ---------- Bubble Basin Capabilities — Production Grade ---------- */
  class BubbleBasin {
    constructor(viewportId) {
      this.viewport = document.getElementById(viewportId);
      if (!this.viewport) return;

      this.phrases = [
        'Web Development',
        'SEO Optimization',
        'Google Ads',
        'UI/UX Design',
        'Brand Strategy',
        'Digital Marketing',
        'ROI Focus',
        'Custom Design',
        '🚀',
        '👍',
        '🎯',
        '💡',
        '🔒',
        '⚡'
      ];

      this.bubbles = [];
      this.droplets = [];
      this.active = false;
      this.waveReady = false;   // True once all bubbles settled
      this.respawnTimer = null;

      // Bind animation loop
      this._animate = this._animate.bind(this);
      this._raf = requestAnimationFrame(this._animate);

      this._initObserver();
    }

    /* --- Intersection Observer: activate when viewport is in view --- */
    _initObserver() {
      const io = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting && !this.active) {
            this.active = true;
            this._spawnWave();
          }
          if (!e.isIntersecting) {
            this.active = false;
            this._clearAll();
          }
        });
      }, { threshold: 0.15 });
      io.observe(this.viewport);
    }

    /* --- Get viewport dimensions safely --- */
    _dims() {
      const r = this.viewport.getBoundingClientRect();
      return {
        w: r.width > 100 ? r.width : (this.viewport.clientWidth || window.innerWidth),
        h: r.height > 100 ? r.height : 440
      };
    }

    /* --- Spawn a full wave of bubbles (all 14 shuffled, staggered) --- */
    _spawnWave() {
      if (!this.active) return;
      // Shuffle indices so text & emoji bubbles are mixed
      const indices = this.phrases.map((_, i) => i);
      for (let i = indices.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [indices[i], indices[j]] = [indices[j], indices[i]];
      }
      indices.forEach((phraseIdx, spawnOrder) => {
        setTimeout(() => {
          if (this.active) this._createBubble(phraseIdx, spawnOrder);
        }, spawnOrder * 280);
      });
    }

    /* --- Create a single bubble --- */
    _createBubble(idx, spawnOrder) {
      const { w, h } = this._dims();
      const text = this.phrases[idx];

      // Measure text to determine dynamic circle size
      const charLen = text.length;
      const isEmoji = charLen <= 2;
      const size = isEmoji ? 75 : Math.max(85, Math.min(130, charLen * 7 + 20));

      // DOM creation
      const el = document.createElement('div');
      el.className = `water-bubble cap-bubble-${idx}`;
      el.style.width = size + 'px';
      el.style.height = size + 'px';

      const txtEl = document.createElement('div');
      txtEl.className = 'water-bubble-text' + (isEmoji ? ' bubble-emoji' : '');
      txtEl.innerText = text;
      el.appendChild(txtEl);
      this.viewport.appendChild(el);

      // Alternate left/right based on spawn order (mixed)
      const fromLeft = spawnOrder % 2 === 0;

      // Target: accumulate in the middle band (Y: 30%–70% of viewport height)
      const midBandTop = h * 0.25;
      const midBandBottom = h * 0.65;
      const targetY = midBandTop + Math.random() * (midBandBottom - midBandTop);

      // Target X: spread evenly across viewport width with jitter
      const slotWidth = (w - size) / (this.phrases.length);
      const targetX = slotWidth * spawnOrder + Math.random() * slotWidth * 0.5 + size * 0.3;

      // Starting position: off-screen left or right, at bottom half
      const startX = fromLeft ? -size - 30 : w + 30;
      const startY = h * 0.5 + Math.random() * (h * 0.35);

      // Set initial position instantly so there's no flash at (0,0)
      el.style.transform = `translate3d(${startX}px, ${startY}px, 0)`;

      // Fade in
      requestAnimationFrame(() => {
        el.style.transition = 'opacity 0.6s ease';
        el.style.opacity = '1';
      });

      const bubble = {
        el,
        idx,
        size,
        // Current position
        x: startX,
        y: startY,
        // Target resting position
        tx: targetX,
        ty: targetY,
        // Movement phase: 'entering' -> 'settled'
        phase: 'entering',
        // Gentle sway params (for when settled)
        swayAngle: Math.random() * Math.PI * 2,
        swaySpeed: 0.008 + Math.random() * 0.006,
        swayRadius: 3 + Math.random() * 5,
        // Easing speed (lower = smoother/slower) 
        ease: 0.012 + Math.random() * 0.008,
        popped: false
      };

      // Pop on hover or click
      const handler = () => this._popBubble(bubble);
      el.addEventListener('mouseenter', handler);
      el.addEventListener('click', handler);

      this.bubbles.push(bubble);
    }

    /* --- Pop a bubble with splash effect --- */
    _popBubble(bubble) {
      if (bubble.popped) return;
      bubble.popped = true;

      const cx = bubble.x + bubble.size / 2;
      const cy = bubble.y + bubble.size / 2;

      // Burst scale-up + fade
      bubble.el.style.transition = 'transform 0.3s cubic-bezier(0.175,0.885,0.32,1.275), opacity 0.3s ease';
      bubble.el.style.transform = `translate3d(${bubble.x}px, ${bubble.y}px, 0) scale(1.2)`;
      bubble.el.style.opacity = '0';

      // Splash droplets
      const colorMap = [
        '#6F5CF2', '#4FEBFD', '#F4C430', '#39D353',
        '#FF5A79', '#50E3C2', '#FF8E53', '#E3E7FD',
        '#FF6B6B', '#845EF7', '#20C997', '#FCC419',
        '#339AF0', '#F06595'
      ];
      const color = colorMap[bubble.idx] || '#6F5CF2';
      const numDroplets = 10 + Math.floor(Math.random() * 5);

      for (let i = 0; i < numDroplets; i++) {
        const dEl = document.createElement('div');
        dEl.className = 'bubble-droplet';
        dEl.style.backgroundColor = color;
        this.viewport.appendChild(dEl);

        const angle = (i / numDroplets) * Math.PI * 2 + Math.random() * 0.4;
        const speed = 1.5 + Math.random() * 3;

        this.droplets.push({
          el: dEl,
          x: cx, y: cy,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 1.2,
          opacity: 1,
          life: 30 + Math.random() * 20
        });
      }

      // Remove DOM after animation
      setTimeout(() => {
        if (bubble.el.parentNode) bubble.el.parentNode.removeChild(bubble.el);
      }, 320);

      // Remove from array
      const i = this.bubbles.indexOf(bubble);
      if (i !== -1) this.bubbles.splice(i, 1);

      // Check if all bubbles are popped -> schedule next wave
      if (this.bubbles.length === 0 && this.active) {
        clearTimeout(this.respawnTimer);
        this.respawnTimer = setTimeout(() => {
          if (this.active) this._spawnWave();
        }, 900); // Short pause before new wave
      }
    }

    /* --- Animation loop --- */
    _animate() {
      // Move bubbles toward their target (lerp/easing)
      for (let i = this.bubbles.length - 1; i >= 0; i--) {
        const b = this.bubbles[i];
        if (b.popped) continue;

        if (b.phase === 'entering') {
          // Smooth lerp toward target
          b.x += (b.tx - b.x) * b.ease;
          b.y += (b.ty - b.y) * b.ease;

          // Check if close enough to target to settle
          const dx = Math.abs(b.tx - b.x);
          const dy = Math.abs(b.ty - b.y);
          if (dx < 1.5 && dy < 1.5) {
            b.x = b.tx;
            b.y = b.ty;
            b.phase = 'settled';
          }
        }

        // Gentle sway even while entering (organic feel)
        b.swayAngle += b.swaySpeed;
        const swayX = Math.sin(b.swayAngle) * b.swayRadius;
        const swayY = Math.cos(b.swayAngle * 0.7) * (b.swayRadius * 0.4);

        const displayX = b.x + swayX;
        const displayY = b.y + swayY;

        b.el.style.transform = `translate3d(${displayX}px, ${displayY}px, 0)`;
      }

      // Update droplets
      for (let i = this.droplets.length - 1; i >= 0; i--) {
        const d = this.droplets[i];
        d.x += d.vx;
        d.y += d.vy;
        d.vy += 0.12; // Gravity
        d.opacity -= 1 / d.life;

        if (d.opacity <= 0) {
          if (d.el.parentNode) d.el.parentNode.removeChild(d.el);
          this.droplets.splice(i, 1);
        } else {
          d.el.style.transform = `translate3d(${d.x}px, ${d.y}px, 0)`;
          d.el.style.opacity = d.opacity;
        }
      }

      this._raf = requestAnimationFrame(this._animate);
    }

    /* --- Clear everything (when section leaves view) --- */
    _clearAll() {
      clearTimeout(this.respawnTimer);
      this.bubbles.forEach(b => {
        if (b.el.parentNode) b.el.parentNode.removeChild(b.el);
      });
      this.droplets.forEach(d => {
        if (d.el.parentNode) d.el.parentNode.removeChild(d.el);
      });
      this.bubbles = [];
      this.droplets = [];
    }

    destroy() {
      this.active = false;
      this._clearAll();
      cancelAnimationFrame(this._raf);
    }
  }

  // Initialize Bubble Basin on window load
  window.addEventListener('load', () => {
    new BubbleBasin('bubbleViewport');
  });


  /* ---------- Contact form submit simulation ---------- */
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      
      btn.textContent = 'Sending message...';
      btn.disabled = true;

      setTimeout(() => {
        btn.textContent = 'Message Sent Successfully!';
        btn.style.background = 'var(--accent-neon-green)';
        btn.style.color = '#000';
        
        setTimeout(() => {
          btn.textContent = originalText;
          btn.style.background = '';
          btn.style.color = '';
          btn.disabled = false;
          contactForm.reset();
        }, 2200);
      }, 1500);
    });
  }

  /* ---------- Interactive Expertise Slider ---------- */
  const textSlides = document.querySelectorAll('.expertise-slide-text-item');
  const graphics = document.querySelectorAll('.expertise-graphic-item');
  const navBtns = document.querySelectorAll('.expertise-nav-btn');
  
  if (textSlides.length && graphics.length && navBtns.length) {
    let activeIndex = 0;
    let progressInterval = null;
    let elapsed = 0;
    const duration = 3500; // 3.5s per slide on desktop
    const intervalTick = 50; // check progress every 50ms
    
    const isMobileView = () => window.innerWidth <= 991;

    const showSlide = (index) => {
      activeIndex = index;
      elapsed = 0;
      
      // Update Active Classes
      textSlides.forEach((slide, i) => {
        slide.classList.toggle('active', i === index);
      });
      graphics.forEach((graphic, i) => {
        graphic.classList.toggle('active', i === index);
      });
      navBtns.forEach((btn, i) => {
        btn.classList.toggle('active', i === index);
        const fill = btn.querySelector('.expertise-nav-progress-fill');
        if (fill) fill.style.width = '0%';
      });
    };
    
    const startProgress = () => {
      if (progressInterval) {
        clearInterval(progressInterval);
        progressInterval = null;
      }
      
      // Never auto-advance on mobile — mobile users read at their own pace via manual tap tabs
      if (isMobileView()) {
        return;
      }
      
      progressInterval = setInterval(() => {
        if (isMobileView()) {
          clearInterval(progressInterval);
          progressInterval = null;
          return;
        }

        elapsed += intervalTick;
        const percentage = Math.min(100, (elapsed / duration) * 100);
        
        const activeBtn = navBtns[activeIndex];
        if (activeBtn) {
          const fill = activeBtn.querySelector('.expertise-nav-progress-fill');
          if (fill) fill.style.width = percentage + '%';
        }
        
        if (elapsed >= duration) {
          const nextIndex = (activeIndex + 1) % textSlides.length;
          showSlide(nextIndex);
        }
      }, intervalTick);
    };
    
    // Bind click events to nav buttons
    navBtns.forEach((btn, index) => {
      btn.addEventListener('click', () => {
        showSlide(index);
        startProgress();
      });
    });

    // Window resize handler
    window.addEventListener('resize', () => {
      if (isMobileView()) {
        if (progressInterval) {
          clearInterval(progressInterval);
          progressInterval = null;
        }
        navBtns.forEach(btn => {
          const fill = btn.querySelector('.expertise-nav-progress-fill');
          if (fill) fill.style.width = '0%';
        });
      } else {
        if (!progressInterval) {
          startProgress();
        }
      }
    }, { passive: true });

    // Global method to switch slides from external cards/buttons
    window.goToExpertiseSlide = (index) => {
      showSlide(index);
      startProgress();
      const el = document.getElementById('expertiseSection');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    };

    // Initialize
    showSlide(0);
    startProgress();
  }

  /* ---------- Automatic Horizontal Scroll Carousel with Hover Pause ---------- */
  const carousel = document.querySelector('.project-scroll-container');
  if (carousel) {
    let scrollInterval;
    const intervalTime = 2500; // Scrolls every 2.5 seconds (maximum 3 seconds)

    const getScrollStep = () => {
      const firstSlide = carousel.querySelector('.project-carousel-slide');
      if (firstSlide) {
        return firstSlide.getBoundingClientRect().width + 30; // Slide width + gap
      }
      return 380;
    };

    const handleAutoScroll = () => {
      const maxScroll = carousel.scrollWidth - carousel.clientWidth;
      if (carousel.scrollLeft >= maxScroll - 15) {
        carousel.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        carousel.scrollBy({ left: getScrollStep(), behavior: 'smooth' });
      }
    };

    const startScroll = () => {
      clearInterval(scrollInterval);
      scrollInterval = setInterval(handleAutoScroll, intervalTime);
    };

    const stopScroll = () => {
      clearInterval(scrollInterval);
    };

    // Start auto-scrolling on initialization
    startScroll();

    // Event listeners to pause auto-scrolling when user hovers
    carousel.addEventListener('mouseenter', stopScroll);
    carousel.addEventListener('mouseleave', startScroll);

    // Support touch devices (pause during finger swipe, resume on release)
    carousel.addEventListener('touchstart', stopScroll, { passive: true });
    carousel.addEventListener('touchend', startScroll, { passive: true });
  }

  /* ---------- Universal Global Accordion Toggler ---------- */
  window.toggleAcc = function(el) {
    const wrapper = el.closest('.webagency-accordion-wrapper');
    if (!wrapper) return;
    const content = wrapper.querySelector('.webagency-accordion-content');
    const svg = el.querySelector('svg');
    const allWrappers = document.querySelectorAll('.webagency-accordion-wrapper');
    const allContents = document.querySelectorAll('.webagency-accordion-content');
    const allSvgs = document.querySelectorAll('.webagency-accordion-header svg');

    const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';

    allContents.forEach(c => { c.style.maxHeight = '0px'; });
    allSvgs.forEach(s => { s.style.transform = 'rotate(0deg)'; });
    allWrappers.forEach(w => { w.classList.remove('is-open'); });

    if (!isOpen) {
      content.style.maxHeight = (content.scrollHeight + 16) + 'px';
      if (svg) svg.style.transform = 'rotate(180deg)';
      wrapper.classList.add('is-open');
    }
  };

  /* =========================================================
     Universal Portfolio Fancybox / Lightbox Modal System
     100% Centered, Fully Responsive, Keyboard & Touch Enabled
     ========================================================= */
  (function initPortfolioFancybox() {
    let fancyboxEl = null;
    let currentGallery = [];
    let currentIndex = 0;
    let touchStartX = 0;
    let touchEndX = 0;

    function createFancyboxDOM() {
      const existing = document.getElementById('portfolioFancybox');
      if (existing) return existing;

      const el = document.createElement('div');
      el.id = 'portfolioFancybox';
      el.className = 'portfolio-fancybox';
      el.setAttribute('aria-hidden', 'true');
      el.setAttribute('role', 'dialog');
      el.setAttribute('aria-modal', 'true');
      el.setAttribute('aria-label', 'Portfolio Image Lightbox');

      el.innerHTML = `
        <div class="fancybox-backdrop"></div>
        <div class="fancybox-wrapper">
          <button class="fancybox-btn fancybox-close" type="button" aria-label="Close Lightbox" title="Close (Esc)">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
          <button class="fancybox-btn fancybox-prev" type="button" aria-label="Previous image" title="Previous (Left Arrow)">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="15 18 9 12 15 6"></polyline>
            </svg>
          </button>
          <button class="fancybox-btn fancybox-next" type="button" aria-label="Next image" title="Next (Right Arrow)">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
          <div class="fancybox-container">
            <div class="fancybox-media-wrap">
              <div class="fancybox-spinner"></div>
              <img class="fancybox-img" src="" alt="Portfolio Preview" />
            </div>
          </div>
        </div>
      `;

      document.body.appendChild(el);
      return el;
    }

    function getActiveItems(clickedCard) {
      if (clickedCard && clickedCard.closest('.stacked-gallery-container')) {
        return Array.from(document.querySelectorAll('.stacked-gallery-container .stacked-card'));
      }
      // On portfolio.html with .port-card
      const portCards = document.querySelectorAll('.portfolio-grid .port-card, #portfolioGrid .port-card');
      if (portCards.length > 0) {
        const visible = Array.from(portCards).filter(c => !c.classList.contains('mix-hide') && !c.classList.contains('mix-hidden-layout') && c.offsetParent !== null);
        return visible.length > 0 ? visible : Array.from(portCards);
      }
      // On index.html with .portfolio-item
      const portItems = document.querySelectorAll('.portfolio-grid .portfolio-item');
      if (portItems.length > 0) {
        const visible = Array.from(portItems).filter(item => item.classList.contains('active') && item.offsetParent !== null);
        return visible.length > 0 ? visible : Array.from(portItems);
      }
      return Array.from(document.querySelectorAll('.portfolio-item, .port-card, .stacked-card'));
    }

    function extractItemData(card) {
      const img = card.querySelector('img');
      const src = img ? (img.currentSrc || img.getAttribute('src') || '') : '';
      const alt = img ? (img.getAttribute('alt') || '') : 'Portfolio Preview';
      return { src, alt };
    }

    function renderSlide(index) {
      if (!currentGallery.length) return;
      if (index < 0) index = currentGallery.length - 1;
      if (index >= currentGallery.length) index = 0;
      currentIndex = index;

      const item = currentGallery[currentIndex];
      const img = fancyboxEl.querySelector('.fancybox-img');
      const spinner = fancyboxEl.querySelector('.fancybox-spinner');
      const prevBtn = fancyboxEl.querySelector('.fancybox-prev');
      const nextBtn = fancyboxEl.querySelector('.fancybox-next');

      if (currentGallery.length <= 1) {
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
      } else {
        prevBtn.style.display = 'flex';
        nextBtn.style.display = 'flex';
      }

      img.classList.add('is-loading');
      spinner.classList.add('is-active');

      const tempImg = new Image();
      tempImg.onload = () => {
        img.src = item.src;
        img.alt = item.alt;
        img.classList.remove('is-loading');
        spinner.classList.remove('is-active');
      };
      tempImg.onerror = () => {
        img.src = item.src;
        img.classList.remove('is-loading');
        spinner.classList.remove('is-active');
      };
      tempImg.src = item.src;
    }

    function openFancybox(card) {
      fancyboxEl = createFancyboxDOM();
      const items = getActiveItems(card);
      currentGallery = items.map(extractItemData).filter(d => !!d.src);

      const clickedImg = card.querySelector('img');
      const clickedSrc = clickedImg ? (clickedImg.currentSrc || clickedImg.getAttribute('src')) : '';
      let foundIndex = currentGallery.findIndex(d => d.src === clickedSrc);
      if (foundIndex === -1) foundIndex = 0;

      renderSlide(foundIndex);

      fancyboxEl.classList.add('is-open');
      fancyboxEl.setAttribute('aria-hidden', 'false');
      document.body.classList.add('fancybox-open');
    }

    function closeFancybox() {
      if (!fancyboxEl) return;
      fancyboxEl.classList.remove('is-open');
      fancyboxEl.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('fancybox-open');
    }

    // Delegated click listener for any portfolio item
    document.addEventListener('click', (e) => {
      const card = e.target.closest('.portfolio-item, .port-card, .stacked-card, .project-carousel-frame, .port-frame');
      if (card && !e.target.closest('.portfolio-fancybox')) {
        const targetCard = card.closest('.portfolio-item, .port-card, .stacked-card') || card;
        e.preventDefault();
        openFancybox(targetCard);
        return;
      }

      // Close button or backdrop click
      if (e.target.closest('.fancybox-close') || e.target.classList.contains('fancybox-backdrop') || e.target.classList.contains('fancybox-wrapper')) {
        closeFancybox();
        return;
      }

      // Prev / Next button click
      if (e.target.closest('.fancybox-prev')) {
        e.stopPropagation();
        renderSlide(currentIndex - 1);
        return;
      }
      if (e.target.closest('.fancybox-next')) {
        e.stopPropagation();
        renderSlide(currentIndex + 1);
        return;
      }
    });

    // Keyboard navigation (Escape, ArrowLeft, ArrowRight)
    document.addEventListener('keydown', (e) => {
      if (!fancyboxEl || !fancyboxEl.classList.contains('is-open')) return;
      if (e.key === 'Escape') {
        closeFancybox();
      } else if (e.key === 'ArrowLeft') {
        renderSlide(currentIndex - 1);
      } else if (e.key === 'ArrowRight') {
        renderSlide(currentIndex + 1);
      }
    });

    // Touch swipe gestures for mobile devices
    document.addEventListener('touchstart', (e) => {
      if (!fancyboxEl || !fancyboxEl.classList.contains('is-open')) return;
      if (e.touches && e.touches.length) {
        touchStartX = e.touches[0].screenX;
      }
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      if (!fancyboxEl || !fancyboxEl.classList.contains('is-open')) return;
      if (e.changedTouches && e.changedTouches.length) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }
    }, { passive: true });

    function handleSwipe() {
      const diff = touchEndX - touchStartX;
      if (Math.abs(diff) > 40) {
        if (diff < 0) {
          renderSlide(currentIndex + 1); // Swipe left -> next
        } else {
          renderSlide(currentIndex - 1); // Swipe right -> prev
        }
      }
    }
  })();

})();

