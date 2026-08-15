import re

html_file = r'd:\portfolio2\final_portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the 5 specific terms
replacements = {
    "Creative": "Generative",
    "Reliable": "Robust",
    "Strategist": "Predictive",
    "Builder": "Architect",
    "Efficient": "Autonomous"
}

for old_term, new_term in replacements.items():
    html = html.replace(f">{old_term}</p>", f">{new_term}</p>")
    html = html.replace(f">{old_term}</span>", f">{new_term}</span>")
    html = html.replace(f">\n{old_term}\n</p>", f">\n{new_term}\n</p>")
    # General fallback just in case there are no specific tags around it:
    html = re.sub(r'>\s*' + old_term + r'\s*<', f'>{new_term}<', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
