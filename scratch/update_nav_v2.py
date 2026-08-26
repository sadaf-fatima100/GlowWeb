import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Regex to catch href="..." inside the anchor tag for Search Engine Optimization
    # e.g., <a href="services.html">Search Engine Optimization</a>
    html = re.sub(r'<a href="[^"]*">Search Engine Optimization</a>', '<a href="search-engine-optimization.html">Search Engine Optimization</a>', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
