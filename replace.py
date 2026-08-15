import re
import os

input_file = r"C:\Users\peace\.gemini\antigravity\brain\f22e0e4f-147c-4e14-93cd-a12e117058bd\.system_generated\steps\4\content.md"
output_file = r"d:\portfolio2\porto.html"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract HTML content
html_start = content.find('<!DOCTYPE html>')
if html_start != -1:
    html_content = content[html_start:]
else:
    html_content = content

# Replace yellow with blue
# The yellow used is #ffff23 / #FFFF23
# We'll use a nice vibrant blue like #007aff (Apple Blue) which fits well with dark/light themes.
html_content = re.sub(r'#ffff23', '#007aff', html_content, flags=re.IGNORECASE)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {output_file}")
