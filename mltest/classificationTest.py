#분류
# 붓꽃의 꽃받침의 길이와 너비로 종류를 예측
from sklearn.datasets import load_iris

iris = load_iris()
#print(iris)
#print(iris.DESCR)
data = iris.data
label = iris.target
names = iris.target_names

from sklearn.model_selection import train_test_split
train_data, test_data, train_label, test_label = \
    train_test_split(data, label, test_size=0.2, random_state=0)
from sklearn.svm import SVC
svc = SVC()
model = svc.fit(train_data, train_label)

print(model.score(train_data, train_label))
print(model.score(test_data,test_label ))

from sklearn import metrics
predicts = model.predict(test_data)
score = metrics.accuracy_score( test_label, predicts)
print(score)

result = model.predict([[5.7, 2.8, 10.0, 4.5]])
print( names[  result[0]  ])

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize = ( 6, 4))
color = np.array(["red","blue","green"])
#ax1 = fig.add_subplot(1,2,1)
#ax1.scatter(data[:2],data[:3], color=colors[label],alpha=0.5)

#predicts = model(data)
#ax2 = fig.add_subplot(1,2,2)
#ax2.scatter(data[:2],data[:3], color=colors[predicts],alpha=0.5)

#plt.show()

# K겹 교차검증

# GridSearchCV
from sklearn.model_selection import GridSearchCV
params = [
    {"C":[1,10,100,1000],"kernel":["linear"]},
    {"C":[1,10,100,1000],"kernel":["rbf"],"gamma":[0.001,0.0001]}
    ]
gs = GridSearchCV(svc, params, n_jobs=1)
models = gs.fit(data, label)
print(models.best_score_)
print(models.best_params_)
print(models.best_estimator_)
best_model = models.best_estimator_
result = best_model.predict([[2.5,5.6,4.7,5.5]])
print(names[result])