# -*- coding: utf-8 -*-
import scrapy


class Dbtop250SpiderSpider(scrapy.Spider):
    name = "dbtop250_spider"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    conunt = 0
    def parse(self, response):
        self.conunt +=1
        for eve in response.xpath('//div[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href'):
            full_url = eve.extract()
            yield scrapy.Request(full_url,callback=self.parse_movie)

        if self.conunt * 25 < 250:
            full_url = 'https://movie.douban.com/top250?start={}&filter='.format(str(self.conunt*25))
            yield scrapy.Request(full_url,callback=self.parse)
    def parse_movie(self,response):
        from dbtop250.items import Dbtop250Item
        item = Dbtop250Item()
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        # item['auto'] = response.xpath('//*[@id="info"]/span/span[2]/a/text()').extract()
        item['ping'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()').extract()
        yield item
