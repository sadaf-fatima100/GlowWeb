import re

with open('google-ads.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Title
html = html.replace('<title>Google Ads Management - Hywiz Technologies</title>', '<title>Search Engine Optimization - Hywiz Technologies</title>')

# Hero
html = html.replace('<div class="eyebrow" style="display:inline-block; margin-bottom: 20px;">🚀 Maximize ROI</div>', '<div class="eyebrow" style="display:inline-block; margin-bottom: 20px;">SEO Services</div>')
html = re.sub(r'<h1 class="hero-title">Targeted Google Ads Campaigns to <span style="color:var\(--accent-primary\);">Maximize ROI</span> and Reach</h1>', '<h1 class="hero-title" style="font-size: clamp(2.5rem, 5vw, 4.5rem);">Result-Driven SEO Services to <span style="color:var(--accent-primary);">Rank Higher</span> and Grow Smarter</h1>', html)
html = html.replace('Achieve your marketing goals with expertly crafted Google Ads campaigns. We focus on driving qualified leads, increasing conversions, and delivering exceptional results.', 'Boost your visibility and attract organic traffic with expert SEO strategies. We optimize your website for search engines to drive growth and deliver measurable success.')
# We'll just leave the hero image as Google ads for now or replace it later if the user provides one. 
html = html.replace('alt="Google Ads Features"', 'alt="SEO Services"')

# Overview / Process Section
html = html.replace('<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Google Ads Services</div>', '<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">SEO Services</div>')
# Heading is already Driving Targeted Traffic & Maximizing Your ROI
html = html.replace('Our Google Ads services are tailored to help your business reach the right audience at the right time. Choose us for expertly managed campaigns and strategic targeting.', 'Our SEO services are designed to boost your website’s visibility and drive organic traffic. We specialize in comprehensive optimization strategies, including keyword research, technical SEO, and content enhancements, to ensure your business ranks higher and attracts the right audience.<br><br>Choose us for proven SEO solutions, customized strategies, and measurable results that align with your goals. With a focus on performance, advanced tools, and ongoing optimization, we help your business stay ahead in search engine rankings and achieve sustainable success.')

# Nodes
html = html.replace('Data-Driven Campaigns', 'Tailored SEO Strategies')
html = html.replace('Advanced Analytics', 'Enhanced Website Visibility')
html = html.replace('Keyword Targeting', 'In-Depth Keyword Research')
html = html.replace('Increased Lead Gen', 'Organic Traffic Growth')
html = html.replace('High-Converting Ads', 'Technical SEO Expertise')
html = html.replace('ROI-Focused Marketing', 'Measurable, Long-Term Results')

# Stacking Cards
html = html.replace('<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Why Choose Us</div>', '<div class="eyebrow" style="justify-content: center; margin-bottom: 20px;">Why Choose Us</div>')
html = re.sub(r'<h2 style="font-size: clamp\(2.2rem, 4vw, 3.4rem\); line-height: 1.1; letter-spacing: -0.02em; margin-top: 8px;">Driving Conversions with <br><span class="accent-text">Targeted Ad Campaigns</span></h2>', '<h2 style="font-size: clamp(2.2rem, 4vw, 3.4rem); line-height: 1.1; letter-spacing: -0.02em; margin-top: 8px;">Achieve Higher Rankings &amp; <br><span class="accent-text">Long-Term Growth</span></h2>', html)
html = html.replace('Our Google Ads services are built to help your business grow through smart, results-oriented ad campaigns.', 'Our SEO services are crafted to help your business dominate search engines and connect with your target audience. By leveraging innovative techniques, in-depth research, and advanced tools, we deliver optimization strategies that boost visibility and drive sustained results.<br><br>Choose us for tailored SEO solutions, measurable outcomes, and expert guidance. With a focus on performance and continuous improvement, we ensure your business thrives in the competitive digital landscape.')

# Cards Headings & Text
html = html.replace('<h3>Advanced Keyword Research</h3>\n              <p>Discovering the most profitable keywords for maximum impact.</p>', '<h3>Customized SEO Strategies for Your Unique Needs</h3>')
html = html.replace('<h3>Increased Conversions</h3>\n              <p>Driving qualified lead generation straight into your sales pipeline.</p>', '<h3>Enhanced Organic Traffic and Audience Engagement</h3>')
html = html.replace('<h3>Engaging Ad Content</h3>\n              <p>Creative and highly-optimized ad content that demands attention.</p>', '<h3>Sustainable Results with Long-Term Optimization</h3>')
html = html.replace('<h3>Cost-Effective Solutions</h3>\n              <p>Sustainable growth strategies engineered for maximum budget efficiency.</p>', '<h3>Technical SEO for Optimized Site Performance</h3>')
# Wait, SEO only provided 3 items for stacking cards in the URL text?
# Wait, the extracted text says:
# LI: Customized SEO Strategies for Your Unique Needs 
# LI: Enhanced Organic Traffic and Audience Engagement 
# LI: Sustainable Results with Long-Term Optimization 
# LI: Technical SEO for Optimized Site Performance
# So there are 4 cards! Perfect! That matches the 4 cards in google-ads.html.

# Pricing Heading
html = html.replace('<h2>Affordable Google Ads <br><em>Service Plans</em></h2>', '<h2>Affordable SEO Services <br><em>Plans</em></h2>')
html = html.replace('Choose the perfect Google Ads service plan tailored to your business needs. No hidden fees, just results.', 'Choose the perfect SEO service plan tailored to your business needs. Our transparent pricing ensures strategic optimization, higher rankings, and ongoing support—no hidden fees, just results.')

# Pricing Starter Plan
starter_features = """
          <ul class="pricing-features">
            <li>4 Keywords</li>
            <li>5 Pages Optimization</li>
            <li>1 Article Writing</li>
            <li>1 Location</li>
            <li>Keyword Analysis</li>
            <li>Competition Analysis</li>
            <li>Local Search Setup</li>
            <li>Detailed Analysis Report</li>
            <li>Monthly Action Report</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through;">Blog Creation/Submission</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through;">Video Creation</li>
            <li class="disabled" style="opacity:0.5; text-decoration:line-through;">Search Engine Ranking Report</li>
            <li>Turn Around Time: 4 days</li>
          </ul>
"""
html = html.replace('<h3 class="plan-name">Starter Plan</h3>', '<h3 class="plan-name">Starter Plan</h3>')
html = re.sub(r'<div class="price-wrap">\s*<span class="old-price">\$871\.25</span>\s*<span class="new-price">\$697</span>\s*</div>', '<div class="price-wrap"><span class="old-price">$871.25</span><span class="new-price">$697</span></div>', html)
html = re.sub(r'(<div class="pricing-card reveal-up".*?<div class="price-wrap">.*?</div>\s*)<ul class="pricing-features">.*?</ul>', r'\1' + starter_features.strip(), html, count=1, flags=re.DOTALL)

# Pricing Premium Plan
premium_features = """
          <ul class="pricing-features">
            <li>6 Keywords</li>
            <li>8 Pages Optimization</li>
            <li>2 Article Writing</li>
            <li>1 Location</li>
            <li>Keyword Analysis</li>
            <li>Competition Analysis</li>
            <li>Local Search Setup</li>
            <li>Detailed Analysis Report</li>
            <li>Monthly Action Report</li>
            <li>Blog Creation/Submission</li>
            <li>Video Creation</li>
            <li>Search Engine Ranking Report</li>
            <li>Turn Around Time: 5 days</li>
          </ul>
"""
html = html.replace('<h3 class="plan-name">Premium Plan</h3>', '<h3 class="plan-name">Premium Plan</h3>')
html = re.sub(r'<div class="price-wrap">\s*<span class="old-price">\$1465\.33</span>\s*<span class="new-price">\$997</span>\s*</div>', '<div class="price-wrap"><span class="old-price" style="color:rgba(255,255,255,0.7);">$1465.33</span><span class="new-price">$997</span></div>', html)
html = re.sub(r'(<div class="pricing-card premium reveal-up".*?<div class="price-wrap">.*?</div>\s*)<ul class="pricing-features">.*?</ul>', r'\1' + premium_features.strip(), html, count=1, flags=re.DOTALL)

# Pricing Business Plan (Diamond)
business_features = """
          <ul class="pricing-features">
            <li>10 Keywords</li>
            <li>15 Pages Optimization</li>
            <li>2 Article Writing</li>
            <li>1 Location</li>
            <li>Keyword Analysis</li>
            <li>Competition Analysis</li>
            <li>Local Search Setup</li>
            <li>Detailed Analysis Report</li>
            <li>Monthly Action Report</li>
            <li>Blog Creation/Submission</li>
            <li>Video Creation</li>
            <li>Search Engine Ranking Report</li>
            <li>Turn Around Time: 7 days</li>
          </ul>
"""
html = html.replace('<h3 class="plan-name">Business Plan</h3>', '<h3 class="plan-name">Business Plan</h3>')
html = re.sub(r'<div class="price-wrap">\s*<span class="old-price">\$1871\.25</span>\s*<span class="new-price">\$1497</span>\s*</div>', '<div class="price-wrap"><span class="old-price">$1871.25</span><span class="new-price">$1497</span></div>', html)
html = re.sub(r'(<div class="pricing-card reveal-up".*?<h3 class="plan-name">Business Plan</h3>\s*<div class="price-wrap">.*?</div>\s*)<ul class="pricing-features">.*?</ul>', r'\1' + business_features.strip(), html, count=1, flags=re.DOTALL)

with open('search-engine-optimization.html', 'w', encoding='utf-8') as f:
    f.write(html)
