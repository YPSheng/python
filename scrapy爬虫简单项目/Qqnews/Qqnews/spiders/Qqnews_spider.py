# -*- coding: utf-8 -*-
import scrapy

from Qqnews.items import QqnewsItem


class QqnewsSpiderSpider(scrapy.Spider):
    name = "Qqnews_spider"
    allowed_domains = ["qq.com"]
    start_urls = ['http://mil.qq.com/mil_index.htm']

    def parse(self, response):
        for eveUrl in response.xpath('//a[@class="linkto"]/@href'):
            yield scrapy.Request(eveUrl.extract(),callback=self.parse_content)


    def parse_content(self,response):
        item = QqnewsItem()
        title = response.xpath('//div[@class="hd"]/h1/text()').extract()
        date1 = response.xpath('//span[@class="a_time"]/text()').extract()
        date2 = response.xpath('//div[@class="md"]/text()').extract()
        date3 = response.xpath('//div[@class="time"]/text()').extract()
        date = str(date1)+str(date2)+str(date3)
        author = response.xpath('//div[@class="content-article"]/p[1]/text()').extract()
        content = response.xpath('//div[@class="content-article"]/text()').extract()
        print(title,date,author,content)
        yield item
