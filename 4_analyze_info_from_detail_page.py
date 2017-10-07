# -*- coding:UTF-8 -*- ＃
# import io
import codecs
import os
import re
import sys
# import StringIO
# import pycurl
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

mdir = sys.path[0] + '/'
f2 = codecs.open(mdir + 'get_book_info_detail.csv', 'w', 'utf8')
page_list = os.listdir(mdir + "/item")
# print page_list

for page in page_list:
    page_full = mdir + 'item/' + page
    # print page
    soup = BeautifulSoup(open(page_full))
    try:
        title = soup.select('.article .indent .subjectwrap .subject #info')
        title = str(title).replace("</span>", "").replace("<span>", "")
        title = title.replace("<br/>", "").replace('<span class="pl">', "")
        title = title.replace('<div class="" id="info">', "")
        title = re.sub('<a.*">', "", title).replace("</a>", "")
        title = title.replace("</div>", "").replace(" ", "")
        ISBN = str(re.search(r"ISBN:[0-9]+", title).group(0))
        ISBN = str(re.search(r"[0-9]+", ISBN).group(0))
        # print ISBN
        f2.write(ISBN)
        f2.write("\t")

        f2.write(page.replace("douban_", "").replace(".html", ""))
        f2.write("\t")

        soup_score = soup.select('.article .indent .subjectwrap #interest_sectl .rating_wrap .rating_per')
        # print soup_score
        for score in soup_score:
            score = score.get_text()
            if len(score) == 0:
                score = "0"
            else:
                score = score
            f2.write(str(score))
            f2.write("\t")

        try:
            soup_short_comment = soup.select('.article .related_info .mod-hd .pl')
            short_comment = soup_short_comment[0]
            short_comment = short_comment.get_text()
            short_comment = str(re.search(r"[0-9]+", short_comment).group(0))
            # print short_comment
            f2.write(short_comment)
        except:
            f2.write("0")
        f2.write("\t")

        try:
            soup_long_comment = soup.select('.article .related_info .reviews .pl')
            long_comment = soup_long_comment[0]
            long_comment = long_comment.get_text()
            long_comment = str(re.search(r"[0-9]+", long_comment).group(0))
            # print long_comment
            f2.write(long_comment)
        except:
            f2.write("0")
        f2.write("\t")

        # try:
        #     soup_note=soup.select('.article .related_info .ugc-mod .pl')
        #     note=soup_note[0]
        #     note=note.get_text()
        #     note=str(re.search(r"[0-9]+",note).group(0))
        #     f2.write(str(note))
        # except:
        #     print 'error'
        f2.write("0")
        f2.write("\t")

        soup_read_status = soup.select('.aside #collector .pl')

        try:
            doings = re.findall('doings">[0-9]+', str(soup_read_status))
            doings = doings[0].replace('doings">', '')
            f2.write(doings)
        except:
            f2.write("0")
        f2.write("\t")

        try:
            collections = re.findall('collections">[0-9]+', str(soup_read_status))
            collections = collections[0].replace('collections">', '')
            f2.write(collections)
        except:
            f2.write("0")
        f2.write("\t")

        try:
            wishes = re.findall('wishes">[0-9]+', str(soup_read_status))
            wishes = wishes[0].replace('wishes">', '')
            f2.write(wishes)
        except:
            f2.write("0")
        f2.write("\t")

        try:
            pic = soup.select('.article .indent .subjectwrap .subject #mainpic .nbg')
            pic = pic[0].get('href')
            f2.write(pic)
        except:
            f2.write("0")
        f2.write("\n")

    except:
        continue
        print page + "error"
    # print page
print 'success'


f2.close()
