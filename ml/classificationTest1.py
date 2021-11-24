# 랜덤 포레스트
# 식용버섯 분류
import urllib.request as req
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
# req.urlretrieve(url, "mushroom.csv")
# print("다운로드 완료")

mr = pd.read_csv("mushroom.csv", header=None )
print(mr.iloc[:5,:])

data = []
label = []
for index, row in mr.iterrows():
    label.append(row.loc[0])
    row_data = []
    for value in row.loc[1:] :
        row_data.append(ord ( value ) )             # 문자를 숫자로
    data.append(row_data)    
data = np.array(data)
label = np.array(label)
# print( data.shape )         #(8124,22)
# print( label.shape)         #(8124, )
print(data[:5, :])

train_data, test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3, random_state = 0)
    
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
model = lr.fit(train_data, train_label)
print(model.score(train_data,train_label))  #0.94
print(model.score(test_data, test_label))       #0.94

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
model = nb.fit(train_data, train_label)
print(model.score(train_data, train_label))     # 0.9
print(model.score(test_data, test_label))      # 0.9

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
model = dtc.fit(train_data, train_label)
print(model.score(train_data, train_label))     # 1.0
print(model.score(test_data, test_label))       # 1.0

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=10, random_state=0)
model = rf.fit( train_data, train_label)
print(model.score(train_data, train_label))     #1.0
print(model.score(test_data, test_label))       #1.0

from sklearn.metrics import confusion_matrix
predicts = model.predict(test_data)
cm = confusion_matrix(test_label, predicts)
            
import seaborn as sns
import matplotlib.pyplot as plt
# f, ax = plt.subplot( figsize=(5,5) )
# sns.heatmap( cm, annot=True, linewidths=0.5, \
                        # linecolor="red", fmt=".0f", ax=ax)
# plt.xlabel ( "predict")
# plt.ylabel("label")
# plt.show()

from sklearn.metrics import accuracy_score, classification_report
score = accuracy_score(test_label, predicts)
print(score)
scores = classification_report(test_label, predicts)
print(scores)

                # precision    recall  f1-score   support
#
                    # e       1.00      1.00      1.00      1272
                    # p       1.00      1.00      1.00      1166
                    #
              # accuracy                           1.00      2438
     # macro avg       1.00      1.00      1.00      2438
# weighted avg       1.00      1.00      1.00      2438

# SVM
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data = iris.data
label = iris.target
train_data, test_data, train_label, test_label=\
    train_test_split(data,label,test_size=0.3, random_state=0)
    
#알고리즘 설정    
from sklearn import svm
al = svm.SVC()          # 0.97, 0.97            

from sklearn.neighbors import KNeighborsClassifier
al = KNeighborsClassifier(3)            # 0.96,   0.97

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF        #1.0,  0.977
al = GaussianProcessClassifier(1.0 * RBF(1.0))

from sklearn.ensemble import AdaBoostClassifier
al = AdaBoostClassifier()           # 0.96        0.91

from sklearn.naive_bayes import GaussianNB
al = GaussianNB()                   # 0.94,     1.0

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
al = QuadraticDiscriminantAnalysis()            #0.99      0.97

model = al.fit(train_data,train_label)
print(model.score(train_data, train_label))
print(model.score(test_data, test_label))

# SVM
# BMI 과체중 분류

#파일생성
# def bmi(h , w ):
    # b = w / ((h/100)**2)
    # if b < 18.5 :
        # return "thin"
    # elif b < 25 :
        # return "normal"
    # else : 
        # return "fat"
        #
# import random
# with open("bmi.csv","w",encoding="utf-8") as f :
    # f.write("height,weight,bmi\n")
    # for i in range( 20000 ) :
        # h = random.randint(120,200)
        # w = random.randint(40,150)
        # b = bmi(h,w)
        # f.write("{0},{1},{2}\n".format(h,w,b))
# print("파일생성")

bmi = pd.read_csv("bmi.csv",encoding="utf-8")
label = bmi["bmi"]
h = bmi["height"]
w = bmi["weight"]
# 가중치 없애기 위해서,,
h = (h - h.min())/(h.max() - h.min())
w = (w - w.min())/(w.max() - w.min())
data = pd.concat( (h,w), axis=1 )
# print( data.shape)      # (20000,2)
# print( label.shape)     # ( 20000, )

train_data, test_data, train_label, test_label = \
    train_test_split( data, label, test_size=0.3, random_state=0 )

svc = svm.SVC()
model = svc.fit( train_data, train_label )
print( model.score( train_data, train_label ) )         # 0.99
print( model.score( test_data, test_label ) )           # 0.99

hp = ( 170 - h.min() ) / ( h.max() - h.min() )
wp = ( 70 - w.min() ) / ( w.max() - w.min() )

predict = model.predict( [[hp, wp]]) 
print( predict )

import matplotlib.pyplot as plt
fig = plt.figure( figsize=(8, 4) )
ax1 = fig.add_subplot( 1, 2, 1 )
def scatter( ax, label, color ) :
    b = bmi[ bmi["bmi"] == label ]
    ax.scatter( b["weight"], b["height"], color=color, \
                marker=".", label=label, alpha=0.5 )
    ax.legend()
scatter( ax1, "fat", "red" )
scatter( ax1, "normal", "green" )
scatter( ax1, "thin", "yellow" )

predicts = model.predict( data )
ax2 = fig.add_subplot( 1, 2, 2 )
def scat( ax, label, color ) :
    b = bmi[ predicts == label ]
    ax.scatter( b["weight"], b["height"], color=color, \
                marker=".", label=label, alpah=0.5 )
    ax.legend()
scatter( ax2, "fat", "red" )
scatter( ax2, "normal", "green" )
scatter( ax2, "thin", "yellow" )

plt.show()    

# 종양 분석
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
#print(cancer.target_names, np.bincount(cancer.target))
data = cancer.data
label = cancer.target
train_data, test_data, train_label, train_label = \
    train_test_split(data, label, test_size=0.3, random_state=0)
    
svc = svm.SVC()
model = svc.fit(train_data, train_label)
print(model.score(train_data, train_label))
print(model.score(test_data, test_label))

# 정규화
min_data = data.min(axis=0)
range_data = (data - min_data).max(axis=0)
train_data_scaled = (train_data - min_data) / range_data
test_data_scaled = (test_data - min_data)   / range_data
#
# import matplotlib.pyplot as plt
# plt.boxplot( train_data_scaled, manage_ticks=False )
# plt.xlabel( "features" )
# plt.ylabel( "size" )
# plt.show()

model = svc.fit( train_data_scaled, train_label)
print(model.score(train_data_scaled, train_label))      #0.98
print(model.score(test_data_scaled,test_label))         #0.97

svc = svm.SVC( C=1000 )
svc.fit( train_data, train_label)
print(model.score(train_data_scaled,train_label))
print(model.score(test_data_scaled, test_label))

