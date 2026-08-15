import re
from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

svg_position = soup.find('svg', class_='about-timeline-position')
if svg_position:
    svg_position['viewBox'] = "0 0 1118 1120"
    if 'viewbox' in svg_position.attrs:
        svg_position['viewbox'] = "0 0 1118 1120"

# Wait, is there any other element with a large height?
# The wrapper `.about-card-container` itself might have a large padding or height if it's set in Webflow CSS.
# Let's save the SVG change first.
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done viewBox change")
