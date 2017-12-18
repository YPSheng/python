# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'
LOG_LEVEL= 'INFO'


#数据库,我已经写死了，所以这里就不写值了，如果需要在这里调用的可以填写这两个值
# MONGO_URI = ''
# MONGO_DATABASE = ''

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lagou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# COOKIE = " user_trace_token=20171016205119-74af5f4b-4f58-445f-9516-f8c19f475243; LGUID=20171016205145-c44d7b22-b270-11e7-991d-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=2; _gat=1; index_location_city=%E5%8C%97%E4%BA%AC; login=false; unick=""; _putrc=""; JSESSIONID=ABAAABAAADEAAFI9B5F7A7C0171C81B55991A6F507BB38C; TG-TRACK-CODE=index_navigation; _gid=GA1.2.1376878689.1512383958; _ga=GA1.2.358203920.1509241265; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511828514,1511828645,1512096311,1512383961; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512391953; LGSID=20171204201356-99b53ec2-d8ec-11e7-82ca-525400f775ce; LGRID=20171204205308-13e42a93-d8f2-11e7-8301-525400f775ce; SEARCH_ID=b1c5303a69754a66bc97d63dc0fec865"
# Cookie =  {'user_trace_token':'20171016205119-74af5f4b-4f58-445f-9516-f8c19f475243',' LGUID':'20171016205145-c44d7b22-b270-11e7-991d-525400f775ce', 'showExpriedIndex':'1',
#            'showExpriedCompanyHome':'1', 'showExpriedMyPublish':'1', 'hasDeliver':'2', '_gat':'1','index_location_city':'%E5%8C%97%E4%BA%AC','login':'false',
#            'unick':"", '_putrc':"", 'JSESSIONID':'ABAAABAAADEAAFI9B5F7A7C0171C81B55991A6F507BB38C' ,'TG-TRACK-CODE':'index_navigation','_gid':'GA1.2.1376878689.1512383958','_ga':'GA1.2.358203920.1509241265','Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1511828514,1511828645,1512096311,1512383961','Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1512391953','LGSID':'20171204201356-99b53ec2-d8ec-11e7-82ca-525400f775ce',
#            'LGRID':'20171204205308-13e42a93-d8f2-11e7-8301-525400f775ce','SEARCH_ID':'b1c5303a69754a66bc97d63dc0fec865'}
#  Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#         'Accept':'application/json, text/javascript, */*; q=0.01',
#         'Accept-Encoding':'gzip, deflate, br',
#         'Accept-Language':'zh-CN,zh;q=0.8',
#         'Connection':'keep-alive',
#         'Content-Length':'25',
#         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#         'Cookie':'user_trace_token=20171016205119-74af5f4b-4f58-445f-9516-f8c19f475243; LGUID=20171016205145-c44d7b22-b270-11e7-991d-525400f775ce; JSESSIONID=ABAAABAAAIAACBIB57C77C4ECB2518EE2D0B9135B108E91; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=http%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E9%2592%25A9%26rsv_spt%3D1%26rsv_iqid%3D0xaa9b6e5d00013b57%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3D%26tn%3Dbaiduhome_pg%26ch%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; _putrc=54D6D44AC87A2A52; login=true; unick=%E6%9D%A8%E9%B9%8F%E5%8D%87; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=2; _ga=GA1.2.358203920.1509241265; _gid=GA1.2.1325253718.1511828511; LGSID=20171128082152-21c7cb9f-d3d2-11e7-ae6a-525400f775ce; LGRID=20171128082206-2a422523-d3d2-11e7-ae6a-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510323969,1511253705,1511253729,1511828514; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511828527; SEARCH_ID=8267a0cd29464ff6b38f86b1d1e17b96; index_location_city=%E5%8C%97%E4%BA%AC',
#         'Host':'www.lagou.com',
#         'Origin':'https://www.lagou.com',
#         'Cookie':'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512613229,1512613260,1512625404,1512968182; index_location_city=%E5%8C%97%E4%BA%AC; _ga=GA1.2.2037062440.1512613233; user_trace_token=201712011102032-33c95bdc-daf5-11e7-8800-525400f775ce; LGUID=20171207102032-33c95ef6-daf5-11e7-8800-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=4; JSESSIONID=ABAAABAAADEAAFI7D85FFAA76F7A088717F2BAF4B49DB5A; SEARCH_ID=e00f27cb11504a72a10b8ec58bd5f04f; _gat=1; LGSID=20171211125618-9f9c7c23-de2f-11e7-8e96-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_COCOS2D-X%3Fpx%3Ddefault%26city%3D%25E5%2585%25A8%25E5%259B%25BDstart.firefoxchina.cn; LGRID=20171211125650-b2cc7009-de2f-11e7-8e96-525400f775ce; _putrc=54D6D44AC87A2A52; _gid=GA1.2.834272328.1512968180; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512968210',
        # 'Referer':"https://www.lagou.com",
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'X-Anit-Forge-Code':'0',
        # 'X-Anit-Forge-Token':'None',
        # 'X-Requested-With':'XMLHttpRequest'
# }


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'lagou.middlewares.MyCustomDownloaderMiddleware': 543,
    'lagou.middlewares.UserAgentMiddleware':500,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lagou.pipelines.LagouPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#开启scrapy-redis分布式
#修改调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#开启去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"