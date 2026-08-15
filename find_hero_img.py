from bs4 import BeautifulSoup

with open(r'd:\portfolio2\porto.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

hero = soup.find(id='hero')
if hero:
    # Print the image or anything containing 'img' or 'profile'
    profile_wrap = hero.find(class_=lambda c: c and 'profile' in c)
    if profile_wrap:
        print("Found profile wrap:")
        print(profile_wrap.prettify()[:1000])
    else:
        print("Profile wrap not found")
        # Let's find any img
        for img in hero.find_all('img'):
            print(img.prettify())
