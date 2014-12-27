# -*- coding: utf-8 -*-

# python import
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter

# project import
import items

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


def get_items(module):
    md = module.__dict__
    return (str(md[c].__name__) for c in md if (isinstance(md[c], type) and md[c].__module__ == module.__name__))


class tgjuPipeline(object):
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
        for key in get_items(items):
            self.files[key] = open('%s_%s.json' % (spider.name, key), 'w+b')
            self.exporter[key] = JsonItemExporter(self.files[key])
            self.exporter[key].start_exporting()

    def spider_closed(self, spider):
        for key in get_items(items):
            self.exporter[key].finish_exporting()
            self.files.pop(key).close()

    def process_item(self, item, spider):

        try:
            self.exporter[item.__class__.__name__].export_item(item)
        except KeyError:
            pass
        return item
