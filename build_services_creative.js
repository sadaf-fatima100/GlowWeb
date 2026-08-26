const fs = require('fs');
const path = require('path');

const projectDir = 'd:\\workspace\\hywiz-tasks\\m01\\projects\\2nd website';
const indexHtml = fs.readFileSync(path.join(projectDir, 'index.html'), 'utf8');
const headEnd = indexHtml.indexOf('<!-- WEB AGENCY HERO SECTION -->');
const head = indexHtml.substring(0, headEnd);

const servicesContent = `
<!-- SERVICES CREATIVE HERO -->
<section class="services-hero-creative">
  <div class="glow-orb"></div>
  <div class="wrap services-hero-grid">
    <div class="hero-content">
      <!-- Standard eyebrow pill to replace the hero badge -->
      <div class="eyebrow" style="margin-top: 40px; margin-bottom: 24px;">Premium Agency Services</div>
      <div class="webagency-heading-wrap">
        <h1 class="webagency-heading photo-heading">
          <span class="heading-top">Elevate Your Digital Presence</span>
          <span class="heading-sub">Crafting Exceptional Websites &amp; Driving Digital Success</span>
        </h1>
      </div>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-primary">Start Your Project</a>
        <a href="#services" class="btn btn-ghost">Explore Services</a>
      </div>
    </div>
    
    <div class="hero-image-creative" style="height: 100%; min-height: 500px; display: flex; align-items: stretch; position: relative; margin-top: 60px;">
      <!-- Floating tags overlay -->
      <div class="webagency-floating-tags-container" style="position: absolute; top: 30px; left: -30px; z-index: 5;">
        <div class="webagency-floating-tag tag-1">
          Premium Design
        </div>
        <div class="webagency-floating-tag tag-2" style="margin-top: 12px; margin-left: 40px;">
          SEO Optimization
        </div>
      </div>
      
      <!-- Bottom Left Floating Square -->
      <div class="webagency-floating-square" style="position: absolute; bottom: 60px; left: -50px; z-index: 6;">
        <div class="square-value">99%</div>
        <div class="square-label">Client Satisfaction</div>
      </div>
      
      <img src="images/services_hero_img_final.png" alt="Web Agency Services" loading="eager" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.1);">
    </div>
  </div>
</section>

<!-- CORE SERVICES CREATIVE GRID -->
<section id="services" class="wrap" style="margin-top: 80px; padding-bottom: 80px;">
  <div class="section-title text-center">
    <div class="eyebrow" style="margin: 0 auto 12px auto;">Our Services</div>
    <h2 class="h2" style="font-family: var(--font-display); font-size: 2.5rem; font-weight: 800;">Discover a wide range of expert services tailored to skyrocket your business</h2>
  </div>
  <div class="services-grid-creative">
    <div class="service-card-creative">
      <div class="icon-wrapper">
        <svg viewBox="0 0 24 24" width="36" height="36" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H7c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.04-.42 1.99-1.07 2.75z"/></svg>
      </div>
      <h3>Web Development</h3>
      <p>Our development services focus on creating dynamic, high-performing websites that deliver seamless UX & drive results.</p>
      <a href="contact.html" class="btn btn-ghost mt-4" style="margin-top:24px;">Get Started</a>
    </div>
    <div class="service-card-creative">
      <div class="icon-wrapper">
         <svg viewBox="0 0 24 24" width="36" height="36" fill="currentColor"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2s.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2s.07-1.35.16-2h4.68c.09.65.16 1.32.16 2s-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2s-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z"/></svg>
      </div>
      <h3>Google Ads</h3>
      <p>Maximize your ROI with expertly crafted ad campaigns designed to target the right audience and generate quality leads.</p>
      <a href="contact.html" class="btn btn-ghost mt-4" style="margin-top:24px;">Get Started</a>
    </div>
    <div class="service-card-creative">
      <div class="icon-wrapper">
         <svg viewBox="0 0 24 24" width="36" height="36" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
      </div>
      <h3>SEO Optimization</h3>
      <p>Boost your visibility with cutting-edge SEO strategies that ensure your business ranks higher and attracts organic traffic.</p>
      <a href="contact.html" class="btn btn-ghost mt-4" style="margin-top:24px;">Get Started</a>
    </div>
  </div>
</section>

<!-- OUR PROCESS -->
<section class="process-section-creative" style="padding-block: 100px;">
  <div class="wrap">
    <div class="section-title text-center">
      <div class="eyebrow" style="margin: 0 auto 12px auto;">Our Process</div>
      <h2 class="h2" style="font-family: var(--font-display); font-size: 2.5rem; font-weight: 800;">We follow a proven approach: understand, execute, and optimize</h2>
    </div>
    <div class="process process-grid-creative" style="max-width: 900px; margin: 0 auto; margin-top:60px;">
      <div class="process-step">
        <div class="depth">01</div>
        <h4>Understanding Needs</h4>
        <p>We start by listening to your goals and analyzing your business to craft a tailored strategy.</p>
      </div>
      <div class="process-step">
        <div class="depth">02</div>
        <h4>Seamless Execution</h4>
        <p>Our team brings strategy to life with expert design & development, ensuring impactful implementation.</p>
      </div>
      <div class="process-step">
        <div class="depth">03</div>
        <h4>Delivering Results</h4>
        <p>We track performance and provide continuous support to ensure long-term success for your business.</p>
      </div>
    </div>
  </div>
</section>

<!-- EXPERTISE DETAILS CREATIVE -->
<section class="wrap" style="padding-block: 100px;">
  <div class="section-title text-center">
    <div class="eyebrow" style="margin: 0 auto;">An Overview of Our Expertise</div>
  </div>
  <div class="expertise-row-creative" style="margin-top: 60px;">
    <div class="expertise-content-creative">
      <div class="eyebrow">Web Development</div>
      <h2>Custom Website Design and Innovative Digital Solutions</h2>
      <p>We combine creativity with advanced technology to craft impactful and user-friendly websites. Using iterative development and innovative solutions, we build digital experiences that engage users and drive success.</p>
      <a href="contact.html" class="btn btn-solid mt-4">Order Your Website</a>
    </div>
    <div class="expertise-image-creative">
      <img src="webagency_hero_team.jpg" alt="Web Development" loading="lazy">
    </div>
  </div>

  <div class="expertise-row-creative reverse">
    <div class="expertise-content-creative">
      <div class="eyebrow">Search Engine Optimization</div>
      <h2>Skyrocket Your Presence with Powerful SEO Solutions</h2>
      <p>Our SEO services are designed to help your business dominate search engines and connect with your audience. By implementing tailored strategies, optimizing content, and enhancing website performance, we ensure sustained growth.</p>
      <a href="contact.html" class="btn btn-solid mt-4">Want To Get SEO Services</a>
    </div>
    <div class="expertise-image-creative">
      <img src="webagency_hero_team.jpg" alt="SEO Optimization" loading="lazy">
    </div>
  </div>

  <div class="expertise-row-creative">
    <div class="expertise-content-creative">
      <div class="eyebrow">Google Ads Services</div>
      <h2>Maximize Your Reach with Result-Driven Campaigns</h2>
      <p>Our Google Ads services focus on creating highly targeted and optimized campaigns that deliver measurable results. From keyword research to ad design and performance tracking, we help you achieve maximum ROI.</p>
      <a href="contact.html" class="btn btn-solid mt-4">Get Google Ads Services</a>
    </div>
    <div class="expertise-image-creative">
      <img src="webagency_hero_team.jpg" alt="Google Ads Services" loading="lazy">
    </div>
  </div>
</section>
`;

