# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from pprint import pformat

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Restaurant(scrapy.Item):
    """
    食べログのレストラン情報。
    """

    name = scrapy.Field()
    address = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    station = scrapy.Field()
    score = scrapy.Field()


class BlogPost(scrapy.Item):
    """
    ブログの投稿。
    """

    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    def __repr__(self):
        """
        ログへの出力時に長くなり過ぎないよう、contentを省略して表示する。
        """

        d = dict(self)  # このItemと同じフィールド・値を持つdictを得る。
        if len(d['content']) > 100:
            # 100文字より長い場合は省略する。
            d['content'] = d['content'][:100] + '...'

        return pformat(d)  # dictの文字列表現を返す。


class Page(scrapy.Item):
    """
    Webページ。
    """

    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    def __repr__(self):
        """
        ログへの出力時に長くなり過ぎないよう、contentを省略する。
        """

        p = Page(self)  # このPageを複製したPageを得る。
        if len(p['content']) > 100:
            p['content'] = p['content'][:100] + '...'  # 100文字より長い場合は省略する。

        return super(Page, p).__repr__()  # 複製したPageの文字列表現を返す。
