import time
import re
import sys

import requests
import lxml.html
from pymongo import MongoClient

from scraper_tasks import scrape


def main():
    """
    クローラーのメインの処理
    """

    client = MongoClient('localhost', 27017)  # ローカルホストのMongoDBに接続する
    collection = client.scraping.ebook_htmls  # scrapingデータベースのebook_htmlsコレクションを得る
    # keyで高速に検索できるように、ユニークなインデックスを作成する
    collection.create_index('key', unique=True)

    response = requests.get('https://gihyo.jp/dp')  # 一覧ページを取得する
    urls = scrape_list_page(response)  # 詳細ページのURL一覧を得る
    for url in urls:
        key = extract_key(url)  # URLからキーを取得する

        ebook_html = collection.find_one({'key': key})  # MongoDBからkeyに該当するデータを探す
        if not ebook_html:  # MongoDBに存在しない場合だけ、詳細ページをクロールする
            time.sleep(1)
            print('Fetching {0}'.format(url), file=sys.stderr)
            response = requests.get(url)          # 詳細ページを取得する
            collection.insert_one({
                'url': url,
                'key': key,
                'html': response.content,
            })  # HTMLをMongoDBに保存する

            scrape.delay(key)


def scrape_list_page(response):
    """
    一覧ページのResponseから詳細ページのURLを抜き出す
    """
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('a[itemprop="url"]'):
        url = a.get('href')
        if url.startswith('https://gihyo.jp/dp/ebook/'):
            yield url


def extract_key(url):
    """
    URLからキー (URLの末尾のISBN) を抜き出す
    """
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)

if __name__ == '__main__':
    main()
