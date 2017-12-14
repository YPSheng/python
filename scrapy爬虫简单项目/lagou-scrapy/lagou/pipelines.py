# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

#存储到mongodb数据库
class LagouPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE','items')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient()
        self.db = self.client['lagouzhiwei']

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db['zhiweitest2'].insert(dict(item))
