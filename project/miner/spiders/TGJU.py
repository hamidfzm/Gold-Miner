# -*- coding: utf-8 -*-
__author__ = 'Hamid FzM'

# python import
from scrapy import Item, Spider
# project import
from miner.items import Gold


class tgjuSpider(Spider):
    name = "tgju"
    allowed_domains = ["tgju.org"]
    start_urls = [
        "http://www.tgju.org/"
    ]

    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        for item in response.css('#gold-table tbody tr'):
            gold = Gold()
            gold['title'] = '|'.join(item.xpath('th/text()').extract())
            data = item.xpath('td//text()').extract()
            gold['price'] = data[0]
            gold['tolerance'] = data[1]
            gold['min'] = data[2]
            gold['max'] = data[3]
            gold['time'] = data[4]
            yield gold