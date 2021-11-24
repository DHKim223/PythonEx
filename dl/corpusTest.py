# 형태소 처리
from konlpy.tag import Hannanum
hannanum = Hannanum()
str = u"나는 비빔밥을 먹었다"
# print(hannanum.analyze(str))        # 구 분석
# print(hannanum.morphs(str))         # 형태소 분석
# print(hannanum.nouns(str))          #명사 분석
# print(hannanum.pos(str))        # 형태소 분석 태깅

from konlpy.tag import Kkma
kkma = Kkma()
# print(kkma.morphs(str))     # 형태소 분석
# print(kkma.nouns(str))      # 명사 분석
# print(kkma.pos(str))        #형태소 분석 태깅
# print(kkma.sentences(str))  # 문장 분석

from konlpy.tag import Komoran
komoran = Komoran()
# print(komoran.morphs(str))  #형태소 분석
# print(komoran.nouns(str))  #명사 분석
# print(komoran.pos(str))  #형태소 분석 태깅

from konlpy.tag import Okt
okt = Okt()
# print(okt.morphs(str))  #형태소 분석
# print(okt.nouns(str))  #명사 분석
# print(okt.phrases(str)) # 구 분석
# print(okt.pos(str))  #형태소 분석 태깅

# Python Deep Learning
from sklearn.datasets import make_moons
data, label = make_moons( n_samples=500, noise=0.25, random_state=0 )

import matplotlib.pyplot as plt
import numpy as np
# colors = np.array( ["red", "blue"] )
# plt.figure( figsize=( 5, 5 ) )
# plt.scatter( data[:,0], data[:,1], color=colors[label[:]] ,alpha=0.5 )
# plt.show()

from sklearn.model_selection import train_test_split
train_data, test_data, train_label, test_label = \
    train_test_split(data,label,test_size=0.3, stratify=label, random_state=0, hidden_layer_sizes=[100,100])
    
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(solver="lbfgs", random_state=0)
model = mlp.fit(train_data, train_label)

import mglearn
mglearn.plots.plot_2d_separator(mlp, train_data, fill=True, alpha=0.3)
mglearn.discrete_scatter( train_data[:,0], train_data[:,1], train_label , alpha=0.5)
plt.xlabel("class0")
plt.xlabel("class1")
plt.show()
print(model.score(train_data, train_label))
print(model.score(test_data, test_label))

