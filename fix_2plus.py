import re

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Specifically target the 2+ text element which has font-size="29"
html = re.sub(r'(<text[^>]*font-size="29"[^>]*?)\s*textLength="2200"\s*lengthAdjust="spacingAndGlyphs"([^>]*>)', r'\1\2', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
