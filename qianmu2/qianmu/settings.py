# -*- coding: utf-8 -*-

# Scrapy settings for qianmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


#修改调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#开启去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# REDIS_URL = 'redis://localhost:6379'
SCHEDULER_PERSIST = True


BOT_NAME = 'qianmu'

SPIDER_MODULES = ['qianmu.spiders']
NEWSPIDER_MODULE = 'qianmu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#并发请求数量
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#请求延迟时间（秒）该为0表示没有延迟
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#是否保存cookies，最好关闭
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  'accept-encoding': "gzip, deflate",
  'accept-language': "zh-CN,zh;q=0.8",
  'cache-control': "no-cache",
  'connection': "keep-alive",
  # 'host': "140.143.192.76:8002",
  'if-modified-since': "Tue, 14 Nov 2017 15:13:12 GMT",
  'if-none-match': "W/\"5a0b0808-327c0\"",
  # 'referer': "http://140.143.192.76:8002/ranking/905.htm",
  'upgrade-insecure-requests': "1",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
#}
HTTPPROXY_ENABLED = False
PROXIES = ['http://pc1120:pc1120@123.249.34.10:888', 'http://pc1120:pc1120@1.82.230.113:888']
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'qianmu.middlewares.MyCustomDownloaderMiddleware': None,
    'qianmu.middlewares.RandomUserAgentMiddleware': 500,
    'qianmu.middlewares.RandomProxyMiddleware': 749,
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
   # 'qianmu.pipelines.CheckPipeline': 300,
   # 'qianmu.pipelines.RedisPipeline': 301,
   # 'qianmu.pipelines.MysqlPipeline': 302,
    'scrapy_redis.pipelines.RedisPipeline':300
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
