from urllib.request import urlopen, Request
import gzip
import time
import re

import lxml.html
from pymongo import MongoClient

USER_AGENT = 'mybot'


def crawl():
    queue.append('http://gihyo.jp/book')

    while queue:
        url = queue.pop(0)
        html = fetch(url)
        parse(url, html)
        time.sleep(1)


def fetch(url):
    request = Request(url, headers={
        'User-Agent': USER_AGENT,
    })
    f = urlopen(request)
    if f.getheader('Content-Encoding') == 'gzip':
        f = gzip.GzipFile(fileobj=f)

    html = f.read().decode('utf-8')
    return html


def parse(url, html):
    if is_detail_page(url):
        book = scrape_detail_page(html)
        print(book)
        save(book)
    else:
        urls = scrape_list_page(html)
        queue.extend(urls)


def is_detail_page(url):
    return re.search(r'^http://gihyo\.jp/book/\d+/[\d-]+$', url) is not None


def scrape_list_page(html):
    root = lxml.html.fromstring(html)
    for a in root.xpath('//h3//a'):
        yield a.get('href')


def scrape_detail_page(html):
    root = lxml.html.fromstring(html)
    return {
        'title': ''.join(root.xpath('//h1[@itemprop="name"]/text()')),
        'author': re.sub(r'　[著編]', '', root.xpath('//p[@itemprop="author"]')[0].text),
        'numPages': root.xpath('//span[@itemprop="numberOfPages"]')[0].text,
    }


def save(book):
    collection.insert(book)


if __name__ == '__main__':
    queue = []
    client = MongoClient('localhost', 27017)
    db = client.scraping
    global collection
    collection = db.books

    crawl()
