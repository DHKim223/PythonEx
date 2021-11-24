# 군집화
# K-means
# make_blobs
from sklearn.datasets import make_blobs
data, label = make_blobs( 300, random_state=0 )
print(data.shape)       #(300, 2)
print(label.shape)      #(300, )

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3)
model = km.fit(data)
#print(model.score(data, label))
predicts = model.predict(data)
print(predicts)




import matplotlib.pyplot as plt
import numpy as np
# fig = plt.figure( figsize=(8, 4) )
# ax1 = fig.add_subplot( 1, 2, 1 )
# colors = np.array( ["red", "green", "blue"] )
# ax1.scatter( data[:,0], data[:,1], color=colors[label[:]], alpha=0.5 )
# #plt.show()
#
# ax2 = fig.add_subplot( 1, 2, 2 )
# ax2.scatter( data[:,0], data[:,1], color=colors[model.labels_], alpha=0.5 )
# ax2.scatter( model.cluster_centers_[:,0], model.cluster_centers_[:,1], \
             # color="k", marker="^")
             #
# plt.show()

# 엘보우 기법
# 적정한 K값 ( 군집의 갯수) 를 찾아준다.
# 왜곡이 급격히 변하는 위치를 찾아 준다.
# from scipy.spatial.distance import cdist
# distortions = []            # 왜곡        데이터와 센터의 간격이 클수록 왜곡이 심하다
# ks = range( 1, 10 )
# for k in ks :
    # km = KMeans( n_clusters=k )
    # model = km.fit( data ) 
    # distortions.append( sum( np.min( cdist( \
        # data, model.cluster_centers_, "euclidean"), axis=1)) / data.shape[0] ) 
# plt.plot( ks, distortions, "bx-" )
# plt.xlabel( "K" )
# plt.ylabel( "Distotion" )
# plt.show()

# 실루엣 기법
# 0에 가까울 수록 군집화, 1에 가까울 수록 분리
# from sklearn.metrics import silhouette_samples
# from matplotlib import cm
# predicts = model.predict(data)
# clust_labels = np.unique(predicts)
# n_cluster = clust_labels.shape[0]
# silhouette_values = silhouette_samples(data,predicts, metric="euclidean")
# y_ax_lower, y_ax_upper = 0, 0
# yticks = []
# for i, c in enumerate( clust_labels):
    # c_silhouette_values = silhouette_values[predicts == c]
    # c_silhouette_values.sort()
    # y_ax_upper += len(c_silhouette_values)
    # color = cm.jet(float(i)/n_cluster)
    # plt.barh(range(y_ax_lower, y_ax_upper),c_silhouette_values, \
        # height = 1.0, edgecolor = "none", color = color )
    # yticks.append((y_ax_upper+y_ax_lower)/2)
    # y_ax_lower += len(c_silhouette_values)
    #
# silhouette_avg = np.mean (c_silhouette_values)
# plt.axvline(silhouette_avg, color="red", linestyle="--")
# plt.yticks(yticks, clust_labels +1 )
# plt.ylabel("cluster")
# plt.xlabel("Silhouette Coefficient")
# plt.show()
        #
        
# 붓꽃 분류
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data[:,2:4]
label = iris.target

from sklearn.cluster import KMeans
km = KMeans( n_clusters=3 )
model = km.fit( data )
predicts = model.predict( data )

# import matplotlib.pyplot as plt
# import numpy as np
# fig = plt.figure( figsize=(8,4) )
# ax1 = fig.add_subplot( 1, 2, 1 )
# colors = np.array( ["red", "green", "blue"] )
# ax1.scatter( data[:, 0], data[:,1], color=colors[label[:]], alpha=0.5 )
#
# ax2 = fig.add_subplot( 1, 2, 2 )
# ax2.scatter( data[:, 0], data[:,1], color=colors[predicts[:]], alpha=0.5 )
# plt.show()

print( model.score( data, label ) )         # -31
from sklearn.metrics import accuracy_score
score = accuracy_score( label, predicts )
print( score )                              # 0.02

from sklearn.metrics import confusion_matrix
result = confusion_matrix( label, predicts )
print( result )    

#DBSCAN
# 밀도기반 군집화
from sklearn.datasets import make_moons
data,label = make_moons(n_samples=300, noise = 0.05, random_state=40)
km = KMeans(n_clusters=2, random_state=0)
model = km.fit(data)
predicts = model.predict(data)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,2,1)
colors = np.array(["red","blue"])
ax1.scatter(data[:,0], data[:,1], color=colors[predicts[:]], alpha=0.5)

ax2 = fig.add_subplot(1,2,2)
ax2.scatter( data[:,0], data[:,1], color=colors[label[:]],alpha=0.5)

from sklearn.cluster import DBSCAN
scan = DBSCAN( eps=0.3, min_samples=5 )
model = scan.fit( data )

fig = plt.figure( figsize=(8, 4) )
ax1 = fig.add_subplot( 1, 2, 1 )
colors = np.array( ["red", "blue"] )
ax1.scatter( data[:,0], data[:,1], color=colors[scan.labels_], alpha=0.5 )

ax2 = fig.add_subplot( 1, 2, 2 )
ax2.scatter( data[:,0], data[:,1], color=colors[label[:]], alpha=0.5)
plt.show()
        

    
    

