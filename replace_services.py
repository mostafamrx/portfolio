import re
from bs4 import BeautifulSoup

user_html = """
<!-- Services Section -->
        <section id="services" style="padding: 100px 5%; color: #111;">
            
            <!-- Header & Subtitle -->
            <div style="margin-bottom: 60px; max-width: 600px;">
                <h2 style="font-size: 4.5rem; font-weight: 900; line-height: 1; margin-bottom: 20px; letter-spacing: -2px;">AI Solutions<br>That Deliver</h2>
                <p style="font-size: 1.1rem; color: #444; line-height: 1.6;">
                    Engineering intelligent systems tailored to your business. From conversational AI to predictive analytics and automated workflows.
                </p>
            </div>

            <!-- Services Cards Container -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); background: rgba(227, 225, 217, 0.3); border-radius: 20px; overflow: hidden;">
                
                <!-- Card 1: AI Agents (Darker Background) -->
                <div style="background: rgba(200, 200, 195, 0.6); padding: 50px 40px; display: flex; flex-direction: column;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 40px;">
                        <div style="background: var(--accent-yellow, #e9ff46); width: 35px; height: 35px; border-radius: 6px; display: flex; justify-content: center; align-items: center; color: #111;">
                            <!-- AI Icon -->
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a2 2 0 0 1 2 2c0 1.1-.9 2-2 2s-2-.9-2-2a2 2 0 0 1 2-2z"></path><path d="M19 8h-1.5a1.5 1.5 0 0 0-1.5 1.5v3.5a1.5 1.5 0 0 1-1.5 1.5h-5a1.5 1.5 0 0 1-1.5-1.5v-3.5A1.5 1.5 0 0 0 6.5 8H5"></path><circle cx="12" cy="16" r="3"></circle></svg>
                        </div>
                        <h3 style="font-size: 1.4rem; font-weight: 800;">Autonomous AI</h3>
                    </div>
                    <h4 style="font-size: 2.2rem; font-weight: 900; margin-bottom: 20px;">AI Agents <span style="font-size: 1rem; font-weight: 500; color: #555;">& Voice</span></h4>
                    <p style="color: #333; line-height: 1.6; font-size: 1.05rem;">
                        Custom-built AI agents with dynamic memory frameworks. I design intelligent conversational systems and real-time voice applications that adapt to complex logic and user behavior.
                    </p>
                </div>

                <!-- Card 2: ML Models -->
                <div style="padding: 50px 40px; display: flex; flex-direction: column; border-right: 1px solid rgba(0,0,0,0.05);">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 40px;">
                        <div style="background: var(--accent-yellow, #e9ff46); width: 35px; height: 35px; border-radius: 6px; display: flex; justify-content: center; align-items: center; color: #111;">
                            <!-- Data/ML Icon -->
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                        </div>
                        <h3 style="font-size: 1.4rem; font-weight: 800;">Predictive Analysis</h3>
                    </div>
                    <h4 style="font-size: 2.2rem; font-weight: 900; margin-bottom: 20px;">ML Models</h4>
                    <p style="color: #444; line-height: 1.6; font-size: 1.05rem;">
                        End-to-end machine learning pipelines utilizing Data-Centric AI. From classification models solving class imbalances to optimizing business strategies through accurate forecasting.
                    </p>
                </div>

                <!-- Card 3: Smart Automations -->
                <div style="padding: 50px 40px; display: flex; flex-direction: column;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 40px;">
                        <div style="background: var(--accent-yellow, #e9ff46); width: 35px; height: 35px; border-radius: 6px; display: flex; justify-content: center; align-items: center; color: #111;">
                            <!-- Automation Icon -->
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polyline></svg>
                        </div>
                        <h3 style="font-size: 1.4rem; font-weight: 800;">Data Engineering</h3>
                    </div>
                    <h4 style="font-size: 2.2rem; font-weight: 900; margin-bottom: 20px;">Smart Pipelines</h4>
                    <p style="color: #444; line-height: 1.6; font-size: 1.05rem;">
                        Designing robust microservices architectures and automated data sync pipelines. I leverage containerized deployments to ensure seamless, real-time data flow without manual intervention.
                    </p>
                </div>
            </div> <!-- Close container -->
        </section> <!-- Close section -->
"""

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

services_sec = soup.find(id='services')
if services_sec:
    # Replace the existing section with the new user_html
    new_soup = BeautifulSoup(user_html, 'html.parser')
    services_sec.replace_with(new_soup)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Done replacing services section")
else:
    print("Error: services section not found")
