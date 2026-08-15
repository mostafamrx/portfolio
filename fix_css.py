import re
import urllib.request

html_file = r"d:\portfolio2\porto.html"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Find all stylesheet links
links = re.findall(r'<link[^>]*href="([^"]+\.css)"[^>]*>', html)

for i, link in enumerate(links):
    if "http" in link:
        print(f"Downloading {link}...")
        try:
            req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                css_content = response.read().decode('utf-8')
            
            # Replace colors
            css_content = re.sub(r'#ffff23', '#007aff', css_content, flags=re.IGNORECASE)
            css_content = re.sub(r'#fdf822', '#007aff', css_content, flags=re.IGNORECASE)
            
            local_css = f"style_{i}.css"
            with open(f"d:\\portfolio2\\{local_css}", "w", encoding="utf-8") as f:
                f.write(css_content)
            
            # Replace the link in HTML
            html = html.replace(link, local_css)
            # Also remove integrity attribute to prevent SRI check failure
            html = re.sub(r'integrity="[^"]+"', '', html)
            print(f"Replaced {link} with {local_css}")
        except Exception as e:
            print(f"Failed to download {link}: {e}")

# Also check for any inline styles inside the HTML that we might have missed
html = re.sub(r'#ffff23', '#007aff', html, flags=re.IGNORECASE)
html = re.sub(r'#fdf822', '#007aff', html, flags=re.IGNORECASE)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated HTML.")
