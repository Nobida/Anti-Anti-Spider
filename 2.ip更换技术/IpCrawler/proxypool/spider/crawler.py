# -*- coding: utf-8 -*-

import time
from .config import spider_rule_list
from .getting import Downloader
from .parserpage import Parser
from .validate import Validate
from db.mongo_db import MongoDB


def check():
    '''
    定时检测数据库中代理的可用性
    :return:
    '''
    while True:
        m = MongoDB()
        count = m.get_count()
        if not count == 0:
            print('开始检测数据库中代理可用性>>>>>>>>')
            proxies = m.get(count)
            Validate().valid_many(proxies, 'check')
        time.sleep(10 * 60)


def crawl_ip():
    '''
    获取可用的代理IP
    :return:
    '''
    while True:
        print('开始抓取可用的代理IP>>>>>>>>>>')
        Crawler().crawl()
        time.sleep(2 * 60 * 60)

class Crawler(object):

    def crawl(self):
        for spider_rule in spider_rule_list:
            for url in spider_rule['urls']:
                resp = Downloader().downloader(url, spider_rule)  # resp为返回的网页内容
                if resp:
                    proxy_list = Parser().parser(resp, spider_rule)
                    Validate().valid_many(proxy_list, 'insert')


if __name__ == "__main__":
    c = Crawler().crawl()
    print(c)
