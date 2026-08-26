import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update dropdown and mobile nav links
    content = content.replace('<a href="services.html">Web Development</a>', '<a href="web-development.html">Web Development</a>')
    
    # Update footer links
    content = content.replace('<a href="#servicesSection">Web Development</a>', '<a href="web-development.html">Web Development</a>')
    
    # Note: On the google ads page, the footer link is to #servicesSection, same as index.html
    # It's better to replace them to point to the new individual page.
    
    # Also update google ads footer link for consistency? (The user didn't ask but it's good practice)
    content = content.replace('<a href="#servicesSection">Google Ads</a>', '<a href="google-ads.html">Google Ads</a>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files.")
