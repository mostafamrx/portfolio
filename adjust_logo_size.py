import re

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add TM back
html = html.replace('MOSTAFA ESSA</text>', 'MOSTAFA ESSA™</text>')

# Set viewBox width to exactly frame the text so it scales up nicely
html = re.sub(r'viewBox="0 0 \d+ 338"', 'viewBox="0 0 1950 338"', html, flags=re.IGNORECASE)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
