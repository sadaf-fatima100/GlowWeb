import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.capture = False
        self.tags = ['h1', 'h2', 'h3', 'p', 'li']

    def handle_starttag(self, tag, attrs):
        if tag in self.tags:
            self.capture = True
            self.text.append(f"\n{tag.upper()}: ")

    def handle_endtag(self, tag):
        if tag in self.tags:
            self.capture = False

    def handle_data(self, data):
        if self.capture:
            clean = data.strip()
            if clean:
                self.text.append(clean + " ")

parser = MyHTMLParser()
with open(r'C:\Users\DELL\.gemini\antigravity\brain\195d047f-6d9f-4fc8-bed1-5fb9721f5964\.system_generated\steps\4825\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

parser.feed(html)
with open('scratch/extracted_seo_text.txt', 'w', encoding='utf-8') as f:
    f.write("".join(parser.text))
