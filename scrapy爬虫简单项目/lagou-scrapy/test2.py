import scrapy
from bs4 import BeautifulSoup
import json
# from scrapy.conf import settings
# from ..items import LagouItem
occupation_list = []
import requests
class LagouspiderSpider:
    # name = "lagouspider"
    # allowed_domains = ["lagou.com"]
    # start_urls = ['https://www.lagou.com/']
    # cookie = settings['COOKIE']
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
    # def __init__(self,name=None,**kwargs):
    #     super(LagouspiderSpider,self).__init__(name,**kwargs)

    def parse(self):
        # for i in range(1,8):
        #     occos = response.xpath('//*[@id="sidebar"]/div/div[{}]/div/dl/dd/a/text()'.format(i)).extract()
        #     for occo in occos:
        #         url = "https://www.lagou.com/jobs/list_{}?px=default&city=%E5%85%A8%E5%9B%BD#filterBox".format('java')
        #         yield scrapy.Request(url,callback=self.parse_page)
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0'
        for i in range(20):
            data = {
                'first':'true',
                'pn':'1',
                'kd':'java'
            }
            response = requests.post(url, data=data, headers=self.headers)
            print(response.text)
            # yield scrapy.FormRequest(url=url, callback=self.parse_page, formdata=data, headers=self.headers)
            # for i in json.loads(response.text).keys():
            #     print(i)
            # if  'resultId' in json.loads(response.text).keys():
            #     for i in json.loads(response.text).get('resultId').get('result'):
            #         print(i)
l  = LagouspiderSpider()
l.parse()