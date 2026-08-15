import html.parser
import re

class TemplateParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.output = []
        self.in_script_or_style = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.in_script_or_style += 1
        
        attr_str = ""
        for k, v in attrs:
            if tag == 'img':
                if k == 'srcset' or k == 'sizes' or k == 'fetchpriority' or k == 'loading':
                    continue # remove these attributes to simplify
                if k == 'src':
                    v = 'https://via.placeholder.com/800x800' # Placeholder image
            if v is None:
                attr_str += f" {k}"
            else:
                # Escape quotes
                v = v.replace('"', '&quot;')
                attr_str += f' {k}="{v}"'
        
        if tag in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'):
            self.output.append(f"<{tag}{attr_str}/>")
        else:
            self.output.append(f"<{tag}{attr_str}>")

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.in_script_or_style -= 1
        
        self.output.append(f"</{tag}>")

    def handle_data(self, data):
        if self.in_script_or_style > 0:
            self.output.append(data)
        else:
            # Replace visible text with placeholders
            if data.strip():
                # Determine what to replace it with based on length
                words = len(data.split())
                if words <= 2:
                    new_data = "Title Here"
                elif words <= 5:
                    new_data = "Your Custom Text Here"
                else:
                    new_data = "This is a placeholder for your longer paragraph. You can replace this text with your own content easily."
                
                # Keep surrounding whitespace
                left_space = data[:len(data) - len(data.lstrip())]
                right_space = data[len(data.rstrip()):]
                
                self.output.append(left_space + new_data + right_space)
            else:
                self.output.append(data)

    def handle_comment(self, data):
        self.output.append(f"<!--{data}-->")

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")

    def handle_decl(self, decl):
        self.output.append(f"<!{decl}>")
        
    def handle_pi(self, data):
        self.output.append(f"<?{data}>")

with open(r'd:\portfolio2\porto.html', 'r', encoding='utf-8') as f:
    content = f.read()

parser = TemplateParser()
parser.feed(content)

# Add line breaks before common tags to make it more readable
html_out = "".join(parser.output)
html_out = re.sub(r'(<(div|section|nav|header|footer|p|h1|h2|h3|h4|h5|h6|ul|li|a)[^>]*>)', r'\n\1', html_out)
html_out = re.sub(r'(</(div|section|nav|header|footer|p|h1|h2|h3|h4|h5|h6|ul|li|a)>)', r'\1\n', html_out)

with open(r'd:\portfolio2\porto_template.html', 'w', encoding='utf-8') as f:
    f.write(html_out)
