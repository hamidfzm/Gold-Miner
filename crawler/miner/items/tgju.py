# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Gold(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    price = Field()
    tolerance = Field()
    min = Field()
    max = Field()
    time = Field()


class Coin(Gold):
    pass


class Others(Gold):
    pass


class Market(Item):
    title = Field()
    indicator = Field()
    tolerance = Field()


class Currency(Item):
    title = Field()
    price = Field()
    tolerance = Field()