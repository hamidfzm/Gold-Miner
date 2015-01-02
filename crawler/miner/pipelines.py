# -*- coding: utf-8 -*-

# python import
from scrapy import signals, log
from scrapy.contrib.exporter import JsonItemExporter
from datetime import datetime
import os

# project import
from items import tgju
from pymongo import MongoClient


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


def get_items(module):
    md = module.__dict__
    return (str(md[c].__name__) for c in md if (isinstance(md[c], type) and md[c].__module__ == module.__name__))


class JsonPipeline(object):
    def __init__(self):
        self.files = dict()
        self.exporter = dict()

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        for key in get_items(tgju):
            path = os.path.join('temp', key)
            if not os.path.exists(path):
                os.makedirs(path)
            self.files[key] = open(os.path.join(path,
                                                '%s_%s_%s.json' % (spider.name,
                                                                   key.lower(),
                                                                   datetime.now().strftime('%Y%m%dT%H%M%S'))),
                                   'w+b')

            self.exporter[key] = JsonItemExporter(self.files[key])
            self.exporter[key].start_exporting()

    def spider_closed(self, spider):
        for key in get_items(tgju):
            self.exporter[key].finish_exporting()
            self.files.pop(key).close()

    def process_item(self, item, spider):

        try:
            log.msg('-----------------%s------------------' % item.__class__.__name__)
            self.exporter[item.__class__.__name__].export_item(item)
        except KeyError:
            pass
        return item


class tgjuPipeline(object):
    def __init__(self):
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.tgju

    def spider_closed(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[item.__class__.__name__.lower()].update({'title': item['title']}, dict(item), True)
        return item