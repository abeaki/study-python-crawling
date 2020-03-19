# coding: utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

import scrapy

from ..items import NewsItem


class YahooNewsSpider(scrapy.Spider):
    name = 'yahoo_news'
    allowed_domains = [
        'news.yahoo.co.jp',
        'headlines.yahoo.co.jp',
    ]
    start_urls = [
        'http://news.yahoo.co.jp/flash',
    ]

    def parse(self, response):
        print(response.url, response.xpath('//title/text()').extract()[0])
        for a in response.xpath('//ul[@class="listBd"]//p[@class="ttl"]/a'):
            url = a.xpath('@href').extract()[0]
            yield scrapy.Request(url, self.parse_detail)

    def parse_detail(self, response):
        item = NewsItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="yjXL"]/text()').extract()[0]
        item['description'] = ''.join(response.xpath('//div[@class="ynDetailPgraphWrap clearFix"]/p[@class="ynDetailText"]/text()').extract())
        yield item
