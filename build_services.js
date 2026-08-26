const fs = require('fs');
const path = require('path');

const projectDir = 'd:\\workspace\\hywiz-tasks\\m01\\projects\\2nd website';
const indexHtml = fs.readFileSync(path.join(projectDir, 'index.html'), 'utf8');
const headEnd = indexHtml.indexOf('<!-- WEB AGENCY HERO SECTION -->');
const footStart = indexHtml.indexOf('<!-- FOOTER -->');

const head = indexHtml.substring(0, headEnd);
const foot = indexHtml.substring(footStart);

const servicesContent = `
<!-- SERVICES HERO SECTION -->
<section class="services-page-hero">
  <div class="wrap text-center">
    <h1 class="h1">Our Services</h1>
    <p class="subtitle">Explore our wide range of expert services, from Web Design and Development to SEO, Google Ads, and Website Maintenance, crafted to elevate your business and drive measurable results.</p>
  </div>
</section>

<!-- CORE SERVICES GRID -->
<section class="services-core-grid wrap section-padding">
  <div class="section-title text-center">
    <h6 class="kicker">Our Services</h6>
    <h2 class="h2">Discover a wide range of expert services tailored to skyrocket your business online</h2>
  </div>
  <div class="services-grid-premium">
    <div class="service-card-premium">
      <div class="icon">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H7c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.04-.42 1.99-1.07 2.75z"/></svg>
      </div>
      <h3>Web Development</h3>
      <p>Our development services focus on creating dynamic, high-performing websites that deliver seamless UX & drive results.</p>
      <a href="contact.html" class="btn btn-ghost mt-4">Get Started</a>
    </div>
    <div class="service-card-premium">
      <div class="icon">
         <svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2s.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2s.07-1.35.16-2h4.68c.09.65.16 1.32.16 2s-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2s-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z"/></svg>
      </div>
      <h3>Google Ads</h3>
      <p>Maximize your ROI with expertly crafted ad campaigns designed to target the right audience and generate quality leads.</p>
      <a href="contact.html" class="btn btn-ghost mt-4">Get Started</a>
    </div>
    <div class="service-card-premium">
      <div class="icon">
         <svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
      </div>
      <h3>SEO Optimization</h3>
      <p>Boost your visibility with cutting-edge SEO strategies that ensure your business ranks higher and attracts organic traffic.</p>
      <a href="contact.html" class="btn btn-ghost mt-4">Get Started</a>
    </div>
  </div>
</section>

<!-- OUR PROCESS -->
<section class="services-process wrap section-padding">
  <div class="section-title text-center">
    <h6 class="kicker">Our Process</h6>
    <h2 class="h2">We follow a proven approach: understanding your needs, executing strategies, and optimizing for continuous growth and measurable results</h2>
  </div>
  <div class="process-timeline-premium">
    <div class="process-step-premium">
      <div class="step-num-premium">01</div>
      <h4>Understanding Your Needs</h4>
      <p>We start by listening to your goals and analyzing your business to craft a tailored strategy.</p>
    </div>
    <div class="process-step-premium">
      <div class="step-num-premium">02</div>
      <h4>Seamless Execution</h4>
      <p>Our team brings strategy to life with expert design, development, & optimization, ensuring a smooth & impactful implementation.</p>
    </div>
    <div class="process-step-premium">
      <div class="step-num-premium">03</div>
      <h4>Delivering Results</h4>
      <p>We track performance, refine strategies, and provide continuous support to ensure long-term success and growth for your business.</p>
    </div>
  </div>
</section>

<!-- EXPERTISE DETAILS -->
<section class="services-expertise wrap section-padding">
  <div class="section-title text-center">
    <h6 class="kicker">An Overview of Our Expertise</h6>
  </div>
  <div class="expertise-row-premium">
    <div class="expertise-content-premium">
      <h6 class="kicker">Web Development</h6>
      <h2>We are a Web Agency Specializing in Custom Website Design and Innovative Digital Solutions</h2>
      <p>We combine creativity with advanced technology to craft impactful and user-friendly websites. Using iterative development and innovative solutions, we build digital experiences that engage users and drive success.</p>
      <a href="contact.html" class="btn btn-solid mt-4">Order Your Website</a>
    </div>
    <div class="expertise-image-premium">
      <img src="webagency_hero_team.jpg" alt="Web Development" loading="lazy">
    </div>
  </div>

  <div class="expertise-row-premium reverse">
    <div class="expertise-content-premium">
      <h6 class="kicker">Search Engine Optimization</h6>
      <h2>Skyrocket Your Online Presence with Powerful SEO Solutions Tailored to Rank Your Business Higher</h2>
      <p>Our SEO services are designed to help your business dominate search engines and connect with your audience. By implementing tailored strategies, optimizing content, and enhancing website performance, we ensure sustained growth and measurable results.</p>
      <a href="contact.html" class="btn btn-solid mt-4">Want To Get SEO Services</a>
    </div>
    <div class="expertise-image-premium">
      <img src="webagency_hero_team.jpg" alt="SEO Optimization" loading="lazy">
    </div>
  </div>

  <div class="expertise-row-premium">
    <div class="expertise-content-premium">
      <h6 class="kicker">Google Ads Services</h6>
      <h2>Maximize Your Reach with Result-Driven Google Ads Campaigns</h2>
      <p>Our Google Ads services focus on creating highly targeted and optimized campaigns that deliver measurable results. From keyword research to ad design and performance tracking, we help you attract the right audience, increase conversions, and achieve maximum ROI.</p>
      <a href="contact.html" class="btn btn-solid mt-4">Get Google Ads Services</a>
    </div>
    <div class="expertise-image-premium">
      <img src="webagency_hero_team.jpg" alt="Google Ads Services" loading="lazy">
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="services-testimonials wrap section-padding">
  <div class="section-title text-center">
    <h6 class="kicker">Clients Testimonials</h6>
    <h2 class="h2">What they are saying About Us</h2>
  </div>
  <div class="testimonials-grid-premium">
    <div class="testimonial-card-premium">
      <p>"Outstanding service! They expertly transformed our website into a sleek, user-friendly, high-converting digital platform that consistently delivers excellent, measurable results."</p>
      <div class="client-info">
        <h5>James Carter</h5>
        <span>Marketing Director</span>
      </div>
    </div>
    <div class="testimonial-card-premium">
      <p>"They built a powerful, SEO-optimized website with smooth functionality, clear design, and fast performance that truly supports business growth online. Highly recommended!"</p>
      <div class="client-info">
        <h5>Sophia Mitchell</h5>
        <span>Operations Director</span>
      </div>
    </div>
    <div class="testimonial-card-premium">
      <p>"Fantastic experience! Their expert team created a modern, mobile-optimized website that’s intuitive, responsive, and seamlessly designed to boost traffic and online engagement."</p>
      <div class="client-info">
        <h5>Michael Turner</h5>
        <span>Head of Sales</span>
      </div>
    </div>
    <div class="testimonial-card-premium">
      <p>"The team developed a responsive, beautifully crafted website that’s simple to navigate, fully optimized, and designed to increase conversions effectively Excellent work! "</p>
      <div class="client-info">
        <h5>Emma Lawson</h5>
        <span>CEO</span>
      </div>
    </div>
  </div>
</section>
`;

fs.writeFileSync(path.join(projectDir, 'services.html'), head + servicesContent + foot);
console.log('services.html created successfully.');

