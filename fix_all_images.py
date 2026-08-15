import re
from bs4 import BeautifulSoup

porto_file = r'd:\portfolio2\porto.html'
final_file = r'd:\portfolio2\final_portfolio.html'

with open(porto_file, 'r', encoding='utf-8') as f:
    porto_soup = BeautifulSoup(f.read(), 'html.parser')

with open(final_file, 'r', encoding='utf-8') as f:
    final_soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Restore the missing Hero Image
porto_hero = porto_soup.find(class_='hero')
final_hero = final_soup.find(class_='hero')

# Find the hero image wrapper in porto
hero_img_wrap = porto_hero.find(class_='hero-image-wrap') or porto_hero.find(class_=lambda c: c and 'image' in c and 'mobile' not in c)
if not hero_img_wrap:
    # It might be in hero-img or something. Let's find any img in porto_hero that's not mobile
    imgs = porto_hero.find_all('img')
    for img in imgs:
        if 'mobile' not in img.get('class', []):
            porto_hero_img = img
            break
    
# Actually, wait, let's just find the img that had the syntax error in porto.html string
html_str = str(porto_hero)
# We know from earlier there was a <img 1670w"="" ... class="hero-profile-img"
# Let's see if we can find it by class in porto_soup? Wait, BeautifulSoup strips malformed tags!
# So we must extract it from porto.html as a raw string!
