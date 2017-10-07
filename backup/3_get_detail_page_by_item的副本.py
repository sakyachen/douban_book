from bs4 import BeautifulSoup
import io,os,sys
import codecs
import StringIO
import pycurl
import sys
import re
import time
import random
reload(sys)
sys.setdefaultencoding('utf-8')

mdir=sys.path[0]+'/'
current_list=os.listdir(mdir+ "/item")
f1=codecs.open(mdir + 'get_book_info.csv','r','utf8')
item=f1.read().split("\n")
# print item
head = ['Accept:*/*',  
                'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11']
for i in range(0,len(item)):
    item_info=item[i].split("\t")
    url=item_info[1]
    url_id=item_info[2]
    target_name='douban_' + url_id + '.html'

    if target_name not in current_list:
        if i%3==0:
            time.sleep(random.randint(5, 10))
        req=url
        print req
        c = pycurl.Curl()
        # c.setopt(pycurl.COOKIEFILE, "11")
        # c.setopt(pycurl.COOKIEJAR, "11")  

        res = StringIO.StringIO()
        c.setopt(pycurl.URL, req)
        c.setopt(pycurl.WRITEFUNCTION, res.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.HTTPHEADER,head) 
        c.perform()
        html=res.getvalue()

        file=codecs.open(mdir + 'item/'+ target_name,'w','utf8')
        file.write(html)
        file.close()

f1.close()