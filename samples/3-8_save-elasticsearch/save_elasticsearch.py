import re
import json

import lxml.html
import requests


def extract_key(url):
    return re.search(r'^http://gihyo\.jp/book/\d+/([\d-]+)$', url).group(1)


def save_to_elasticsearch(key, item):
    requests.put('http://localhost:9200/scraping/books/{0}'.format(key), json.dumps(item))


with open('book.html') as f:
    root = lxml.html.fromstring(f.read())

for a in root.xpath('//h3//a'):
    url = a.get('href')
    key = extract_key(url)
    save_to_elasticsearch(key, {
        'url': url,
        'title': a.text_content(),
    })
