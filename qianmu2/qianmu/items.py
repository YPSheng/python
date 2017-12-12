# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#简单处理数据
def convert_int(s):
    if isinstance(s,int):
        return s
    if not s:
        return 0
    return int(s.strip().replace(',', ''))

class QianmuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    #对数据进行简单处理
    rank = scrapy.Field(serializer=convert_int)
    country = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    undergraduate_num = scrapy.Field()
    postgraduate_num = scrapy.Field()
    website = scrapy.Field()

if __name__ == '__main__':
    q = QianmuItem()
    #打印所有定义字段
    print(q.fields.keys())
    #打印所有的fields及其序列化函数
    print(q.fields)
    #判断某个item对象是否包含指定字段
    print('name' in q.fields)
    #判断某个字段是否设置了值
    print('name' in q)
