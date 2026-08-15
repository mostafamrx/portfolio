import re
import sys

html_file = r'd:\portfolio2\final_portfolio.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    new_clip = r'<clipPath id="nesh-clip"><text font-family="sans-serif" font-size="250" font-weight="900" lengthAdjust="spacingAndGlyphs" textLength="2200" x="0" y="260">MOSTAFA ESSA™</text></clipPath>'
    
    html = re.sub(r'<clippath id="nesh-clip">.*?</clippath>', new_clip, html, flags=re.DOTALL | re.IGNORECASE)
    
    # Also we should update the width of the blue rect inside the SVG clip, otherwise it might only be 1388 instead of 2200
    html = html.replace('<rect fill="#007aff" height="338" width="1388">', '<rect fill="#007aff" height="338" width="2200">')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced SVG clip path!")
except Exception as e:
    print(f"Error: {e}")
