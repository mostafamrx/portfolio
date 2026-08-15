import re
from bs4 import BeautifulSoup

user_html = """
<!-- Project 1 -->
                <div class="project-card" style="position: relative; flex: 0 0 auto; width: 450px; background: #1a1a1a; padding: 20px; border-radius: 16px; border: 1px solid #333;"> <!-- تمت إضافة position: relative هنا -->
                    <div class="project-tags" style="display: flex; gap: 10px; margin-bottom: 15px;">
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Scikit-learn</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Python</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Google Sheets API</span>
                    </div>
                    
                    <!-- الفيديو -->
                    <video autoplay loop muted playsinline style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; margin-bottom: 20px; background: #333;">
                        <source src="offers_builder.mp4" type="video/mp4">
                        متصفحك لا يدعم تشغيل الفيديو.
                    </video>
                    
                    <!-- تم تحديد عرض النص بـ 85% لكي لا يتداخل مع الزر -->
                    <h3 style="width: 85%; color: #FFF; margin-bottom: 10px; font-size: 1.5rem;">Menu Optimization AI</h3>
                    <p style="width: 85%; color: #aaa; font-size: 1rem; line-height: 1.5;">Engineered a predictive classification model using Random Forest and XGBoost to simulate offers and optimize operational performance.</p>
                    
                    <!-- الزر الأصفر لفتح النافذة المنبثقة -->
                    <button onclick="openModal('modal-project-1')" style="position: absolute; bottom: 30px; right: 30px; width: 45px; height: 45px; background-color: var(--accent-yellow, #e9ff46); border: none; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: #111; font-size: 20px; font-weight: bold; cursor: pointer; transition: transform 0.2s; box-shadow: 0 4px 15px rgba(244, 255, 0, 0.2);">
                        ↗
                    </button>
                </div>

<!-- Project 2 -->
                <div class="project-card" style="position: relative; flex: 0 0 auto; width: 450px; background: #1a1a1a; padding: 20px; border-radius: 16px; border: 1px solid #333;"> <!-- تمت إضافة position: relative -->
                    <div class="project-tags" style="display: flex; gap: 10px; margin-bottom: 15px;">
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Ai Agents</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Docker</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">n8n</span>
                    </div>
                    
                    <!-- الصورة هنا (تم استبدال الـ div بـ img) -->
                    <img src="n8n.png" alt="Automated Sync Pipelines" style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; margin-bottom: 20px; background: #333;">
                    
                    <!-- تحديد عرض النص بـ 85% لترك مساحة للزر -->
                    <h3 style="width: 85%; color: #FFF; margin-bottom: 10px; font-size: 1.5rem;">Automated Sync Pipelines</h3>
                    <p style="width: 85%; color: #aaa; font-size: 1rem; line-height: 1.5;">Designed a microservices architecture to synchronize relational cloud databases automatically utilizing webhook integrations.</p>
                    
                    <!-- الزر الأصفر لفتح النافذة المنبثقة للمشروع الثاني -->
                    <button onclick="openModal('modal-project-2')" style="position: absolute; bottom: 30px; right: 30px; width: 45px; height: 45px; background-color: var(--accent-yellow, #e9ff46); border: none; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: #111; font-size: 20px; font-weight: bold; cursor: pointer; transition: transform 0.2s; box-shadow: 0 4px 15px rgba(244, 255, 0, 0.2);">
                        ↗
                    </button>
                </div>

<!-- Project 3 -->
                <div class="project-card" style="position: relative; flex: 0 0 auto; width: 450px; background: #1a1a1a; padding: 20px; border-radius: 16px; border: 1px solid #333;">
                    <div class="project-tags" style="display: flex; gap: 10px; margin-bottom: 15px;">
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">XGBoost</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">SMOTE</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Data-Centric AI</span>
                    </div>
                    
                    <!-- ضع صورة تعبر عن لوحة التحكم أو التطبيق هنا -->
                    <img src="ASD_perdiction.png" alt="ASD Prediction AI" style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; margin-bottom: 20px; background: #333;">
                    
                    <h3 style="width: 85%; color: #FFF; margin-bottom: 10px; font-size: 1.5rem;">ASD Screening & Prediction AI</h3>
                    <p style="width: 85%; color: #aaa; font-size: 1rem; line-height: 1.5;">An end-to-end Machine Learning pipeline utilizing Data-Centric AI and XGBoost to predict Autism Spectrum Disorder based on behavioral features.</p>
                    
                    <!-- الزر الأصفر لفتح تفاصيل المشروع -->
                    <button onclick="openModal('modal-project-3')" style="position: absolute; bottom: 30px; right: 30px; width: 45px; height: 45px; background-color: var(--accent-yellow, #e9ff46); border: none; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: #111; font-size: 20px; font-weight: bold; cursor: pointer; transition: transform 0.2s; box-shadow: 0 4px 15px rgba(244, 255, 0, 0.2);">
                        ↗
                    </button>
                </div>

                <!-- Project 4 (Work in Progress) -->
                <div class="project-card" style="position: relative; flex: 0 0 auto; width: 450px; background: #1a1a1a; padding: 20px; border-radius: 16px; border: 1px solid #333;">
                    <!-- شارة جاري العمل عليه -->
                    <div style="position: absolute; top: 20px; right: 20px; background: var(--accent-yellow, #e9ff46); color: #111; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 800; z-index: 2; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
                        🚧 IN PROGRESS
                    </div>

                    <div class="project-tags" style="display: flex; gap: 10px; margin-bottom: 15px;">
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">AI Voice</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Dynamic Memory</span>
                        <span style="background: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; color: #ccc;">Async DB</span>
                    </div>
                    
                    <!-- صورة المشروع (يمكنك وضع صورة تعبيرية لمعمارية النظام Blueprint) -->
                    <img src="Ai_teacher.png" alt="Mo3lmy Architecture" style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; margin-bottom: 20px; background: #333; opacity: 0.8;">
                    
                    <h3 style="width: 85%; color: #FFF; margin-bottom: 10px; font-size: 1.5rem;">Mo3lmy Framework</h3>
                    <p style="width: 85%; color: #aaa; font-size: 1rem; line-height: 1.5;">Developing the technical infrastructure for a real-time, adaptive AI voice tutoring application featuring dynamic memory layers and asynchronous database controllers.</p>
                    
                    <!-- الزر الأصفر لفتح تفاصيل المشروع -->
                    <button onclick="openModal('modal-project-4')" style="position: absolute; bottom: 30px; right: 30px; width: 45px; height: 45px; background-color: var(--accent-yellow, #e9ff46); border: none; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: #111; font-size: 20px; font-weight: bold; cursor: pointer; transition: transform 0.2s; box-shadow: 0 4px 15px rgba(244, 255, 0, 0.2);">
                        ↗
                    </button>
                </div>
"""

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

track = soup.find(class_='work-track')
if track:
    track.clear()
    # Add gap styling to work track if needed
    if not track.get('style'):
        track['style'] = ''
    track['style'] += '; display: flex; gap: 30px; padding: 20px 0;'
    track.append(BeautifulSoup(user_html, 'html.parser'))

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Done adding projects")
else:
    print("Error: .work-track not found")
