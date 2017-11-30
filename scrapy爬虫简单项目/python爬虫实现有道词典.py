import requests
import urllib.request
import json
import urllib.parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
headers = {
            'Cookie':'OUTFOX_SEARCH_USER_ID=-763428860@10.168.8.61; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abc31lbWsGNO67M3Fi-8v; OUTFOX_SEARCH_USER_ID_NCOO=1648534080.0892432; _ntes_nnid=bf4e54b134dc8a8b2f65cd59c8ba272e,1508592727589; ___rl__test__cookies=1508593353423',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

dict1 = {
    '0':['zh-CHS','en'],
    '1':['en','zh-CHS'],
    '2':['zh-CHS','ja'],
    '3':['ja','zh-CHS'],
    '4':['zh-CHS','ko'],
    '5':['ko','zh-CHS'],
    '6':['zh-CHS','fr'],
    '7':['fr','zh-CHS'],
    '8':['zh-CHS','ru'],
    '9':['ru','zh-CHS'],
    '10':['zh-CHS','es'],
    '11':['es','zh-CHS'],
    '12':['zh-CHS','pt'],
    '13':['pt','zh-CHS'],
}
switch = input("请选择语言翻译：0：中文-》英语，1：英语-》中文，2：中文-》日语，3：日语-》中文，\n，4：中文-》韩语，5：韩语-》中文，"
               "6：中文-》法语，7：法语-》中文，8：中文-》俄语，\n，9：俄语-》中文，10：中文-》西班牙语，\n，11：西班牙语-》中文，12：中文-》葡萄牙语，"
               "13：葡萄牙语-》中文：")

star = dict1[switch][0]
end = dict1[switch][1]
# print(star)
# print(end)
word = input("请输入你要翻译的语句：")
data = {
        'i':word,
        'from':star,
        'to':end,
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1508593351114',
        'sign':'32cded672e5ba31d4f4929650a5ad22e',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':'true'
}

data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url=url,data=data)
datas = json.loads(response.read().decode("utf-8"))
answer = datas.get('translateResult')[0][0]['tgt']
print(answer)