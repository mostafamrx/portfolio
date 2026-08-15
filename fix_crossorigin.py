with open("d:/portfolio2/porto.html", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('crossorigin="anonymous"', '')

with open("d:/portfolio2/porto.html", "w", encoding="utf-8") as f:
    f.write(text)
