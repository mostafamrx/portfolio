import re

html_file = r'd:\portfolio2\porto.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

hero_start = html.find('id="hero"')
hero_end = html.find('id="about"')
hero_html = html[hero_start:hero_end]

imgs = re.findall(r'<img[^>]+>', hero_html)
print("Images found in raw HTML:")
for img in imgs:
    if 'hero-profile-img' in img or '1670w' in img:
        print(img)
