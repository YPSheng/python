#coding:utf-8
import ssl
from urllib import parse
import re
import requests
import json
import urllib

#
ssl._create_default_https_context = ssl._create_unverified_context
# headers = {
#             'Cookie':'JSESSIONID=95820ECC00B038495AC43E949F6D4A69; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=351273482.64545.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2017-10-25; _jc_save_toDate=2017-10-20; _jc_save_wfdc_flag=dc',
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# }

# 获取所有的站点信息
def get_station():
    url = 'http://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9028'
    response = urllib.request.urlopen(url).read()
    # print(response)
    return response.decode("utf-8")

#获取出发点和终点站的信息
def station(stationinfo,star,end):
    str2 = stationinfo[20:][:-2]
    str3 = str2.split('|')
    order1 = str3.index(star)
    order2 = str3.index(end)
    starstation = str3[int(order1) + 1]
    endstation= str3[int(order2) + 1]
    return starstation,endstation

# 获取列车信息
def getTrainInfo(start,end,date):

    # params = {
    train_date = date
    from_station = start
    to_station = end
    purpose_codes = 'ADULT'
    # }
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes={}'.format(train_date,from_station,to_station,purpose_codes)
    # print(url)
    headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                    'Cookie':'JSESSIONID=B201655CD8BCF12D53ADF6CA6D2AA050; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=770703882.38945.0000; BIGipServerpool_passport=367854090.50215.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2017-10-25; _jc_save_toDate=2017-10-21; _jc_save_wfdc_flag=dc'

    }
    response = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(response).read()
    # response = response.urlopen()
    return response.decode("utf-8")

# 获取价钱信息，打印列车的所有信息
def getTicketInfo(getTrainInfos,train_date,stationinfo):
    # print(getTrainInfos)
    getTrainInfos = json.loads(getTrainInfos).get('data').get('result')

    for getTrainInfo in getTrainInfos:
        order3 = getTrainInfo.split('|')
        train_no = order3[2]
        seat_types = str(order3[-1:])[2:5]
        if len(seat_types) != 3 :
            continue
        from_station_no = str(order3[1:][15])
        to_station_no = str(order3[1:][16])
        url  = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no={}&from_station_no={}&to_station_no={}&seat_types={}&train_date={}'.format(train_no,from_station_no,to_station_no,seat_types,train_date)
        # url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=26000K772632&from_station_no=10&to_station_no=11&seat_types=113&train_date=2017-10-25'
        headers = {
                      'Accept':'* / *',
                      'Accept - Encoding':'gzip, deflate, br',
                      'Accept - Language':'zh - CN, zh;q = 0.8',
                      'Cache - Control':'no - cache',
                      'Connection':'keep - alive',
                      'Host':'kyfw.12306.cn',
                      'If - Modified - Since':'0',
                      'Referer:https':'// kyfw.12306.cn / otn / leftTicket / init',
                      'X - Requested - With':'XMLHttpRequest',
                      'Cookie': 'JSESSIONID = B201655CD8BCF12D53ADF6CA6D2AA050;route = 495c805987d0f5c8c84b14f60212447d;BIGipServerotn = 770703882.38945.0000;BIGipServerpool_passport = 367854090.50215.0000;_jc_save_fromStation = % u5317 % u4EAC % 2BJP;_jc_save_toStation = % u5929 % u6D25 % 2TJP;_jc_save_fromDate = 2017 - 10 - 25;_jc_save_toDate = 2017 - 10 - 21;_jc_save_wfdc_flag = dc',
                      'User - Agent':' Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36'
        }
        response = urllib.request.urlopen(url).read()
        datas = response.decode("utf-8")
        com = re.compile('({.*?}})')
        datas = com.findall(datas)
        for data in datas:
            if len(data) > 30:
                data = json.loads(data)
                # print(data)
                datas = data.get('data')
                print("------------------本次列车-----------------------------------")
                print('本次列车', order3[3])

                str2 = stationinfo[20:][:-2]
                str3 = str2.split('|')
                order1 = str3.index(order3[4])
                order2 = str3.index(order3[7])
                starstation = str3[int(order1) - 1]
                endstation = str3[int(order2) - 1]

                print('出发站点', starstation)
                print('到达站点', endstation)
                print('出发时间', order3[8])
                print('到达时间', order3[9])
                print('历时时间', order3[10])
                # print(type(datas))
                for k in datas:

                    if k == 'A9':
                        print('商务座特等座',"：",datas[k])
                    elif k == 'M':
                        print("一等座","：",datas[k])
                    elif k == 'O':
                        print("二等座","：",datas[k])
                    elif k == 'WZ':
                        print("无座","：",datas[k])
                    elif k == 'A4':
                        print("软卧", "：", datas[k])
                    elif k == 'WZ':
                        print("无座", "：", datas[k])
                    elif k == 'F':
                        print("动卧", "：", datas[k])
                    elif k == 'A3':
                        print("硬卧", "：", datas[k])
                    elif k == 'A1':
                        print("硬座", "：", datas[k])
                    elif k == 'A6':
                        print("高级软卧", "：", datas[k])
                    elif k == 'OT':
                        print("其他", "：", datas[k])

if __name__ == "__main__":
    start = input('出发车站:')
    end = input('到达车站:')
    date = input("出发时间(如2017.10.25):")
    # 处理时间格式
    date = date.replace('.','-')
    stationinfo = get_station()
    starstation,endstation  = station(stationinfo,start,end)
    getTrainInfo = getTrainInfo(starstation,endstation,date)
    getTicketInfo(getTrainInfo,date,stationinfo)











