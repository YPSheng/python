import re
import json
import time
import random
import requests
import urllib
import time
import codecs
import urllib3
def songmid():
    mid = []
    name = []
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=sizer.yqq.song_next&searchid=148958880434449513&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk=1989554541&jsonpCallback=searchCallbacksong5150&loginUin=1093211972&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
    response = requests.get(url)
    if json.loads(response.text[23:-1])['data']['song']['curnum'] and json.loads(response.text[23:-1])['data']['song']['curpage']:
    # if True:
        for i in range(20):
            # print(i)
            jsonpcallback = "searchCallbacksong"+str((random.randint(1000,10000)))
            if i == 0:
                remoteplace = "txt.yqq.song"
            else:
                remoteplace = "sizer.yqq.song_next"
            # print(i)
            params= {
                    'ct': "24",
                    'qqmusic_ver': "1298:",
                    'new_json': "1",
                    'remoteplace': "sizer.yqq.song_next",
                    'searchid': "148958880434449513",
                    't': "0",
                    'aggr': "1",
                    'cr': "1",
                    'catzhida': "1",
                    'lossless': "0",
                    'flag_qc': "0",
                    'p': i+1,
                    'n': str(json.loads(response.text[23:-1])['data']['song']['curnum']),
                    # 'n': 20,
                    'w': "%E4%BA%94%E6%9C%88%E5%A4%A9",
                    'g_tk': "1989554541",
                    'jsonpcallback': jsonpcallback,
                    'loginuin': "1093211972",
                    'hostuin': "0",
                    'format': "jsonp",
                    'incharset': "utf8",
                    'outcharset': "utf-8",
                    'notice': "0",
                    'platform': "yqq",
                    'neednewcode': "0",
                    'cache-control': "no-cache",
            }
            # url2 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?"
            url2 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
            response2 = requests.get(url2,params=params)
            # print(json.loads(response2.text[9:-1]))
            for i in json.loads(response2.content[9:-1])['data']['song']['list']:
                if i['file']['media_mid']:
                    mid.append(i['file']['media_mid'])
                    name.append(i['name'])
    print(set(mid))
    print(len(set(mid)))
    return mid,name
url = []
file = codecs.open('audio2.txt','w')
def resolve(songmids,name):

    for i in range(len(songmids)):
        filename = 'C400' + songmids[i] + '.m4a'
        # print(songmids[i])
        guid = int(random.random() * 2147483647) * int(time.time() * 1000) % 10000000000

        d = {
            'format': 'json',
            'cid': 205361747,
            'uin': 0,
            'songmid': songmids[i],
            'filename': filename,
            'guid': guid,
            'g_tk':5381,
            'loginUin':0,
            'hostUin':0,
            'notice': '0',
            'platform':'yqq',
            'needNewCode':'0',
        }
        headers = {
            'User - Agent':"Mozilla / 5.0(WindowsNT10.0; …) Gecko / 20100101Firefox / 57.0"
        }
        r = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg', params=d)
        try:
            vkey = json.loads(r.text)['data']['items'][0]['vkey']
        except:
            continue
        if vkey:
            audio_url = 'http://dl.stream.qqmusic.qq.com/%s?vkey=%s&guid=%s&uin=0&fromtag=66' % (filename, vkey, guid)
            time.sleep(random.random()*1)
            url.append(audio_url)
            file.write(audio_url+'\n')
if __name__ == "__main__":
    songmids,name =songmid()
    resolve(songmids,name)
    file.close()