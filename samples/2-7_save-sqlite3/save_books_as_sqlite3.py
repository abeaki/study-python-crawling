import re
import sqlite3
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


conn = sqlite3.connect('books.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS books')
c.execute('''CREATE TABLE books
(url text, title text)''')

for link in links:
    c.execute('INSERT INTO books VALUES (?, ?)', (link['url'], link['title']))

conn.commit()
conn.close()
