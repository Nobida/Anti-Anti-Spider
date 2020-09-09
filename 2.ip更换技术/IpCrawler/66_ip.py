# -*- coding: utf-8 -*-



import requests,re


def craw_66ip():
    url = 'http://www.66ip.cn/{}.html'
    for i in range(1,1300):
        r = requests.get(url.format(i)).text
        ips = re.findall('td>(\w+\.\w+\.\w+\.\w+)</td',r,re.S)
        ports = re.findall('\.\w+</td.*?>(\w+)</td',r,re.S)
        for i in range(len(ips)):
            str = ips[i]+":"+ports[i]
            try:
                http = "http://"+ips[i]+":"+ports[i]
                requests.get('https://httpbin.org/get?show_env=1', proxies={"http":http})
            except:
                print('connect failed')
            else:
                print('success')


craw_66ip()