#coding:utf8

import requests
import execjs
import urllib
import re
# from urlparse import urljoin
import json
import time
# from readability.readability import Document
from lxml import html
import logging


def get_source(url):
    s = requests.Session()
    # url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

    headers = {
    "Host":"www.lagou.com",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=python",
    }
    r1 = s.get(url)
    # print (r1.text,'##############################',r1.status_code,)
    try:
        json_data = json.loads(r1.text)
    except Exception as e:
        logging.debug('###############json failed:{}'.format(e))
        return ""
    encrypt_data = json_data.get('encrypt_data','')
    return encrypt_data
#js里面my_result函数直接返回object给Python会报错，所以这里将JSON.parse移除了，返回parse前的json字符串
def my_result(encrypt_data):
    ctx = execjs.compile(open('qimingpian_test.js').read())
    result = ctx.call('my_result',encrypt_data)
    return result

if __name__ == '__main__':
    start_url = 'https://vipapi.qimingpian.com/DataList/productListVip'
    encrypt_data = get_source(start_url)
    result = my_result(encrypt_data)
    print('##################',result)




