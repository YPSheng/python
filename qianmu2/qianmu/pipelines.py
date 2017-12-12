# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem
import redis

# logger = logger.Lo


class CheckPipeline(object):
    def process_item(self, item, spider):
        if item['undergraduate_num']  or item['postgraduate_num']:
            return item
        raise DropItem('Miss %s'%item['name'])

class RedisPipeline(object):
    def __init__(self):
        self.r = redis.Redis(host='localhost',port=7777,db=0)

    def process_item(self,item,spider):
        self.r.sadd(spider.name,item['name'])
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conne = None
        self.cur = None
    def open_spider(self,spider):

        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='rock1204',
            db='qianmu',
            charset='utf8'
    )
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        cols = item.keys()
        values = [item[col] for col in cols]
        cols = ['`%s`' % col for col in cols]
        sql = "INSERT INTO `universities` ("+','.join(cols) + ") VALUES ("+','.join(["%s"]*8) + ")"
        self.cur.execute(sql,values)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()