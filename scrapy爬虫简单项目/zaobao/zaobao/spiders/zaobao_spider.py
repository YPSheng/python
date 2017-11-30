# -*- coding: utf-8 -*-
import scrapy

from zaobao.items import ZaobaoItem


class ZaobaoSpiderSpider(scrapy.Spider):
    name = "zaobao_spider"
    allowed_domains = ["zaobao.com"]
    start_urls = ['http://zaobao.com/']

    def parse(self, response):
        for eve in response.xpath('//*[@id="DressUp]/div/div/div/div/a/@href'):
            full_url = response.urljoin(eve.extract())
            yield scrapy.Request(full_url,callback=self.parse_news)

    def parse_news(self,response):
        item = ZaobaoItem()
        item['name'] = response.xpath('//*[@id="MainCourse"]/div/h1/text()').extract()
        item['url'] = response.xpath('//*[@id="MainCourse]/div/div[2]').extract()
        print(item)
        yield item