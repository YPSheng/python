# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
class QqnewsPipeline(object):

    def __init__(self):
        MONGODN_HOST = settings['MONGODB_HOST']
        MONGODB_PORT = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        MONGODB_CNAME = settings['MONGODB_CNAME']
        client = pymongo.MongoClient(host=MONGODN_HOST,port=MONGODB_PORT)
        tdb = client[dbName]
        self.post = tdb[MONGODB_CNAME]
    def process_item(self, item, spider):
        news = dict(item)
        self.post.insert(news)
        return item
