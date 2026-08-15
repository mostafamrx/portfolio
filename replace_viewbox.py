import re

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace viewbox to make it wide enough for MOSTAFA ESSA
html = re.sub(r'viewbox="0 0 1288 338"', 'viewBox="0 0 2300 338"', html, flags=re.IGNORECASE)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
