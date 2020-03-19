import sys

import feedparser
import requests
from bs4 import BeautifulSoup


def main():
    d = feedparser.parse('http://b.hatena.ne.jp/hotentry.rss')
    urls = [entry.link for entry in d.entries]

    for url in urls:
        print(fetch_and_scrape(url))


def fetch_and_scrape(url):
    print('Start downloading', url, file=sys.stderr)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    return {
        'url': url,
        'title': soup.title.text.strip(),
    }

if __name__ == '__main__':
    main()
