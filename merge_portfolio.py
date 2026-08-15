import re
from bs4 import BeautifulSoup
import os

with open(r'd:\portfolio2\porto.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

with open(r'd:\portfolio2\MY_portfolio.html', 'r', encoding='utf-8') as f:
    my_soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Update Hero Section
# Name and Headline
titles = soup.find_all(class_="hero-title")
if len(titles) >= 2:
    titles[0].string = "AI"
    titles[1].string = "ENGINEER"

# Profile Image
profile_img = soup.find(class_="hero-profile-img")
if profile_img:
    profile_img['src'] = "profile.png"
    if 'srcset' in profile_img.attrs:
        del profile_img['srcset']

# Subtitles / Descriptions
descs = soup.find_all(class_="hero-subtitle")
if descs:
    for d in descs:
        d.string = "Engineering intelligent systems. I specialize in building autonomous AI Agents, smart automations, and scalable ML applications that drive business efficiency and innovation."

# Stats (Projects & Experience)
# Usually inside classes like "hero-stat-number" and "hero-stat-text"
stat_nums = soup.find_all(string=re.compile(r'80\+'))
for n in stat_nums:
    n.replace_with("7+")

# Logo / Small Texts
# Find "Nenad" and replace with "Mostafa", "Popadic" with "Essa"
for text_node in soup.find_all(string=re.compile(r'Nenad|Popadic|The Webflow Expert', re.IGNORECASE)):
    new_text = text_node.replace('Nenad', 'Mostafa').replace('nenad', 'mostafa').replace('Popadic', 'Essa').replace('popadic', 'essa')
    new_text = new_text.replace('The Webflow Expert', 'The AI Expert')
    text_node.replace_with(new_text)

# 2. Services Section ("What you get")
services = soup.find_all(class_="capa-card-wrap")
my_services_data = [
    {"title": "Autonomous AI", "desc": "Custom-built AI agents with dynamic memory frameworks. I design intelligent conversational systems and real-time voice applications that adapt to complex logic and user behavior."},
    {"title": "Predictive Analysis", "desc": "End-to-end machine learning pipelines utilizing Data-Centric AI. From classification models solving class imbalances to optimizing business strategies through accurate forecasting."},
    {"title": "Data Engineering", "desc": "Designing robust microservices architectures and automated data sync pipelines. I leverage containerized deployments to ensure seamless, real-time data flow without manual intervention."}
]

if services:
    for i, s_data in enumerate(my_services_data):
        if i < len(services):
            title = services[i].find(class_="capa-card-title")
            if title: title.string = s_data["title"]
            
            desc = services[i].find(class_="capa-card-p")
            if desc: desc.string = s_data["desc"]

# 3. Experience / Journey
exp_cards = soup.find_all(class_="history-card-inner")
my_exp_data = [
    {"year": "2026", "title": "AI Systems Architect", "desc": "Leading the development of autonomous AI agents and scalable Machine Learning applications for predictive analysis and automation."},
    {"year": "2025", "title": "Software & ERP", "desc": "Architected and developed enterprise resource planning (ERP) systems, streamlining complex business operations and data integration."},
    {"year": "2023", "title": "Data Analysis", "desc": "Headed data analytics initiatives, extracting actionable insights from large datasets to drive strategic business decisions."},
    {"year": "2020", "title": "Web Design & SEO", "desc": "Managed full-cycle website operations, combining custom web design with technical SEO to build robust digital foundations."}
]

if exp_cards:
    for i, e_data in enumerate(my_exp_data):
        if i < len(exp_cards):
            year = exp_cards[i].find(class_="history-year")
            if year: year.string = e_data["year"]
            
            title = exp_cards[i].find(class_="history-card-title")
            if title: title.string = e_data["title"]
            
            desc = exp_cards[i].find(class_="history-p")
            if desc: desc.string = e_data["desc"]

# 4. Projects Section
projects = soup.find_all(class_="work-card")
my_projects_data = [
    {"title": "Menu Optimization AI", "tags": "Scikit-learn, Python, Google Sheets API", "media": "offers_builder.mp4", "is_video": True, "modal": "modal-project-1"},
    {"title": "Automated Sync Pipelines", "tags": "Ai Agents, Docker, n8n", "media": "n8n.png", "is_video": False, "modal": "modal-project-2"},
    {"title": "ASD Screening & Prediction AI", "tags": "XGBoost, SMOTE, Data-Centric AI", "media": "ASD_perdiction.png", "is_video": False, "modal": "modal-project-3"},
    {"title": "Mo3lmy Framework", "tags": "AI Voice, Dynamic Memory, Async DB", "media": "Ai_teacher.png", "is_video": False, "modal": "modal-project-4"}
]

if projects:
    for i, p_data in enumerate(my_projects_data):
        if i < len(projects):
            proj = projects[i]
            
            # Change Title
            p_title = proj.find(class_="work-card-title")
            if p_title: p_title.string = p_data["title"]
            
            # Change image/video
            img = proj.find('img')
            if img:
                if 'srcset' in img.attrs:
                    del img['srcset']
                if p_data["is_video"]:
                    # Create video element
                    video_html = f'<video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;"><source src="{p_data["media"]}" type="video/mp4"></video>'
                    video_soup = BeautifulSoup(video_html, 'html.parser')
                    img.replace_with(video_soup)
                else:
                    img['src'] = p_data["media"]
            
            # Modify the link to open the modal
            # Instead of a normal link, we will add an onclick event and change href to #
            link = proj.find('a', class_="work-card-link")
            if link:
                link['href'] = "#"
                link['onclick'] = f"openModal('{p_data['modal']}'); return false;"

# Delete unused sections like Testimonials or Articles
# For testimonials, let's find classes containing "testimonial"
for section in soup.find_all(class_=re.compile(r'testimonial', re.IGNORECASE)):
    section.decompose()
for section in soup.find_all(class_=re.compile(r'article|faq', re.IGNORECASE)):
    section.decompose()

# 5. Inject Modals HTML, CSS, and JS
# Get Modals CSS from MY_portfolio.html
my_styles = my_soup.find_all('style')
if my_styles:
    # Only keep the modal styles
    modal_css = """
    /* Modal Styles Injected */
    .modal-overlay {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(10px);
        z-index: 10000; opacity: 0; visibility: hidden; transition: all 0.3s ease;
        display: flex; justify-content: center; align-items: center;
    }
    .modal-overlay.active { opacity: 1; visibility: visible; }
    .modal-content {
        background: #111; width: 90%; max-width: 800px; max-height: 85vh;
        overflow-y: auto; border-radius: 16px; padding: 40px; position: relative;
        transform: translateY(30px); transition: transform 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    .modal-overlay.active .modal-content { transform: translateY(0); }
    .close-btn {
        position: absolute; top: 20px; left: 20px; background: none; border: none;
        color: #fff; font-size: 2rem; cursor: pointer; transition: color 0.2s;
    }
    .close-btn:hover { color: #007aff; }
    .modal-features { display: flex; flex-direction: column; gap: 20px; }
    .feature-item h4 { color: #fff; margin-bottom: 5px; font-size: 1.1rem; }
    .feature-item p { color: #aaa; font-size: 0.95rem; line-height: 1.5; }
    .modal-content::-webkit-scrollbar { width: 8px; }
    .modal-content::-webkit-scrollbar-track { background: transparent; }
    .modal-content::-webkit-scrollbar-thumb { background: #555; border-radius: 10px; }
    """
    style_tag = soup.new_tag("style")
    style_tag.string = modal_css
    soup.head.append(style_tag)

# Extract Modal Elements
modals = my_soup.find_all(id=re.compile(r'modal-project-\d'))
for modal in modals:
    # Change any yellow accent colors inside modal to blue to match porto.html
    modal_str = str(modal).replace('var(--accent-yellow)', '#007aff')
    modal_soup = BeautifulSoup(modal_str, 'html.parser')
    soup.body.append(modal_soup)

# Inject JS for Modals
script_tag = soup.new_tag("script")
script_tag.string = """
function openModal(modalId) {
    document.getElementById(modalId).classList.add('active');
    document.body.style.overflow = 'hidden'; 
}
function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
    document.body.style.overflow = 'auto'; 
}
"""
soup.body.append(script_tag)

# Save the updated HTML
html_content = str(soup)
with open(r'd:\portfolio2\final_portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Merged successfully!")
