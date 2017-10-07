# coding:utf-8
from bs4 import BeautifulSoup
import io
import os
import sys
import codecs
import sys
import re
import time
import random
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')
# 以下为基本配置项，获取代理和浏览器信息
mdir = sys.path[0]+'/'
proxy_list = codecs.open(mdir + 'proxy_list.csv', 'r', 'utf8')
myproxies = proxy_list.read().split("\n")

# user_agents_list=codecs.open(mdir + 'user_agents_list.csv','r','utf8')
# user_agents=user_agents_list.read().split("\n")
user_agents = [
    "Mozilla/5.0 +(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)"]


def get_html(url, headers, proxies):

    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)

    # 下面是模拟浏览器进行访问
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_userAget)
    req.add_header("GET", url)
    req.add_header("Host", "book.douban.com")
    req.add_header("Referer", "https://market.douban.com")

    # 下面是使用ip代理进行访问
    proxy_support = urllib2.ProxyHandler({"http": random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(req)
    return html

# 以下为指定页面的抓取流程
current_list = os.listdir(mdir + "/item")
book_list = codecs.open(mdir + 'get_book_info_clean.csv', 'r', 'utf8')
item = book_list.read().split("\n")

item_reslut = codecs.open(
    mdir + 'log_item_reslut_get_book_info_clean.csv', 'w', 'utf8')

for i in range(0, len(item)-1):
    item_info = item[i].split("\t")
    url = item_info[1]
    url_id = item_info[2]
    target_name = 'douban_' + url_id + '.html'

    if target_name not in current_list:
        if i % 3 == 0:
            time.sleep(random.randint(3, 7))
        try:
            html = get_html(url, user_agents, myproxies).read()
        except:
            print url, "failed"
            continue

        file = codecs.open(mdir + 'item/' + target_name, 'w', 'utf8')
        file.write(html)
        file.close()
        print url, "success"
        item_reslut.write(url + ",success" + "\n")
    else:
        item_reslut.write(url + ",exist" + "\n")

book_list.close()
proxy_list.close()
item_reslut.close()
# user_agents_list.close()
