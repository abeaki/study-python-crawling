import re

import lxml.html
from pymongo import MongoClient
from celery import Celery


app = Celery('scraper_tasks', broker='amqp://guest@localhost//')


@app.task
def scrape(key):
    client = MongoClient('localhost', 27017)  # ローカルホストのMongoDBに接続する
    html_collection = client.scraping.ebook_htmls  # scrapingデータベースのebooksコレクションを得る

    ebook_html = html_collection.find_one({'key': key})  # MongoDBからkeyに該当するデータを探す
    ebook = scrape_detail_page(key, ebook_html['url'], ebook_html['html'])

    ebook_collection = client.scraping.ebooks
    ebook_collection.insert_one(ebook)

    return ebook


def scrape_detail_page(key, url, html):
    """
    詳細ページのResponseから電子書籍の情報をdictで得る
    """
    root = lxml.html.fromstring(html)
    ebook = {
        'key': key,
        'url': url,
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text_content().strip(),
        'content': [re.sub(r'\s+', ' ', h3.text_content()).strip() for
                    h3 in root.cssselect('#content > h3')],
    }
    return ebook


def extract_key(url):
    """
    URLからキー (URLの末尾のISBN) を抜き出す
    """
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)
