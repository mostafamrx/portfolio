import re
from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the CTA title (Transform Your Webflow)
cta_h2 = soup.find(lambda tag: tag.name == 'h2' and 'Transform Your' in tag.text)
if cta_h2:
    cta_h2.clear()
    cta_h2.append(BeautifulSoup('Transform Your<br>Business<br><span style="color:#ffffff;">With AI</span>', 'html.parser'))
else:
    print("Could not find CTA title")

# Find the CTA paragraph
# "Every Webflow site has room to grow..."
cta_p = soup.find(lambda tag: tag.name == 'p' and 'Every Webflow site has room to grow' in tag.text)
if cta_p:
    cta_p.string = "Every business has untapped potential. By integrating cutting-edge AI models, autonomous agents, and smart data pipelines, you can automate workflows, predict trends, and scale faster than ever before. Let's build the future of your company today."
else:
    print("Could not find CTA paragraph")

# Find the CTA image next to "Have something in mind?"
# Let's find the text "Have something in mind?" and look for nearby image
mind_text = soup.find(lambda tag: tag.name in ['div', 'span'] and 'Have something in mind?' in tag.text)
if mind_text:
    parent = mind_text.find_parent('div', class_='cta-bottom') or mind_text.parent.parent
    if parent:
        img = parent.find('img')
        if img:
            img['src'] = "new_profile.png"
            img['srcset'] = ""
else:
    print("Could not find mind text")

# Find the Let's Talk button
lets_talk = soup.find(lambda tag: tag.name == 'a' and "Let's Talk" in tag.text)
if lets_talk:
    lets_talk['href'] = 'https://wa.me/201030654348'
    lets_talk['target'] = '_blank'
else:
    print("Could not find Let's Talk button")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done updating CTA")
