from bs4 import BeautifulSoup
# import io
import os
import sys
import codecs
# import StringIO
# import pycurl
# import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

mdir = sys.path[0]+'/'
f2 = codecs.open(mdir + 'get_book_info.csv', 'w', 'utf8')
page_list = os.listdir(mdir + "/web")
# print page_list

for page in page_list:
    page_full = mdir + 'web/' + page
    soup = BeautifulSoup(open(page_full))
    # print soup
    # soup.total=soup.select('.subject-list')
    # print soup.total
    soup_title = soup.select('.subject-list .subject-item .info .')
    # for title in soup_title:
    #     print title.a['title'],title.a['href']
    soup_info = soup.select('.subject-list .subject-item .info .pub')
    # for info in soup_info:
    #     print info.get_text()
    soup_score = soup.select(
        '.subject-list .subject-item .info .star .rating_nums')
    # for score in soup_score:
    #     print score.get_text()
    soup_users = soup.select('.subject-list .subject-item .info .star .pl')
    # for users in soup_users:
    #     print users.get_text().replace(" ","").replace("\n","")

    for i in range(0, len(soup_title)):
        try:
            title = soup_title[i].a['title']
            print title
            url = soup_title[i].a['href']
            info = soup_info[i].get_text().replace(" ", "").replace("\n", "")
            score = soup_score[i].get_text()
            users = soup_users[i].get_text().replace(" ", "").replace("\n", "")
            users = str(re.search(r"[0-9]+", users).group(0))
            f2.write(page.split("_")[0]+"_"+page.split("_")[1])
            f2.write("\t")
            f2.write(url)
            f2.write("\t")
            f2.write(url.split("/")[4])
            f2.write("\t")
            f2.write(title)
            f2.write("\t")
            f2.write(score)
            f2.write("\t")
            f2.write(users)
            f2.write("\t")
            f2.write(info)
            f2.write("\n")
        except:
            print page + "error"
    print page + "success"


f2.close()
