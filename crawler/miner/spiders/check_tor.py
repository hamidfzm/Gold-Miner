# -*- coding: utf-8 -*-
__author__ = 'Hamid FzM'

# python import
from scrapy import Spider
# project import


class TorSpider(Spider):
    name = "tor"
    allowed_domains = ["torproject.org"]
    start_urls = [
        "https://check.torproject.org/"
    ]

    def parse(self, response):
        print(response.body)