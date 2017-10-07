# -*- coding:UTF-8 -*- ＃
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mdir = sys.path[0] + '/'
data_file = mdir + 'get_book_info.csv'

df = pd.read_table(data_file, header=None, names=['tag', 'url', 'id', 'title', 'score', 'users', 'info'])
df = df.drop_duplicates(['id'])
df.to_csv(mdir + 'get_book_info_clean.csv', sep="\t", index=False, header=False)
print "success"
