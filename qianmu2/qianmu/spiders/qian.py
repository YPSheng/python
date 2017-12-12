# -*- coding: utf-8 -*-
import scrapy
from ..items import QianmuItem
from scrapy_redis.spiders import RedisSpider

def filter(html):
    return html.replace('\t','').replace('\r\n','')

class QianSpider(scrapy.Spider):
    name = 'qian'
    allowed_domains = ['140.143.192.76']
    start_urls = ['http://140.143.192.76:8002/2018USNEWS世界大学排名']

    def __init__(self,name=None,max_num=0,**kwargs):
        super(QianSpider,self).__init__(name,**kwargs)
        self.logger.info('max crawl pages set %s '%max_num)
        self.max_num = int(max_num)


    def parse(self,response):
        links = response.xpath('//*[@id="content"]/table//tr/td[2]/a/@href').extract()
        for num,i in enumerate(links):
            # print(i)
            if self.max_num and self.max_num <= num:
                break
            if not i.startswith('http://'):
                i = 'http://140.143.192.76:8002/%s' % i
            request = scrapy.Request(i,callback=self.parse_uni)
            request.meta['rank'] = num+1
            # print(i)
            yield request
    def parse_uni(self,response):
        response = response.replace(body=filter(response.text))
        self.logger.info(response.url)
        wiki = response.xpath('//div[@id="wikiContent"]')[0]
        name = response.xpath('//*[@class="wikiTitle"]/text()').extract_first()
        # item = dict(num=response.meta['rank'],title=name)
        keys = wiki.xpath('./div[@class="infobox"]/table/tbody/tr/td[1]/p/text()').extract()
        cols = wiki.xpath('./div[@class="infobox"]/table/tbody/tr/td[2]')
        values = [','.join(col.xpath('.//text()').extract()) for col in cols]
        item = QianmuItem()
        data = dict(zip(keys,values))
        item['name'] = name
        item['rank'] = response.meta['rank']
        item['country'] = data.get(u'国家','')
        item['state'] = data.get(u'州省','')
        item['city'] = data.get(u'城市','')
        item['undergraduate_num'] = data.get(u'本科生人数','')
        item['postgraduate_num'] = data.get(u'研究生人数','')
        item['website'] = data.get(u'网址','')
        self.logger.warning("item %s scraped" % item)
        yield item
