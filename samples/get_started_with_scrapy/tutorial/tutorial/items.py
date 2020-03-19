# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import re

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()

    def __repr__(self):
        text = super(NewsItem, self).__repr__()
        return re.sub(r'\\u([0-9a-f]{4})', lambda x: unichr(int('0x' + x.group(1), 16)), text)
