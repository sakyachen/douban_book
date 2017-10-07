from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
import pandas as pd
import sys

# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
reload(sys)
sys.setdefaultencoding('utf8')
mdir = sys.path[0] + '/'

data_file_item = mdir + 'combine_web_item.csv'
df_item = pd.read_table(data_file_item, header=0)
df_item = df_item.fillna(0)
# print df_item
# print df_item.describe()
X = df_item[['short_comment', 'long_comment', 'reading', 'collectiongs', 'wishes', 'users']]
y = df_item['score']
# print X.describe()
# print y.describe()
lr = linear_model.LinearRegression()

# # boston = datasets.load_boston()
# # y = boston.target
# # # print boston.data

# X = scale(X)
result = lr.fit(X, y)

print result.coef_
print result.intercept_
# # cross_val_predict returns an array of the same size as `y` where each entry
# # is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, X, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
