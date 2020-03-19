# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import re

import scrapy


class UsedCarItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()

    def __repr__(self):
        text = super(UsedCarItem, self).__repr__()
        return re.sub(r'\\u([0-9a-f]{4})', lambda x: unichr(int('0x' + x.group(1), 16)), text)
