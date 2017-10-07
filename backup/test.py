#coding:utf-8
import urllib2
import random

def get_html(url,headers,proxies):

    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)

    #下面是模拟浏览器进行访问
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_userAget)
    req.add_header("GET", url)
    # req.add_header("Host", "blog.csdn.net")
    # req.add_header("Referer", "http://blog.csdn.net/?&page=6")

    #下面是使用ip代理进行访问
    proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(req)
    return html

url = "http://36kr.com/"
user_agents = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWe...hrome/45.0.2454.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"]
myproxies=["122.5.83.175:808","117.90.6.108:9000"]

html = get_html(url,user_agents,myproxies)

print html.read()