import glob
import re

html_files = glob.glob("*.html")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace data-default-theme="light" with data-default-theme="dark" data-theme="dark"
    new_content = re.sub(
        r'<html([^>]*?)data-default-theme="light"([^>]*?)>',
        r'<html\1data-default-theme="dark" data-theme="dark"\2>',
        content
    )
    # Ensure data-theme="dark" is present if data-default-theme="dark" exists without data-theme
    new_content = re.sub(
        r'<html([^>]*?)data-default-theme="dark"(?![^>]*?data-theme)([^>]*?)>',
        r'<html\1data-default-theme="dark" data-theme="dark"\2>',
        new_content
    )
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated default theme to dark in {fpath}")

print("All HTML pages standardized to dark theme default!")
