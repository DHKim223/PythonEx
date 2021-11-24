# 머신러닝 분석
import numpy as np
from sklearn import svm
from sklearn.linear_model._glm.glm import GeneralizedLinearRegressor
data = np.array( [[0,0],[0,1],[1,0],[1,1]] )         # 학습용데이터
#label = np.array( [0,0,0,1] ) # and                 # 정답 ( 라벨 )
#label = np.array( [0,1,1,1] ) # or                    # 정답 ( 라벨 )
label = np.array( [0,1,1,0] ) # Xor                    # 정답 ( 라벨 )

svc = svm.SVC()                                                # 알고리즘선택        
model = svc.fit(data, label)                             # 학습
print(model.predict(  [[0,1]]  ))                       # 예측


data = np.array( [[0,0],[0,1],[1,0],[1,1],\
                                [0,0],[0,1],[1,0],[1,1],
                                [0,0],[0,1],[1,0],[1,1],           
                  ] ) 

label = np.array( [0,1,1,0,1,1,0,0,1,1,0,0] )
svc = svm.SVC()                                                # 알고리즘선택        
model = svc.fit(data, label)                             # 학습

test_data = np.array([[0,0],[0,1],[1,0],[1,1]])
test_label = np.array([0,1,0,1])
predicts = model.predict(test_data)
print(test_label)
print(predicts)
from sklearn import metrics
score = metrics.accuracy_score(test_label,predicts)
print(score)

print(model.predict( [[0,1]] ))     # 예측

print("#########################################")
# 회귀분석
import pandas as pd
data = pd.read_csv("ozone.csv")
#print(data.head())
#print(data.shape)   # (153, 6)

data = data.dropna(axis=0)
# print(data.shape)
# print(data.head())
# print(data.count())

# 오존과 온도
x = data ["Temp"].values            #    독립변수 X축
y = data["Ozone"].values             #    종속변수 Y축

# 오존과 바람
x = data ["Wind"].values            #    독립변수 X축
y = data["Ozone"].values             #    종속변수 Y축


from scipy import stats
result = stats.linregress(x,y)
print(result)

print(80*result.slope + result.intercept)       # 예측

import matplotlib.pyplot as plt
# plt.scatter(x,y)
# plt.plot(x,result.slope * x+result.intercept, c="r")
# plt.xlabel("Temp")
# plt.ylabel("Ozone")
# plt.show()

#  Boston 주택가격
from sklearn.datasets import load_boston

boston = load_boston()
# print(type(boston))
# print(boston)
# print(boston.DESCR)            # 명세
#print(boston.feature_names) # Column names
data = boston.data
label = boston.target
#print(type(data))
#print(boston.shape)         #(506,13)     #numpy.ndarray 만 shape 사용가능
#print(label.shape)              #(506, )

data = pd.DataFrame(data)

from sklearn.model_selection import train_test_split
train_data, test_data, train_label, test_label = \
    train_test_split(data, label, test_size=0.3, random_state=0)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model = lr.fit(train_data,train_label)
print(model.score(train_data,train_label))      #0.76
print(model.score(test_data, test_label))       # 0.67

predicts = model.predict(train_data)
plt.scatter( train_label, predicts)
# x = np.arange(0,50)
# y = np.arange(0,50)
# plt.plot(x,y,c="r")
#
# plt.xlabel("price")
# plt.ylabel("predicts")
# plt.show()

# fig = plt.figure()
# for i in range ( data.shape[1]):
    # fig.add_subplot(4,4,i+1)
    # x = data[i]
    # plt.scatter(x, label,alpha=0.5)
    # plt.xlabel(boston.feature_names[i])
    # plt.ylabel("price")
# plt.show()

import mglearn
data , label = mglearn.datasets.load_extended_boston()
#print(data.shape)
train_data, test_data, train_label, test_label = \
    train_test_split(data, label, test_size=0.3, random_state=0)
lr = LinearRegression()
model = lr.fit(train_data, train_label)
print(model.score(train_data, train_label))     # 0.95
print(model.score(test_data, test_label))       # 0.64

# 릿지 회귀분석
# 선형회귀보다 과적합이 적다
from sklearn.linear_model import Ridge
ridge = Ridge()
model = ridge.fit(train_data, train_label)
print(model.score(train_data, train_label))         # 0.88    
print(model.score(test_data, test_label))           # 0.78

model = Ridge(alpha=10).fit(train_data, train_label)
print(model.score(train_data, train_label))         # 0.77
print(model.score(test_data, test_label))           # 0.67

model = Ridge(alpha=0.01).fit(train_data, train_label)
print(model.score(train_data, train_label))         # 0.94
print(model.score(test_data, test_label))           # 0.74

print("#################################################")
# 맨허튼 임대료
url = "https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/manhattan.csv"
manhattan = pd.read_csv(url)
#print(manhattan.head())
#print(manhattan.shape)          #(3539,18)
#print(type(manhattan))
corr_matrix = manhattan.corr()
#print(corr_matrix["rent"].sort_values(ascending=False))
corr_df = pd.DataFrame(corr_matrix["rent"].sort_values(ascending=False))

# plt.clf()
# plt.figure(figsize=(6,4))
# plt.bar( corr_df.index, corr_df["rent"])
# plt.xticks(rotation=45)
# plt.show()

# from pandas.plotting import scatter_matrix
# attributes = ["bedrooms","bathrooms","size_sqft","no_fee","floor","building_age_yrs","rent"]
# scatter_matrix(manhattan[attributes],figsize=(6,4))
# plt.show()

data = manhattan[["rental_id","bedrooms","bathrooms","size_sqft",\
                   "min_to_subway","floor","building_age_yrs","no_fee",\
                   "has_roofdeck","has_washer_dryer","has_doorman",\
                   "has_elevator","has_dishwasher","has_patio","has_gym"]]

label = manhattan["rent"]
print(data.shape)               # (3539, 15)
print(label.shape)              # (3539, )

train_data,test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3, random_state=0)
    
lr = LinearRegression()
model = lr.fit(train_data,train_label)
print()
print(model.score(train_data,train_label))  # 0.78
print(model.score(test_data,test_label))    # 0.77


data = manhattan[["bedrooms","bathrooms","size_sqft"]]
label = manhattan["rent"]
train_data,test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3, random_state=0)
model = lr.fit(train_data,train_label)
print()
print(model.score(train_data,train_label))  # 0.76
print(model.score(test_data,test_label))    # 0.76

#predict = model.predict(train_data)
#plt.plot(predicts, lable="predict")
# #plt.plot( train_label, label="price")
# plt.scatter(train_label,predicts,alpha=0.5)
# plt.xlabel("price")
# plt.ylabel("predict")
#
# plt.legend()
# plt.show()

my = [[1,1, 1200]]
result = model.predict(my)
print(result)




