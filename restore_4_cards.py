import re
from bs4 import BeautifulSoup

porto_file = r'd:\portfolio2\porto.html'
final_file = r'd:\portfolio2\final_portfolio.html'

with open(porto_file, 'r', encoding='utf-8') as f:
    porto_soup = BeautifulSoup(f.read(), 'html.parser')

with open(final_file, 'r', encoding='utf-8') as f:
    final_soup = BeautifulSoup(f.read(), 'html.parser')

timeline_wrap_porto = porto_soup.find(class_='about-timeline-wrap')

if timeline_wrap_porto:
    # 1. Keep only 4 cards
    cards = timeline_wrap_porto.find_all(class_='about-card-wrap')
    for i, card in enumerate(cards):
        if i >= 4:
            card.decompose()

    # 2. Update timeline overflow
    overflow = timeline_wrap_porto.find(class_='about-timeline-overflow')
    if overflow:
        # Update keyframes to stop at 56% (4th card)
        new_tl_to = "{ 'keyframes': [ { 'height': '14%', 'duration': 2 }, { 'height': '28%', 'duration': 1 }, { 'height': '42%', 'duration': 1.5 }, { 'height': '56%', 'duration': 2 } ], 'ease': 'none' }"
        overflow['data-tl-to'] = new_tl_to

        # Modify the SVG
        svg = overflow.find('svg')
        if svg:
            # Change viewBox height to 1120 to crop it right after the 4th circle (cy="1092.5")
            svg['viewBox'] = "0 0 1118 1120"
            
            # Keep only first 4 circles
            circles = svg.find_all('circle')
            for i, circle in enumerate(circles):
                if i >= 4:
                    circle.decompose()

    # 3. Replace the one in final_portfolio.html
    wrap_final = final_soup.find(class_='about-timeline-wrap')
    if wrap_final:
        wrap_final.replace_with(timeline_wrap_porto)
    else:
        # If it doesn't exist, we just append it somewhere appropriate? It should exist since we only cleared it before
        pass

    with open(final_file, 'w', encoding='utf-8') as f:
        f.write(str(final_soup))

print("Done")
