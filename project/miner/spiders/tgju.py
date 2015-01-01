# -*- coding: utf-8 -*-
__author__ = 'Hamid FzM'

# python import
from scrapy import Spider
# project import
from miner.items.tgju import Gold, Coin, Others, Market


class tgjuSpider(Spider):
    name = "tgju"
    allowed_domains = ["tgju.org"]
    start_urls = [
        "http://www.tgju.org/"
    ]

    def parse(self, response):
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

        for item in response.css('#coin-table tbody tr'):
            coin = Coin()
            coin['title'] = '|'.join(item.xpath('th/text()').extract())
            data = item.xpath('td//text()').extract()
            coin['price'] = data[0]
            coin['tolerance'] = data[1]
            coin['min'] = data[2]
            coin['max'] = data[3]
            coin['time'] = data[4]
            yield coin

        for item in response.css('#other-table tbody tr'):
            others = Others()
            others['title'] = '|'.join(item.xpath('th/text()').extract())
            data = item.xpath('td//text()').extract()
            others['price'] = data[0]
            others['tolerance'] = data[1]
            others['min'] = data[2]
            others['max'] = data[3]
            others['time'] = data[4]
            yield others

        for item in response.css('.market tbody tr'):
            market = Market()
            market['title'] = '|'.join(item.xpath('th/text()').extract())
            data = item.xpath('td//text()').extract()
            market['indicator'] = data[0]
            market['tolerance'] = data[1]
            yield market