import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # The current dropdown structure:
    # <ul class="dropdown-menu">
    #   <li><a href="web-development.html">Web Development</a></li>
    #   <li><a href="google-ads.html">Google Ads</a></li>
    #   <li><a href="#seo">Search Engine Optimization</a></li>
    # </ul>
    # Or in mobile menu:
    # <li><a href="web-development.html">Web Development</a></li>
    # <li><a href="google-ads.html">Google Ads</a></li>
    # <li><a href="#seo">Search Engine Optimization</a></li>

    # Let's replace #seo with search-engine-optimization.html
    html = html.replace('href="#seo"', 'href="search-engine-optimization.html"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
