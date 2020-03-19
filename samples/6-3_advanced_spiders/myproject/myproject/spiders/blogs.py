import scrapy

from myproject.items import BlogPost
from myproject.utils import get_content


class BlogsSpider(scrapy.Spider):
    name = "blogs"
    start_urls = (
        # はてなブックマークの「ブログ・日記」特集の新着エントリ一覧ページ。
        'http://b.hatena.ne.jp/entrylist/%E3%83%96%E3%83%AD%E3%82%B0%E3%83%BB%E6%97%A5%E8%A8%98',
    )

    def parse(self, response):
        """
        はてなブックマークのエントリ一覧ページをパースする。
        """

        # 個別の記事へのリンクをたどる。
        for url in response.css('a.entry-link::attr("href")').extract():
            # parse_post() メソッドをコールバック関数として指定する。
            yield scrapy.Request(url, callback=self.parse_post)

        # of=の値が2桁である間のみ「次の20件」のリンクをたどる（最大5ページ目まで）。
        url_more = response.css('a::attr("href")').re_first(r'.*\?of=\d{2}$')
        if url_more:
            # url_moreの値は /entrylist で始まる相対URLなので、
            # response.urljoin()メソッドを使って絶対URLに変換する。
            # コールバック関数を指定していないので、レスポンスはデフォルト値である
            # parse()メソッドで処理される。
            yield scrapy.Request(response.urljoin(url_more))

    def parse_post(self, response):
        """
        個別の記事ページをパースする。
        """

        # utils.pyに定義したget_content()関数でタイトルと本文を抽出する。
        title, content = get_content(response)
        # BlogPostオブジェクトを作成してyieldする。
        yield BlogPost(url=response.url, title=title, content=content)
