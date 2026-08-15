import os
from bs4 import BeautifulSoup

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all(class_='about-card-wrap')

data = [
    {"year": "20", "title": "Web Design & SEO", "desc": "Managed full-cycle website operations, combining custom web design with technical SEO to build robust digital foundations."},
    {"year": "23", "title": "Data Analysis", "desc": "Headed data analytics initiatives, extracting actionable insights from large datasets to drive strategic business decisions."},
    {"year": "25", "title": "Software & ERP", "desc": "Architected and developed enterprise resource planning (ERP) systems, streamlining complex business operations and data integration."},
    {"year": "26", "title": "AI Systems Architect", "desc": "Leading the development of autonomous AI agents and scalable Machine Learning applications for predictive analysis and automation."}
]

if len(cards) >= 4:
    # Delete cards beyond the 4th
    for card in cards[4:]:
        card.decompose()

    # Update the 4 cards
    for i, card in enumerate(cards[:4]):
        item = data[i]
        
        # Update Year
        year_span = card.find(attrs={"data-number-count": True})
        if year_span:
            year_span['data-number-count'] = item["year"]
            year_span.string = item["year"]
            
        # Update Title
        title_el = card.find(class_='about-card-heading')
        if title_el:
            title_el.string = item["title"]
            
        # Update Desc
        desc_el = card.find('p', class_='op80')
        if desc_el:
            desc_el.string = item["desc"]
            
        # Remove bottom layout (removes modal and extra UI)
        bottom_layout = card.find(class_='about-card-bottom-layout')
        if bottom_layout:
            bottom_layout.decompose()

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Timeline updated successfully!")
else:
    print("Error: Could not find timeline cards in the HTML.")
