# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import BlogPost
from myproject.utils import get_content


class BlogSpider(CrawlSpider):
    name = "blog"
    start_urls = (
        'http://hatenablog.com/',     # はてなブログ
        'http://blog.livedoor.com/',  # ライブドアブログ
        'https://medium.com/',        # Medium
    )

    rules = [
        Rule(LinkExtractor(allow=(
            r'/entry/\d+/',           # はてなブログの記事ページの正規表現
            r'/archives/\d+\.html$',  # ライブドアブログの記事ページの正規表現
            r'/@\w+/[^/]+',           # Mediumの記事ページの正規表現
        ), deny=(
            r'^https?://b\.hatena\.ne\.jp/',  # はてなブックマークのURLはクロールしない
        )), callback='parse_post'),
    ]

    custom_settings = {
        # リンクを辿る深さを1に制限する
        'DEPTH_LIMIT': 1,
        # ドメイン単位ではなくIPアドレス単位でウェイトを入れる
        'CONCURRENT_REQUESTS_PER_IP': 8,
    }

    def parse_post(self, response):
        """
        記事ページをパースする。
        """

        # 正規URLが指定されている場合はそのURLを、指定されていない場合はresponse.urlを使う
        url = response.css('link[rel="canonical"]::attr("href")').extract_first() or response.url
        # タイトルと本文を抽出する
        title, content = get_content(response)

        yield BlogPost(url=url, title=title, content=content)
