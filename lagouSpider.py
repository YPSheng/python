import json
import os
import random
import urllib
import requests
from bs4 import BeautifulSoup
import time
import csv
import codecs
from selenium import webdriver


headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Length':'25',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'user_trace_token=20171016205119-74af5f4b-4f58-445f-9516-f8c19f475243; LGUID=20171016205145-c44d7b22-b270-11e7-991d-525400f775ce; JSESSIONID=ABAAABAAAIAACBIB57C77C4ECB2518EE2D0B9135B108E91; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=http%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E9%2592%25A9%26rsv_spt%3D1%26rsv_iqid%3D0xaa9b6e5d00013b57%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3D%26tn%3Dbaiduhome_pg%26ch%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; _putrc=54D6D44AC87A2A52; login=true; unick=%E6%9D%A8%E9%B9%8F%E5%8D%87; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=2; _ga=GA1.2.358203920.1509241265; _gid=GA1.2.1325253718.1511828511; LGSID=20171128082152-21c7cb9f-d3d2-11e7-ae6a-525400f775ce; LGRID=20171128082206-2a422523-d3d2-11e7-ae6a-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510323969,1511253705,1511253729,1511828514; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511828527; SEARCH_ID=8267a0cd29464ff6b38f86b1d1e17b96; index_location_city=%E5%8C%97%E4%BA%AC',
        'Host':'www.lagou.com',
        'Origin':'https://www.lagou.com',
        'Referer':"h'ttps://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token':'None',
        'X-Requested-With':'XMLHttpRequest'
}

#访问网页  获取所有的json数据
def post(url,para,headers=None,proxy=None,timeOut=5,timeOutRetry=5):
    if not url or not para:
        print("PostError url or para not exit")
        print("11111111111111")
        return None
    try:
        if not headers:
            headers=headers
        response = requests.post(url,data=para,headers=headers)
        print(response.status_code)

        print(response.text)
        if response.status_code == 200 or response.status_code == 302:
            htmlCode =  response.text
            # print('1111111111')
        else:
            print("2222222222222")
            htmlCode = None
    except Exception as e:
        if timeOutRetry > 0:
            htmlCode = post(url=url,para=para,timeOutRetry=(timeOutRetry-1))
            print('3333333333333333333333333333')
            htmlCode = None
    return htmlCode

# url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
# url = 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC'
#对获取的json数据进行处理，获取自己需要的信息，获取每个职位数据页数，
def getinfo(url,para):

    htmlCode = post(url,para=para,headers=headers)   #获取到网页源码,一大堆的json数据
    if htmlCode == None:
        return False
    companies = json.loads(htmlCode).get('content').get('positionResult').get('result')
    totalCount = json.loads(htmlCode).get('content').get('positionResult').get('totalCount')
    pagesize = json.loads(htmlCode).get('content').get('pageSize')
    pages = 0
    if int(totalCount)%int(pagesize) == 0:
        pages = int(int(totalCount)/int(pagesize))
    else:
        pages = int(int(totalCount) // int(pagesize)) + 1

    return pages,companies

#写入文件中，不同的职位保存在不同的文件
def writeCsv(filename,companies):
    info = {}
    csv_file = codecs.open(filename+'.csv', 'ab', 'utf-8', 'ignore')
    csv_writer = csv.writer(csv_file)
    for i in companies:
        info['公司名字'] = i['companyFullName']              #公司名字
        # print(info['公司名字'])
        info['公司城市'] = i['city']                        #职位城市
        info['招聘职位'] = i['positionName']              #招聘职位
        info['发布时间'] = i['formatCreateTime']              #发布时间
        info['薪资待遇'] = i['salary']              #薪资待遇
        info['经验要求'] = i['workYear']              #经验要求
        info['公司大小'] = i['companySize']              #公司大小
        info['公司福利'] = i['positionAdvantage']              #公司福利
        info['公司地址'] = i['district']              #公司地址
        # print(info)
        csv_writer.writerow([i['companyFullName'],i['city'],i['positionName'],i['formatCreateTime'],i['salary'],
                            i['workYear'],i['companySize'],i['positionAdvantage'],i['district']])



#获取所有的职位信息
def occupation():
    url = "https://www.lagou.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ds = soup.find_all("div", attrs=["_class", "menu_sub dn"])

    occupation_list = []
    for h in ds:
        for g in h.find_all('dd'):
            for l in g:
                if l.string != "\n":
                    occupation_list.append(l.string)

    # print(occupation_list)
    # print(len(occupation_list))
    return occupation_list

#获取热门城市这些职位的信息
if __name__ == '__main__':
    occu_list = occupation()
    city_list = ['北京','上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门','长沙','苏州','天津']
    for l in occu_list[:]:
        print(l)
        for j in city_list:
            url = 'https://www.lagou.com/jobs/positionAjax.json?'
            para = {'px': 'default','city':j,'needAddtionalResult': 'false', 'isSchoolJob': 0, 'first': 'true', 'pn': '1',
                    'kd':l}
            pages,companies = getinfo(url,para)
            for i in range(pages):
                para['pn'] = str(i+1)
                time.sleep(random.random()*5)
                print('开始爬取第%s页'%str(i+1))
                try:
                    pages,companies = getinfo(url,para)
                except:
                    continue
                # fina = writeCsv(companies)
                if companies == None:
                    break
                writeCsv(l,companies)
                # csv_writer.writerow(fina)
