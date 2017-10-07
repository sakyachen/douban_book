# coding=utf-8
import mysql.connector
import sys
# import io
import codecs
reload(sys)
sys.setdefaultencoding('utf8')

cnx = mysql.connector.connect(user='root', password='shaka634', host='localhost', port='3306', database='douban_book')
cursor = cnx.cursor()
cursor.execute("set names utf8")


def addCity(ISBN, douban_id, star5, star4, star3, star2, star1, short_comment, long_comment, note, reading, collectiongs, wishes, title, score, users, url_pic):
    try:
        sql = "insert into combine_web_item(ISBN, douban_id, 5star, 4star, 3star, 2star, 1star, short_comment, long_comment, note, reading, collectiongs, wishes, title, score, users, url_pic) values ('"+ISBN+"', '"+douban_id+"', '"+star5+"', '"+star4+"', '"+star3+"', '"+star2+"', '"+star1+"', '"+short_comment+"', '"+long_comment+"', '"+note+"', '"+reading+"', '"+collectiongs+"', '"+wishes+"', '"+title+"', '"+score+"', '"+users+"', '"+url_pic+"')"        
# print sql
        cursor.execute(sql)
        cnx.commit()
    except mysql.connector.Error as e:
        print('insert datas error!{}'.format(e))


mdir = sys.path[0] + '/'
file = codecs.open(mdir + 'combine_web_item.csv', 'r', 'utf8')
f = file.read().split("\n")
for i in range(1, len(f)):
    try:
        content = f[i].split("\t")
        addCity(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9], content[10], content[11], content[12], content[13], content[15], content[14])
    except:
        print "error"
        continue

cursor.close()
cnx.close()
file.close()
