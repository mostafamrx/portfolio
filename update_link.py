from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
for link in links:
    if link.text and 'Book a Call' in link.text:
        link['href'] = 'https://wa.me/201030654348'
        # Optional: open in new tab
        link['target'] = '_blank'

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done")
