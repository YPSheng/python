# -*- coding: utf-8 -*-
import scrapy
import json
from taobaoclass import items
from taobaoclass.items import Iphone,Samsung,Magic,HuaWei,ShouJiKe
import urllib.parse


class TaobaoSpiderSpider(scrapy.Spider):
    name = "taobao_spider"
    totalItem = ['magic','华为mate9']
    allowed_domains = ["taobao.com"]
    start_urls = []
    count = 0
    total = 0
    while(count < 500):
        for eveItem in totalItem:
            count = count + 13
            new_url = 'https://s.taobao.com/api?_ksTS=1488147288907_219&ajax=true&m=customized&q=' + urllib.parse.quote(eveItem) + '&imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8&s=' + str(count) + '&bcoffset=-3'
            start_urls.append(new_url)
    print(start_urls)


    def parse(self, response):
        try:
            html = json.loads(response.body.decode().replace('}}})','}}}').replace("jsonp220(",''))
            for eve in html['API.CustomizedApi']['itemlist']['auctions']:
                print("++++++++++++++++++++++++++++++++++++++++")
                if 'ipad' in str(response.url):
                    items = Iphone()
                    print("ipad")
                elif 'samsung' in str(response.url):
                    items = Samsung()
                    print("Samsung")
                elif 'mate9' in str(response.url):
                    item = HuaWei()
                    print('huawei')
                else:
                    item = ShouJiKe()
                    print('shoujike')
                img = []
                self.total = self.total + 1
                item['title'] = eve['raw_title']
                item['price'] = eve['view_price']
                item['fukuan'] = eve['view_sales']
                item['dizhi'] = eve['item_loc']
                item['url'] = 'https:' + eve['comment_url']
                item['dianpu'] = eve['nick']
                img.append(str('http://' + eve['pic_url']))
                item['image_urls'] = img
                yield item
        except Exception as e:
                print(e)