# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json
from scrapy.conf import settings
from ..items import LagouItem
import requests

occupation_list = []

class LagouspiderSpider(scrapy.Spider):
    name = "lagouspider"
    allowed_domains = ["lagou.com"]
    start_urls = ['https://www.lagou.com']
    cookie = settings['COOKIE']
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '25',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'user_trace_token=20171016205119-74af5f4b-4f58-445f-9516-f8c19f475243; LGUID=20171016205145-c44d7b22-b270-11e7-991d-525400f775ce; JSESSIONID=ABAAABAAAIAACBIB57C77C4ECB2518EE2D0B9135B108E91; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=http%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E9%2592%25A9%26rsv_spt%3D1%26rsv_iqid%3D0xaa9b6e5d00013b57%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3D%26tn%3Dbaiduhome_pg%26ch%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; _putrc=54D6D44AC87A2A52; login=true; unick=%E6%9D%A8%E9%B9%8F%E5%8D%87; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=2; _ga=GA1.2.358203920.1509241265; _gid=GA1.2.1325253718.1511828511; LGSID=20171128082152-21c7cb9f-d3d2-11e7-ae6a-525400f775ce; LGRID=20171128082206-2a422523-d3d2-11e7-ae6a-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510323969,1511253705,1511253729,1511828514; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511828527; SEARCH_ID=8267a0cd29464ff6b38f86b1d1e17b96; index_location_city=%E5%8C%97%E4%BA%AC',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': "h'ttps://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }


    def parse(self, response,pn=1):
        #获取所有职位
        for i in range(1,8):
            occos = response.xpath('//*[@id="sidebar"]/div/div[{}]/div/dl/dd/a/text()'.format(i)).extract()
            for occo in occos:
                # url = "https://www.lagou.com/jobs/list_{}?px=default&city=%E5%85%A8%E5%9B%BD#filterBox".format('java')
                # yield scrapy.Request(url,callback=self.parse_page)
                occu_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0'
                data = {
                    'first':'true',
                    'pn':pn,
                    'kd':'java'
                }
                #获取返回的json数据
                response = requests.post(occu_url, data=data, headers=self.headers)
                # positionIds = json.loads(response.text).get('content').get('positionResult').get('result')
                try:
                    pageSize = json.loads(response.text).get('content').get('pageSize')
                    totalCount = json.loads(response.text).get('content').get('positionResult').get('totalCount')
                except json.decoder.JSONDecodeError:
                    continue
                #获取总页数
                if int(totalCount) % int(pageSize) == 0:
                    pages = int(int(totalCount)/int(pageSize))
                else:
                    pages = int(int(totalCount)/int(pageSize)) + 1

                for page in range(int(pages)):
                    pn = page + 1
                    occu_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0'
                    data = {
                        'first': 'true',
                        'pn': pn,
                        'kd': occo
                    }
                   
                    response = requests.post(occu_url, data=data, headers=self.headers)
                   
                    try:
                        if 'content' in json.loads(response.text).keys():
                            positionIds = json.loads(response.text).get('content').get('positionResult').get('result')


                        for positionId in positionIds:
                            # try:
                            position = positionId.get('positionId')
                            # except:
                            #     continue
                            # print(positionId)
                            item = LagouItem()
                            # self.item = info
                            item['companyFullName'] = positionId['companyFullName']  # 公司名字
                            # print(info['公司名字'])
                            item['city'] = positionId['city']  # 职位城市
                            item['positionName'] = positionId['positionName']  # 招聘职位
                            item['formatCreateTime'] = positionId['formatCreateTime']  # 发布时间
                            item['salary'] = positionId['salary']  # 薪资待遇
                            item['workYear'] = positionId['workYear']  # 经验要求
                            item['companySize'] = positionId['companySize']  # 公司大小
                            item['positionAdvantage'] = positionId['positionAdvantage']  # 公司福利
                            item['district'] = positionId['district']  # 公司地址
                            info_url = "https://www.lagou.com/jobs/{}.html".format(position)
                            # item = LagouItem()
                            # item['companyhref'] = info_url
                            print(item)
                            yield item
                            # yield scrapy.Request(url=info_url, callback=self.parse_fina)
                    except json.decoder.JSONDecodeError:
                        continue
                    except TimeoutError:
                        continue
                        # print(info_url)
                        # yield item

    #获取详细页面的信息，这里试验了，很慢，只获取了页面链接,我就只获取了json数据里面的信息，大部门差不多了
    # def parse_fina(self,response):
    #             item = LagouItem()
        # response = response.text
        # print(response.status)
        # if response.status == 200:
        #     try:
        #         item['companyFullName'] = response.xpath('//*[@id="job_company"]/dt/a/img/@alt').extract()  # 公司名字

            # print(info['公司名字'])
            #     item['city'] = response.xpath('/html/body/div[2]/div/div[1]/dd/p[1]/span[2]/text()').extract()  # 职位城市
            #     item['positionName'] = response.xpath('/html/body/div[2]/div/div[1]/div/span/text()').extract() # 招聘职位
            #     item['formatCreateTime'] = response.xpath('/html/body/div[2]/div/div[1]/dd/p[2]/text()').extract() # 发布时间
            #     item['salary'] = response.xpath('/html/body/div[2]/div/div[1]/dd/p[1]/span[1]/text()').extract()  # 薪资待遇
            #     item['workYear'] = response.xpath('/html/body/div[2]/div/div[1]/dd/p[1]/span[3]/text()').extract()[0]  # 经验要求
            #     item['Jobdescriptions'] = response.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()').extract()  # 职位描述
            #     item['companySize'] = response.xpath('//*[@id="job_company"]/dd/ul/li[3]/text()').extract()  # 公司大小
                # item['positionAdvantage'] = response.xpath('//*[@id="job_detail"]/dd[1]/p/text()').extract()  # 公司福利
                # item['district'] = response.xpath('//*[@id="job_detail"]/dd[3]/div[1]/a/text()').extract()  # 公司地址
                # item['companyhref'] = response.xpath('//*[@id="job_company"]/dd/ul/li[4]/a/@href').extract()  # 公司链接
            # except IndexError:
            #     pass
            #     print(item)
            #     yield item