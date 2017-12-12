from urllib.request import _parse_proxy

import faker
from scrapy.exceptions import NotConfigured
import random
import logging

logger = logging.getLogger()

#处理代理ip，将用户名密码去掉
def reform_url(url):
    proxy_type,user,password,hostport = _parse_proxy(url)
    return '%s://%s' % (proxy_type,hostport)


class RandomProxyMiddleware(object):

    def __init__(self,settings):
        self.proxies = settings.getlist('PROXIES')
        self.max_failed = settings.getint('PROXY_MAX_FAILED',3)
        self.stats = {}.fromkeys(map(reform_url,self.proxies),0)

    def random_proxy(self):
        return random.choice(self.proxies)

    @classmethod
    def from_crawler(cls,crawler):
        if not crawler.settings.getbool("HTTPPROXY_ENABLED"):
            raise NotConfigured
        if not crawler.settings.getlist("PROCIES"):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self,request,spider):
        if 'proxy' not in request.meta:
            # print("111111111111111111111111111111111")
            request.meta['proxy'] = self.random_proxy()

    def process_response(self,request,response,spider):
        cur_proxy = request.meta['proxy']
        #如果该代理不能用，就将它的值+1,也代表着失败次数+1，默认的每个代理Ip对应的值为0
        if response.status > 400:
            self.stats[cur_proxy] += 1
        #如果键为当前代理的值大于最大失败次数时，就从代理池里删除此代理
        if self.stats[cur_proxy] > self.max_failed:
            for proxy in self.proxies:
                if reform_url(proxy) == cur_proxy:
                    self.stats.remove(proxy)
                    break
            logger.warning('proxy %s remove from proxies list' % cur_proxy)
        return response