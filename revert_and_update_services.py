import re
from bs4 import BeautifulSoup

porto_file = r'd:\portfolio2\porto.html'
final_file = r'd:\portfolio2\final_portfolio.html'

with open(porto_file, 'r', encoding='utf-8') as f:
    porto_soup = BeautifulSoup(f.read(), 'html.parser')

with open(final_file, 'r', encoding='utf-8') as f:
    final_soup = BeautifulSoup(f.read(), 'html.parser')

# Get the original services section
orig_services = porto_soup.find(id='services')

# Update Header & Subtitle
h2 = orig_services.find('h2')
h2.clear()
h2.append(BeautifulSoup('AI Solutions<br>That Deliver', 'html.parser'))

p = orig_services.find('p', class_='max-width-389')
p.string = 'Engineering intelligent systems tailored to your business. From conversational AI to predictive analytics and automated workflows.'

# The cards
cards = orig_services.find_all(class_='service-card')

data = [
    {
        'cat': 'Autonomous AI',
        'title': 'AI Agents <span style="font-size: 1rem; font-weight: 500; color: #555;">& Voice</span>',
        'text': 'Custom-built AI agents with dynamic memory frameworks. I design intelligent conversational systems and real-time voice applications that adapt to complex logic and user behavior.',
        'icon': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a2 2 0 0 1 2 2c0 1.1-.9 2-2 2s-2-.9-2-2a2 2 0 0 1 2-2z"></path><path d="M19 8h-1.5a1.5 1.5 0 0 0-1.5 1.5v3.5a1.5 1.5 0 0 1-1.5 1.5h-5a1.5 1.5 0 0 1-1.5-1.5v-3.5A1.5 1.5 0 0 0 6.5 8H5"></path><circle cx="12" cy="16" r="3"></circle></svg>'
    },
    {
        'cat': 'Predictive Analysis',
        'title': 'ML Models',
        'text': 'End-to-end machine learning pipelines utilizing Data-Centric AI. From classification models solving class imbalances to optimizing business strategies through accurate forecasting.',
        'icon': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>'
    },
    {
        'cat': 'Data Engineering',
        'title': 'Smart Pipelines',
        'text': 'Designing robust microservices architectures and automated data sync pipelines. I leverage containerized deployments to ensure seamless, real-time data flow without manual intervention.',
        'icon': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polyline></svg>'
    }
]

for i, card in enumerate(cards):
    if i < 3:
        # Update Icon
        icon_wrap = card.find(class_='service-card-top-item')
        if icon_wrap:
            icon_wrap.clear()
            # Wrap the icon in the user's div to match style
            icon_html = f'<div style="background: #007aff; width: 42px; height: 42px; border-radius: 10px; display: flex; justify-content: center; align-items: center; color: #fff;">{data[i]["icon"]}</div>'
            icon_wrap.append(BeautifulSoup(icon_html, 'html.parser'))
            
            # Add category label text next to icon (original had it separate or we can append it)
            # Original structure: <div class="service-card-top-item"><svg.../><h3 class="margin-bottom-0">Strategy...</h3></div>
            h3_cat = porto_soup.new_tag('h3', attrs={'class': 'margin-bottom-0 h4-style'})
            h3_cat.string = data[i]['cat']
            icon_wrap.append(h3_cat)

        # Update Title
        title_el = card.find('h3', class_='h3-style')
        if title_el:
            title_el.clear()
            title_el.append(BeautifulSoup(data[i]['title'], 'html.parser'))
            
        # Update Text
        text_el = card.find('p', class_='service-card-text')
        if text_el:
            text_el.string = data[i]['text']

# Replace in final_portfolio
current_services = final_soup.find(id='services')
if current_services:
    current_services.replace_with(orig_services)
    
    with open(final_file, 'w', encoding='utf-8') as f:
        f.write(str(final_soup))
    print("Done reverting and updating services")
else:
    print("Could not find services in final_portfolio")

