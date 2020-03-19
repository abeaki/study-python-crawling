# coding: utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

import scrapy
from scrapy.contrib.spiders import XMLFeedSpider

from ..items import NewsItem


class YahooNewsRSSSpider(XMLFeedSpider):
    name = 'yahoo_news_rss'
    allowed_domains = [
        'yahoo.co.jp',
    ]
    start_urls = [
        'http://headlines.yahoo.co.jp/rss/all-bus.xml',
    ]

    def parse_node(self, response, node):
        print(node.extract())
        url = node.xpath('link/text()').extract()[0]
        yield scrapy.Request(url, self.parse_detail)

    def parse_detail(self, response):
        item = NewsItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="yjXL"]/text()').extract()[0]
        item['description'] = ''.join(response.xpath('//div[@class="ynDetailPgraphWrap clearFix"]/p[@class="ynDetailText"]/text()').extract())
        yield item
