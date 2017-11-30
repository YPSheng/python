import urllib
import json
import requests


url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=10.0.144.241&co=&resource_id=6006&t=1484574592369&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110205057557444126394_1484574357057&_=1484574357071'

headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Cookie':'BAIDUID=4812092AE366ED4A55C6D8EA6713A635:FG=1; PSTM=1508161904; BIDUPSID=18C54752D18DC057B004465161A28981; BDUSS=9XM0M3bnJBYUpRZVBFRDRRWXdpVXdIa0d2WDRJUlVFaVlJcFVSMnVFOE5MUkJhSVFBQUFBJCQAAAAAAAAAAAEAAAC6uzCj0KHKqNfTczAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA2g6FkNoOhZQ2; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
            'Host':'sp0.baidu.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
ip = input("请输入你的IP地址：")
params = {
            'query':ip,
            'co':'',
            'resource_id':'6006',
            't':'1484574592369',
            'ie':'utf8',
            'oe':'gbk',
            'cb':'op_aladdin_callback',
            'format':'json',
            'tn':'baidu',
            'cb':'jQuery110205057557444126394_1484574357057',
            '_':'1484574357071'
}

response = requests.get(url,params=params).text
# print(response)
response = json.loads(response[46:][:-2])
# print(response[46:][:-2])
print("location:"+response.get('data')[0].get("location"))
print("titlecont:"+response.get('data')[0].get("titlecont"))
print("origip:"+response.get('data')[0].get("origip"))
print("origipquery:"+response.get('data')[0].get("origipquery"))
print("showlamp:"+response.get('data')[0].get("showlamp"))
print("showLikeShare:"+str(response.get('data')[0].get("showLikeShare")))
print("shareImage:"+str(response.get('data')[0].get("shareImage")))
print("ExtendedLocation:"+response.get('data')[0].get("ExtendedLocation"))
print("QriginQuery:"+str(response.get('data')[0].get("QriginQuery")))
print("tplt:"+response.get('data')[0].get("tplt"))
print("resourceid:"+str(response.get('data')[0].get("resourceid")))
print("fetchkey:"+response.get('data')[0].get("fetchkey"))
print("appinfo:"+response.get('data')[0].get("appinfo"))
print("role_id:"+str(response.get('data')[0].get("role_id")))
print("disp_type:"+str(response.get('data')[0].get("disp_type")))

