import re
from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# I will use BeautifulSoup to find the exact button
soup = BeautifulSoup(html, 'html.parser')
buttons = soup.find_all(lambda tag: tag.name in ['a', 'button'] and 'Try the Live Interactive App' in tag.text)

for btn in buttons:
    if btn.name == 'a':
        btn['href'] = "https://asd-prediction-ml-eg7u2jdrahyeabhj5mqpfj.streamlit.app/"
        # add target blank if it doesn't have it
        if 'target' not in btn.attrs:
            btn['target'] = "_blank"
    elif btn.name == 'button':
        # If it's a button, we can wrap it in an anchor or add onclick
        btn['onclick'] = "window.open('https://asd-prediction-ml-eg7u2jdrahyeabhj5mqpfj.streamlit.app/', '_blank')"

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done updating app link")
