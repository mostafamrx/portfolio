import json
from bs4 import BeautifulSoup

porto_file = r'd:\portfolio2\porto.html'
final_file = r'd:\portfolio2\final_portfolio.html'

with open(porto_file, 'r', encoding='utf-8') as f:
    porto_soup = BeautifulSoup(f.read(), 'html.parser')

with open(final_file, 'r', encoding='utf-8') as f:
    final_soup = BeautifulSoup(f.read(), 'html.parser')

timeline_overflow = porto_soup.find(class_='about-timeline-overflow')
if timeline_overflow:
    # 1. Update the keyframes to stop at 42% (which corresponds to the 3rd card)
    tl_to = timeline_overflow.get('data-tl-to', '')
    if tl_to:
        # It's a string like: { 'keyframes': [ ... ] }
        # Let's just do string replacement for safety instead of json parsing, since it has single quotes
        # Actually it's easier to just replace the whole attribute
        new_tl_to = "{ 'keyframes': [ { 'height': '14%', 'duration': 2 }, { 'height': '28%', 'duration': 1 }, { 'height': '42%', 'duration': 1.5 } ], 'ease': 'none' }"
        timeline_overflow['data-tl-to'] = new_tl_to

    # 2. Modify the SVG
    svg = timeline_overflow.find('svg')
    if svg:
        # Change viewBox height to 780
        svg['viewBox'] = "0 0 1118 780"
        
        # Remove extra circles (keep only the first 3)
        circles = svg.find_all('circle')
        for i, circle in enumerate(circles):
            if i >= 3:
                circle.decompose()

    # 3. Insert it into final_portfolio.html
    wrap = final_soup.find(class_='about-timeline-wrap')
    if wrap:
        # Clear existing just in case
        wrap.clear()
        wrap.append(timeline_overflow)

    with open(final_file, 'w', encoding='utf-8') as f:
        f.write(str(final_soup))

print("Done")
