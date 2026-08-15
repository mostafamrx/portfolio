html = open(r'd:\portfolio2\porto.html', 'r', encoding='utf-8').read()
idx = html.find('1670w')
with open(r'd:\portfolio2\debug.txt', 'w', encoding='utf-8') as f:
    f.write(html[idx-200:idx+300])
