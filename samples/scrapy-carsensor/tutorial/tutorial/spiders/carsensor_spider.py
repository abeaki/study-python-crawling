# coding: utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from scrapy.contrib.spiders import SitemapSpider

from ..items import UsedCarItem


class CarSensorSpider(SitemapSpider):
    name = 'carsensor'
    allowed_domains = [
        'www.carsensor.net',
    ]
    sitemap_urls = [
        'http://www.carsensor.net/usedcar/sitemaps_index.xml',
    ]
    sitemap_rules = [(r'/usedcar/detail/.*/index\.html', 'parse_used_car')]

    def parse_used_car(self, response):
        item = UsedCarItem()
        item['url'] = response.url
        item['name'] = response.css('h2[itemprop="name"]').xpath('text()').extract()[0]
        item['price'] = response.css('h2[itemprop="price"]').xpath('@content').extract()[0]
        yield item
