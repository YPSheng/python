# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import spider,Request
from ..items import ZhihuuserItem

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    #粉丝列表
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        # url = 'https://www.zhihu.com/api/v4/members/wang-qing-qing-70-81?include=allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
        yield Request(self.user_url.format(user = self.start_user, include = self.user_query), self.parse_user)
        yield Request(self.follows_url.format(user = self.start_user, include = self.follows_query,offset = 0, limit = 20), callback = self.parse_follows)

    #用户个人信息
    def parse_user(self, response):
        result = json.loads(response.text)
        item = ZhihuuserItem()
        for field in item.fields:
            #如果定义的item是获取的键名之一，就赋值
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(self.user_url.format(user = result.get('url_token'), include=self.follows_query, limit=20, offset = 0),callback = self.parse_follows)
        yield Request(self.follows_url.format(user = result.get('url_token'), include=self.follows_query, limit=20, offset = 0),callback = self.parse_followers)
        yield Request(self.followers_url.format(user = result.get('url_token'), include=self.follows_query, limit=20, offset = 0),callback = self.parse_followers)

    #关注着信息
    def parse_follows(self,response):

        results = json.loads(response.text)

        #先判断data键名是否存在
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user = result.get('url_token'), include = self.user_query), callback = self.parse_user)

        #获取下一页链接，然后继续对下一页数据进行处理
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_follows)

    #粉丝信息
    def parse_followers(self, response):

        results = json.loads(response.text)

        # 先判断data键名是否存在
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              callback=self.parse_user)

        # 获取下一页链接，然后继续对下一页数据进行处理
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)