from urllib.request import urlopen, Request
import gzip
import time
import re

import lxml.html
from pymongo import MongoClient

USER_AGENT = 'mybot'


def crawl():
    html = fetch('http://gihyo.jp/book')
    urls = scrape_list_page(html)
    for url in urls:
        time.sleep(1)
        html = fetch(url)
        book = scrape_detail_page(html)
        print(book)
        save(book)


def fetch(url):
    request = Request(url, headers={
        'User-Agent': USER_AGENT,
    })
    f = urlopen(request)
    if f.getheader('Content-Encoding') == 'gzip':
        f = gzip.GzipFile(fileobj=f)

    html = f.read().decode('utf-8')
    return html


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
    client = MongoClient('localhost', 27017)
    db = client.scraping
    collection = db.books

    crawl()
