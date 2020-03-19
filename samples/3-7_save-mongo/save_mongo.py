import re

import lxml.html
from pymongo import MongoClient


def is_detail_page(url):
    return re.search(r'^http://gihyo\.jp/book/\d+/[\d-]+$', url) is not None

with open('book.html') as f:
    root = lxml.html.fromstring(f.read())

client = MongoClient('localhost', 27017)
db = client.scraping
collection = db.books

for a in root.xpath('//h3//a'):
    collection.insert({
        'url': a.get('href'),
        'title': a.text_content(),
    })
