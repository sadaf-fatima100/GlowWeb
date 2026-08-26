import re

with open('google-ads.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Title
html = html.replace('<title>Google Ads Management - Hywiz Technologies</title>', '<title>Custom Web Development - Hywiz Technologies</title>')

# Hero
# Because google-ads.html structure is ads-hero-content and ads-hero-visual
html = html.replace('Google Ads Management', 'Web Development Services', 1)
html = html.replace('<h1>Targeted Google Ads <br><em>Campaigns</em></h1>', '<h1>Custom Web <br><em>Development</em></h1>')
html = re.sub(r'<h1 class="hero-title">Targeted Google Ads Campaigns to <span style="color:var\(--accent-primary\);">Maximize ROI</span> and Reach</h1>', '<h1 class="hero-title">Custom Web Development Services to Empower Your <span style="color:var(--accent-primary);">Online Presence</span></h1>', html)
html = html.replace('Achieve your marketing goals with expertly crafted Google Ads campaigns. We focus on driving qualified leads, increasing conversions, and delivering exceptional results.', 'From responsive designs to seamless functionality, we build websites tailored to your business goals. Elevate your brand with cutting-edge development solutions designed to engage and convert.')
html = html.replace('images/google-ads-hero.jpg', 'images/web-dev-hero.png')
html = html.replace('images/google-ads-hero.png', 'images/web-dev-hero.png')
html = html.replace('alt="Google Ads Dashboard"', 'alt="Web Development"')
html = html.replace('alt="Google Ads Features"', 'alt="Web Development"')

# Overview / Process Section
html = html.replace('<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Our Process</div>', '<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Web Development Services</div>', 1)
html = html.replace('<h2>Driving Targeted Traffic &amp; <br><em>Maximizing Your ROI</em></h2>', '<h2>Building Custom Websites for <br><em>Growth &amp; Success</em></h2>')
html = html.replace('Our Google Ads services are tailored to help your business reach the right audience at the right time. Choose us for expertly managed campaigns and strategic targeting.', 'Our Web Development services are designed to transform your ideas into dynamic, high-performing websites. We specialize in creating tailored, scalable, and responsive solutions that deliver seamless user experiences, drive engagement, and achieve measurable results.<br><br>Choose us for exceptional web development, advanced technologies, innovative design, and functionality that sets your business apart. With a team of skilled developers, a focus on quality, and fast project delivery, we ensure your success with solutions that are reliable, secure, &amp; designed to grow with your business.')

# Nodes
html = html.replace('Data-Driven Campaigns', 'Custom Website Development')
html = html.replace('Advanced Analytics', 'Responsive & Scalable Designs')
html = html.replace('Keyword Targeting', 'Advanced Security Features')
html = html.replace('Increased Lead Gen', 'Seamless User Experiences')
html = html.replace('High-Converting Ads', 'Timely Project Delivery')
html = html.replace('ROI-Focused Marketing', 'High-Performance Web Solutions')

# Stacking Cards
html = html.replace('<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Our Process</div>', '<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Why Choose Our Services</div>', 1) # This matches the second one
html = html.replace('<h2>Streamlined Steps for <span class="accent-text">Success</span></h2>', '<h2 style="font-size: clamp(2.2rem, 4vw, 3.4rem); line-height: 1.1; letter-spacing: -0.02em; margin-top: 8px;">Delivering Scalable, Tailored, <br><span class="accent-text">High-Performance Websites</span></h2>')
html = html.replace('We follow a proven approach: understanding your needs, executing strategies, and optimizing for continuous growth and measurable results.', 'Our Web Development services go beyond creating websites; we craft digital experiences that resonate with your audience and align with your business goals. With a focus on functionality, innovation, and design, we ensure your website stands out and drives measurable results.<br><br>Choose us for robust web development solutions, cutting-edge technologies, and a client-centric approach. With expertise in creating responsive and secure platforms, we help your business grow with a website that delivers exceptional performance and user satisfaction.')

# Cards Headings & Text
html = html.replace('<h3>Comprehensive Account Audit</h3>', '<h3>Custom-Tailored Website Development Solutions</h3>')
html = html.replace('We start by analyzing your current performance, identifying opportunities, and crafting a blueprint for success.', 'We build websites customized to your unique brand, ensuring all specific functionalities and requirements are met.')
html = html.replace('<h3>Strategic Campaign Setup</h3>', '<h3>Seamless Integration with Modern Tools and Platforms</h3>')
html = html.replace('Our team builds high-converting campaigns from the ground up, utilizing the latest targeting strategies and ad formats.', 'Our solutions smoothly integrate with modern APIs, platforms, and third-party tools to scale your business operations.')
html = html.replace('<h3>Delivering Results &amp; Ongoing Support</h3>', '<h3>Highly Responsive and Scalable Web Designs</h3>')
html = html.replace('We track performance, refine strategies, and provide continuous support to ensure long-term success and growth for your business.', 'We craft websites that look and perform flawlessly across all devices, built on an architecture that scales with your traffic.')

# Pricing Heading
html = html.replace('<h2>Flexible Plans Built for <span class="accent-text">Every Budget</span></h2>', '<h2>Affordable Website Development <span class="accent-text">Plans</span></h2>')
html = html.replace('Choose the perfect Google Ads plan tailored to your business goals. Our transparent pricing ensures high-quality management, reporting, and support—no hidden fees, just results.', 'Choose the perfect website development plan tailored to your business needs. Our transparent pricing ensures high-quality design, functionality, and support—no hidden fees, just results.')

# Pricing Starter Plan
starter_features = """
          <ul class="pricing-features">
            <li>4 Pages Website</li>
            <li>Basic SEO</li>
            <li>Mobile Responsive Design</li>
            <li>Payment Gateway Integration</li>
            <li>Domain Attachment</li>
            <li>Free Theme</li>
            <li>100% Optimized Web Design</li>
            <li>Turn Around Time: 1 - 2 Weeks</li>
            <li>Free 7 Days Support</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through; color:var(--text-color);">Free Web Hosting</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through; color:var(--text-color);">Product Upload</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through; color:var(--text-color);">Server Optimization</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through; color:var(--text-color);">Google Analytics Setup</li>
          </ul>
"""

html = re.sub(r'<div class="pricing-price">\s*\$500\s*<span class="pricing-period">/mo</span>\s*</div>\s*<div class="pricing-old-price" style="text-decoration: line-through; color: #888; font-size: 1rem; margin-bottom: 15px;">\$625\.00 \| Flat 20% Off</div>', '<div class="pricing-price">$997</div><div class="pricing-old-price" style="text-decoration: line-through; color: #888; font-size: 1rem; margin-bottom: 15px;">$1246.25 | Flat 20% Off</div>', html)
html = html.replace('(Starter Google Ads)', '(Start Up Website)')
html = re.sub(r'(<div class="pricing-card">.*?<div class="pricing-price">.*?</div>\s*<div class="pricing-old-price".*?</div>\s*)<ul class="pricing-features">.*?</ul>', r'\1' + starter_features.strip(), html, count=1, flags=re.DOTALL)

# Pricing Premium Plan
premium_features = """
          <ul class="pricing-features">
            <li>8 Pages Website</li>
            <li>SEO Optimized</li>
            <li>Mobile Responsive Design</li>
            <li>Payment Gateway Integration</li>
            <li>Free Web Hosting</li>
            <li>Domain Attachment</li>
            <li>Premium Theme</li>
            <li>100% Optimized Web Design</li>
            <li>Free 7 Days Support</li>
            <li>Turn Around Time: 2+ Weeks</li>
            <li>Product Upload</li>
            <li>Server Optimization</li>
            <li>Google Analytics Setup</li>
          </ul>
"""
html = re.sub(r'<div class="pricing-price">\s*\$900\s*<span class="pricing-period">/mo</span>\s*</div>\s*<div class="pricing-old-price" style="text-decoration: line-through; color: #fff; opacity:0\.8; font-size: 1rem; margin-bottom: 15px;">\$1125\.00 \| Flat 20% Off</div>', '<div class="pricing-price">$1497</div><div class="pricing-old-price" style="text-decoration: line-through; color: #fff; opacity:0.8; font-size: 1rem; margin-bottom: 15px;">$1996 | Flat 25% Off</div>', html)
html = html.replace('(Advanced Ads Management)', '(Professional Website)')
html = re.sub(r'(<div class="pricing-card premium">.*?<div class="pricing-price">.*?</div>\s*<div class="pricing-old-price".*?</div>\s*)<ul class="pricing-features">.*?</ul>', r'\1' + premium_features.strip(), html, count=1, flags=re.DOTALL)

# Pricing Business Plan (Diamond)
business_features = """
          <ul class="pricing-features">
            <li>12+ Pages Website</li>
            <li>Fully SEO Optimized</li>
            <li>Mobile Responsive Design</li>
            <li>Payment Gateway Integration</li>
            <li>Product Upload</li>
            <li>Chat Bot Setup</li>
            <li>Google Analytics Setup</li>
            <li>Google Search Console</li>
            <li>Domain Attachment</li>
            <li>Free Web Hosting</li>
            <li>Server Optimization</li>
            <li>Free 14+ Days Support</li>
            <li>Turn Around Time: 2-3+ Weeks</li>
          </ul>
"""
html = re.sub(r'<div class="pricing-price">\s*\$1500\s*<span class="pricing-period">/mo</span>\s*</div>\s*<div class="pricing-old-price" style="text-decoration: line-through; color: #888; font-size: 1rem; margin-bottom: 15px;">\$1875\.00 \| Flat 20% Off</div>', '<div class="pricing-price">$1997</div><div class="pricing-old-price" style="text-decoration: line-through; color: #888; font-size: 1rem; margin-bottom: 15px;">$2496.25 | Flat 20% Off</div>', html)
html = html.replace('(Enterprise Solutions)', '(Business Website)')
html = html.replace('Diamond Plan', 'Business Plan')
html = re.sub(r'(<div class="pricing-card diamond">.*?<div class="pricing-price">.*?</div>\s*<div class="pricing-old-price".*?</div>\s*)<ul class="pricing-features">.*?</ul>', r'\1' + business_features.strip(), html, count=1, flags=re.DOTALL)


with open('web-development.html', 'w', encoding='utf-8') as f:
    f.write(html)
