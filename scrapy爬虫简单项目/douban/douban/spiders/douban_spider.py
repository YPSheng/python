# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["douban.com"]
    print("1111111111111111111111")
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):

        for eve in response.xpath('//div[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href'):
            full_url = eve.extract()

            print(full_url)
            yield scrapy.Request(full_url,callback=self.parse_movie)

    def parse_movie(self,response):

         item = DoubanItem()
         item['name'] = response.xpath('//*[@id="content"]/h1/span[1]//text()').extract()
         item['auto'] = response.xpath('//*[@id="info"]/span/span[2]/a/text()').extract()
         item['ping'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()').extract()
         print(item)
         yield item
