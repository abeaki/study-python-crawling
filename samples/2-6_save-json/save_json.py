import re
import json
from html import unescape


def strip_tags(text):
    return re.sub(r'<.*?>', '', text)


with open('book.html') as f:
    html = f.read()

links = []
for url, title in re.findall(r'<a.*href="(.*?)".*?>(.*?)</a></h3>', html, re.IGNORECASE):
    links.append({
        'url': url,
        'title': unescape(strip_tags(title)),
    })

with open('books.json', 'w') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
