import re

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace viewBox with 2200
html = re.sub(r'viewBox="0 0 \d+ 338"', 'viewBox="0 0 2200 338"', html, flags=re.IGNORECASE)

# Add textLength and lengthAdjust to the text element to force it to exactly 2200 width
html = re.sub(r'(<text[^>]*)(>)', r'\1 textLength="2200" lengthAdjust="spacingAndGlyphs"\2', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
