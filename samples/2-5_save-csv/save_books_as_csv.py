import re
import csv
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

with open('books.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for link in links:
        writer.writerow([link['url'], link['title']])
