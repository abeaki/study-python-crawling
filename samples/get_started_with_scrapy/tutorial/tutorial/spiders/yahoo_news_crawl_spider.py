# coding: utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from ..items import NewsItem


class YahooNewsCrawlSpider(CrawlSpider):
    name = 'yahoo_news_crawl'
    allowed_domains = [
        'news.yahoo.co.jp',
        'headlines.yahoo.co.jp',
    ]
    start_urls = [
        'http://news.yahoo.co.jp/flash',
    ]

    rules = (
        # ページャーをクロールする（4ページ目まで）
        Rule(LinkExtractor(allow=(r'/flash\?p=[2-4]$', ))),

        # 詳細ページは parse_detail でパースする
        Rule(LinkExtractor(allow=(r'/hl\?a=\d+-\d+-[\w-]+$', )), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = NewsItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="yjXL"]/text()').extract()[0]
        item['description'] = ''.join(response.xpath('//div[@class="ynDetailPgraphWrap clearFix"]/p[@class="ynDetailText"]/text()').extract())
        yield item
