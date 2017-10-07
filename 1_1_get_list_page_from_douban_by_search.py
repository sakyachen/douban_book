# -*- coding:UTF-8 -*- ＃
import os
import sys
import codecs
import time
import random
import urllib2
# import cookielib
reload(sys)
sys.setdefaultencoding('utf8')

# 以下为基本配置项，获取代理和浏览器信息
#test commit
#test3
mdir = sys.path[0]+'/'
proxy_list = codecs.open(mdir + 'proxy_list.csv', 'r', 'utf8')
myproxies = proxy_list.read().split("\n")

user_agents_list = codecs.open(mdir + 'user_agents_list.csv', 'r', 'utf8')
user_agents = user_agents_list.read().split("\n")
# user_agents = ["Mozilla/5.0 +(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)"]


def get_html(url, headers, proxies):
    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)

# 下面是生成cookie
    # filename = 'cookie.txt'
    # cookie = cookielib.MozillaCookieJar(filename)
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # opener.open("https://www.douban.com/")
    # cookie.save(ignore_discard=True, ignore_expires=True)
    # print cookie

# 下面是模拟浏览器进行访问
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_userAget)
    req.add_header("GET", url)
    req.add_header("Host", "book.douban.com")
    req.add_header("Referer", "https://beijing.douban.com")

# 下面是使用ip代理进行访问
    proxy_support = urllib2.ProxyHandler({"http": random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(req)
    return html


# 以下为指定页面的抓取流程
current_list = os.listdir(mdir + "/web")
word_list = ["绘本", "图画书", "童书", "繪本", "儿童", "儿童文学", "经典绘本"]
for word in word_list:
    for i in range(0, 135):
        page = str(i*15)
        target_name = 'search_' + word + '_' + page + '.html'

        if target_name not in current_list:
            url = "https://book.douban.com/subject_search?search_text=" + word + "&start=" + page + "&cat=1001"
            print url
            if i % 3 == 0:
                time.sleep(random.randint(3, 10))

            try:
                html = get_html(url, user_agents, myproxies).read()
                file = codecs.open(mdir + 'web/' + target_name, 'w', 'utf8')
                file.write(html)
                file.close()
                print url, "success"
            except:
                print url, "failed"
                continue


proxy_list.close()
user_agents_list.close()
