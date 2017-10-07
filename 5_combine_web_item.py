# -*- coding:UTF-8 -*- ＃
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mdir = sys.path[0] + '/'

data_file_web = mdir + 'get_book_info_clean.csv'
df_web = pd.read_table(data_file_web, header=None, names=['tag', 'url', 'douban_id', 'title', 'score', 'users', 'info'])
df_web = df_web[['douban_id', 'title', 'score', 'users']]

data_file_item = mdir + 'get_book_info_detail.csv'
df_item = pd.read_table(data_file_item, header=None, names=['ISBN', 'douban_id', '5star', '4star', '3star', '2star', '1star', 'short_comment', 'long_comment', 'note', 'reading', 'collectiongs', 'wishes', 'url_pic'])

data_reslut = pd.merge(df_item, df_web, on='douban_id', how='left', indicator=False)

data_reslut.to_csv(mdir + 'combine_web_item.csv', sep="\t", index=False, header=True)
print "combine success"
