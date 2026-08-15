import re
from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all circles with data-connect attribute
for i in [5, 6, 7]:
    circle = soup.find('circle', attrs={'data-connect': f'step-{i}'})
    if circle:
        circle.decompose()

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done")
