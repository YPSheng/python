# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from taobao.items import Iphone,Samsung,Magic,HuaWei,ShouJiKe


class TaobaoclassPipeline(object):
    def process_item(self, item, spider):
        host = settings('MONGODB_HOST')
        port = settings('MONGODB_PORT')
        dbName = settings('MONGODB_DBNAME')
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbName]

        if isinstance(item,Iphone):
            self.post = tdb[settings['MONGODB_DOCNAME_IP']]
        elif isinstance(item, Samsung):
            self.post = tdb[settings['MONGODB_DOCNAME_SAM']]
        elif isinstance(item, HuaWei):
            self.post = tdb[settings['MONGODB_DOCNAME_HW']]
        elif isinstance(item, ShouJiKe):
            self.post = tdb[settings['MONGODB_DOCNAME_SJK']]
        elif isinstance(item, Magic):
            self.post = tdb[settings['MONGODB_DOCNAME_MAG']]
        taobao = dict(item)
        self.post.insert(taobao)

        return item
