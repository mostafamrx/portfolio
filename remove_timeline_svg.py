import re
from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Remove the old timeline SVGs
for cls in ['desktop-timeline-icon', 'mobile-timeline-icon']:
    elements = soup.find_all(class_=cls)
    for el in elements:
        el.decompose()

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done")
