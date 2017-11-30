import urllib
import urllib.request
import re
import random
import time
#抓取所需内容
user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
stock_total=[]   #stock_total：所有页面的股票数据   stock_page：某页的股票数据
for page in range(1,8):
    url='http://quote.stockstar.com/stock/ranklist_a_3_1_'+str(page)+'.html'
    request=urllib.request.Request(url=url,headers={"User-Agent":random.choice(user_agent)})#随机从user_agent列表中抽取一个元素
    try:
        response=urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:            #异常检测
        print('page=',page,'',e.code)
    except urllib.error.URLError as e:
        print('page=',page,'',e.reason)
    content=response.read().decode('gbk')       #读取网页内容
    print('get page',page)                  #打印成功获取的页码
    pattern=re.compile('<tbody[\s\S]*</tbody>')
    body=re.findall(pattern,str(content))
    # for i in body:
    #     print(i)
    pattern=re.compile('>(.*?)<')
    stock_page=re.findall(pattern,body[0])      #正则匹配
    # print(stock_page)
    stock_total.extend(stock_page)
    # print(stock_total)
    time.sleep(random.randrange(1,4))        #每抓一页随机休眠几秒，数值可根据实际情况改动
#删除空白字符
stock_last=stock_total[:]  #stock_last为最终所要得到的股票数据
for data in stock_total:
    if data=='':
        stock_last.remove('')
# print(stock_last)
#打印部分结果
print('代码','\t','简称','   ','\t','最新价','\t','涨跌幅','\t','涨跌额','\t','5分钟涨幅')
for i in range(len(stock_last) - 6):
    print(format(stock_last[i],"6s"),'\t',format(stock_last[i+1],"6s"),' ','\t',format(stock_last[i+2],"6s"),'  ','\t',format(stock_last[i+3],"6s"),'  ','\t',format(stock_last[i+4],"6s"),'  ','\t',format(stock_last[i+5],"6s"))
