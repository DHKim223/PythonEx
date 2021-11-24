#로지스틱 회귀
#이항분류
# 공부시간 , 출석일수
import numpy as np
from sklearn.model_selection._split import train_test_split
from sklearn import metrics
from sklearn.preprocessing._data import StandardScaler
from sklearn.model_selection._search import GridSearchCV
from sklearn.ensemble._forest import RandomForestClassifier


data = np.array( [[5,7],[4,1],[5,8],[9,9],[9,8],
                            [8,9],[5,5],[7,8],[8,7],[7,7],
                            [8,8],[8,1],[9,2],[9,8],[8,7],
                            [4,5],[6,1],[5,4],[5,5],[6,7],
                            [6,6],[6,5],[6,9],[8,3],[8,7],
                            [5,5],[6,2],[9,6],[9,9],[9,4]])
                            
 
label = np.array([ 0,0,0,1,1,1,0,1,1,0,
                            1,0,0,1,1,0,0,0,0,0,
                            0,0,1,0,1,0,0,1,1,1 ])
train_data, test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3, random_state=0 )
    
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
model = lr.fit(train_data, train_label)
predicts = model.predict(test_data)
score = metrics.accuracy_score(test_label, predicts)
print(score)

# print(model.score(train_data,train_label))
# print(model.score(test_data, test_label))

score = metrics.precision_score(test_label,predicts)
print(score)

score = metrics.f1_score(test_label,predicts)
print(score)

score = metrics.roc_auc_score(train_label, lr.decision_function(train_data))
print(score)
score = metrics.roc_auc_score(test_label, lr.decision_function(test_data))
print(score)

predict = model.predict([[5,5]])
predict = model.predict([[9,6]])
yn = np.array(["불합격","합격"])
print(yn[predict])

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(data, columns=["hour","attendance"])
df["pass"] = label
#sns.pairplot(df)
sns.pairplot(df,hue="pass")
#plt.show()

# 의사 결정 트리
# 붓꽃 품종 분류
from sklearn.datasets import load_iris
iris = load_iris()
#print(iris.DESCR)
data = iris.data
label = iris.target
#print(data.shape)   # (150,4)
#print(label.shape)  # (150, )
names = iris.target_names
print(data[:5,:])
data = data[:,2:4]

train_data, test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3, random_state=0)
    
sc = StandardScaler()
sc.fit(train_data)
sc.fit(test_data)
train_data = sc.transform(train_data)
test_data = sc.transform( test_data)
#print(test_data[:5, : ])

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy",max_depth=3, random_state=0)
model = dtc.fit(train_data, train_label)
print(model.score(train_data, train_label)) # 0.98
print(model.score(test_data, test_label))   # 0.97

test = [[2.5,1.4]]
sc.fit(test)
test = sc.transform(test)
predict = model.predict(test)
print(names[predict])

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
dot_data = export_graphviz( dtc, \
                                          feature_names=["petal Length","petal Width"],
                                          class_names=names, filled=True, special_characters=True)
graph = graph_from_dot_data(dot_data)
#graph.write_png("iris.png")

# 암 검진 분류
from sklearn.datasets import load_breast_cancer 
cancer = load_breast_cancer()
#print(cancer.DESCR)
data = cancer.data
label = cancer.target
#print(data.shape)       # (569,30)
#print(label.shape)      # (569, )
#print(data[0])
train_data, test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3,random_state=0)
    
#print( cancer.feature_names)
dtc = DecisionTreeClassifier(max_depth=5, random_state = 0)
model = dtc.fit(train_data,train_label)
print( model.score(train_data, train_label))    #0.98
print(model.score(test_data,test_label))        #0.93

malignant = cancer.data[cancer.target==0]       #양성
benign = cancer.data[cancer.target==1]              #음성

# plt.figure(figsize=(12,6))
# for i in range(len(cancer.feature_names)) :
    # plt.subplot(8,4,i+1)
    # plt.hist(malignant[:,i],bins=20, alpha=0.5)
    # plt.hist(benign[:i],bins=20,alpha=0.5)
    # plt.title(cancer.feature_names[i])
# plt.show()

from sklearn.metrics import confusion_matrix
predicts = model.predict(test_data)
print(confusion_matrix(test_label,predicts))

#              예측    
#   실    [[ 60   3]
#   제     [  8 100]]

from sklearn.metrics import classification_report
print( classification_report(test_label,predicts))

                    # precision    recall  f1-score   support
                    #
                    # 0       0.88      0.95      0.92        63
                    # 1       0.97      0.93      0.95       108
                    #
    #           accuracy                           0.94       171
   #   macro avg       0.93      0.94      0.93       171
# weighted avg       0.94      0.94      0.94       171

from sklearn.metrics import roc_auc_score
print(roc_auc_score(test_label,predicts))

dot_data = export_graphviz(dtc,out_file=None,\
                                                feature_names=cancer.feature_names,\
                                                class_names=cancer.target_names, \
                                                filled=True,rounded=True,special_characters=True)
graph = graph_from_dot_data(dot_data)
graph.write_png("cancer.png")

# plt.figure(figsize=(8,6))
# plt.xlabel("importance")
# plt.ylabel("features")
# plt.yticks(np.arange(len(cancer.feature_names) ),cancer.feature_names)
# plt.barh(range(len(cancer.feature_names) ), model.feature_importances_)
# plt.show()

import seaborn as sns

# df = pd.DataFrame(data,columns=cancer.feature_names)
# sy = pd.Series(label,dtype="category")
# sy = sy.cat.rename_categories(cancer.target_names)
# df["class"] = sy
# sns.pairplot(vars=["worst radius","worst texture", "worst perimeter","worst area"],\
                    # hue = "class", data=df)
# plt.show()

# 랜덤 포레스트
cancer = load_breast_cancer()
data = cancer.data
label = cancer.target
label_names = cancer.target_names
feature_names = cancer.feature_names
train_data,test_data, train_label,test_label = \
    train_test_split(data,label,test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier( n_estimators=100, random_state=0 )
model = rfc.fit(train_data,train_label)
print()
print("#################################################################")
plt.clf()
print(model.score(train_data, train_label)) #1.0
print(model.score(test_data, test_label))   # 0.96

# n_features = len(feature_names)
# plt.barh(range(n_features),model.feature_importances_,align="center")
# plt.yticks(np.arange(n_features),feature_names)
# plt.xlabel("importance")
# plt.ylabel("feature")
# plt.show()

params = {"n_estimators":[5,10,15,20],
                    "max_depth":[4,5,6],
                    "min_samples_Leaf":[10,12,14],
                    "min_samples_split":[10,12,14]}
cv = GridSearchCV( RandomForestClassifier( random_state=0 ),params,n_jobs=1)
models = cv.fit( train_data, train_label )
model = models.best_estimator_
print( models.best_params_)

predicts = model.predict(test_data)
report = classification_report(test_label, predicts )
print(report)





