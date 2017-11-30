# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoclassItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    fukuan = scrapy.Field()
    dizhi = scrapy.Field()
    url = scrapy.Field()
    dianqu = scrapy.Field()

class Iphone(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    fukuan = scrapy.Field()
    dizhi = scrapy.Field()
    url = scrapy.Field()
    dianqu = scrapy.Field()

class Samsung(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    fukuan = scrapy.Field()
    dizhi = scrapy.Field()
    url = scrapy.Field()
    dianqu = scrapy.Field()



class HuaWei(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    fukuan = scrapy.Field()
    dizhi = scrapy.Field()
    url = scrapy.Field()
    dianqu = scrapy.Field()


class Magic(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    fukuan = scrapy.Field()
    dizhi = scrapy.Field()
    url = scrapy.Field()
    dianqu = scrapy.Field()



class ShouJike(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    fukuan = scrapy.Field()
    dizhi = scrapy.Field()
    url = scrapy.Field()
    dianqu = scrapy.Field()
