# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyFullName =  Field() # 公司名字
    # print(info['公司名字'])
    city = Field()  # 职位城市
    positionName = Field()  # 招聘职位
    formatCreateTime = Field()  # 发布时间
    salary = Field()  # 薪资待遇
    workYear = Field()  # 经验要求
    Jobdescriptions = Field()    #职位描述
    companySize = Field()  # 公司大小
    positionAdvantage = Field()  # 公司福利
    district = Field()          #公司地址
    companyhref = Field()       #公司链接