const reusableSectionsStart = indexHtml.indexOf('<!-- INFINITE VERTICAL SCROLL TESTIMONIALS MARQUEE SECTION -->');
let foot = indexHtml.substring(reusableSectionsStart);

// Replace the dynamic bubble Capabilities section with a static premium grid for the Services page
const staticCapabilitiesHtml = `
<!-- STATIC CAPABILITIES GRID FOR SERVICES PAGE -->
<section class="wrap" style="padding-block: 100px;">
  <div class="section-title text-center" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
    <div class="eyebrow" style="margin: 0 auto 12px auto;">Interactive Experience</div>
    <h2 class="h2" style="font-family: var(--font-display); font-size: 2.5rem; font-weight: 800;">Our Core Capabilities</h2>
    <p style="color: var(--fg-soft); margin-top: 16px;">Discover the technologies and frameworks we master to build next-generation platforms.</p>
  </div>
  <div class="capabilities-static-grid" style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; margin-top: 40px; max-width: 900px; margin-inline: auto;">
    <div class="cap-pill" style="--pill-color: 100, 149, 237;">Figma</div>
    <div class="cap-pill" style="--pill-color: 147, 112, 219;">React</div>
    <div class="cap-pill" style="--pill-color: 102, 205, 170;">Node.js</div>
    <div class="cap-pill" style="--pill-color: 255, 160, 122;">Webflow</div>
    <div class="cap-pill" style="--pill-color: 255, 182, 193;">Framer</div>
    <div class="cap-pill" style="--pill-color: 72, 209, 204;">GSAP</div>
    <div class="cap-pill" style="--pill-color: 100, 149, 237;">Tailwind CSS</div>
    <div class="cap-pill" style="--pill-color: 147, 112, 219;">Next.js</div>
    <div class="cap-pill" style="--pill-color: 255, 182, 193;">Three.js</div>
    <div class="cap-pill" style="--pill-color: 102, 205, 170;">SEO Mastery</div>
    <div class="cap-pill" style="--pill-color: 255, 160, 122;">UI/UX Design</div>
    <div class="cap-pill" style="--pill-color: 72, 209, 204;">Google Ads</div>
  </div>
</section>
`;

// Remove the dynamic bubble Capabilities section from the reusable footer block entirely
foot = foot.replace(/<!-- CAPABILITIES SECTION -->[\s\S]*?<\/section>/, '');

// Append the new static Capabilities HTML to the end of servicesContent (BEFORE the footer block starts)
fs.writeFileSync(path.join(projectDir, 'services.html'), head + servicesContent + '\n' + staticCapabilitiesHtml + '\n' + foot);
console.log('Creative services.html created successfully.');