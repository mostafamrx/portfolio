import shutil
import re
from bs4 import BeautifulSoup

# Copy the new photo
new_photo_path = r'C:\Users\peace\Downloads\763761527_1616110816728376_2898293960429012657_n.png'
dest_path = r'd:\portfolio2\my_real_photo.png'
shutil.copy(new_photo_path, dest_path)

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken img tag
html = re.sub(r'<img 1670w"="".*?src="[^"]+".*?>', '', html) # Wait, it might be better to just parse it or replace the exact broken string.
# Actually, let's just do a string replace for the broken prefix:
html = html.replace('<img 1670w"=""', '<img')

soup = BeautifulSoup(html, 'html.parser')

mind_text = soup.find(lambda tag: tag.name in ['div', 'span'] and 'Have something in mind?' in tag.text)
if mind_text:
    parent = mind_text.find_parent('div', class_='cta-bottom') or mind_text.parent.parent
    if parent:
        img = parent.find('img')
        if img:
            img['src'] = 'my_real_photo.png'
            # Remove srcset and sizes just in case they have junk
            if 'srcset' in img.attrs:
                del img.attrs['srcset']
            if 'sizes' in img.attrs:
                del img.attrs['sizes']
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("Fixed img tag and updated photo.")
        else:
            print("Could not find img element inside parent")
    else:
        print("Could not find parent of mind_text")
else:
    print("Could not find mind_text")
