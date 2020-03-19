# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = "news1"
    allowed_domains = ["news.yahoo.co.jp"]
    start_urls = (
        'http://www.news.yahoo.co.jp/',
    )

    def parse(self, response):
        pass
