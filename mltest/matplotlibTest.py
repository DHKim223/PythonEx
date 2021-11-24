import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plot
s = pd.Series(np.random.randn(100), index=np.arange(0,100))
#print(s)
s=s.cumsum()
#s.plot()
plt.plot(s)
plt.clf()       # 초기화

x = np.random.randn(100)
y = np.random.randn(100)
#plt.plot(x,y)
#plt.plot(x,y,"bo")
#plt.plot(x,y,"r^")
plt.clf()

# Bar 
s =pd.Series(np.random.randn(20) )
#s.plot(kind="bar")
#s.plot(kind="barh")
#plt.bar(s.index,height=s.values)
plt.barh(s.index,width=s.values)
plt.clf()

df = pd.DataFrame(np.random.randn(10,4), columns=["A","B","C","D"], index=list("abcdefghij"))
#df.plot(kind="bar")
#df.plot(kind="barh", stacked = True)
plt.bar(df.index,df["A"])
plt.bar(df.index, df["B"], bottom = df["A"])
plt.bar(df.index, df["C"], bottom = df["B"])
plt.bar(df.index, df["D"], bottom = df["C"])
plt.clf()

# Histogram
s = pd.Series( np.random.randn(200))
#s.hist(bins=50)     # 막대기 갯수
a = 2.0 * np.random.randn(1000) + 1.0
b = np.random.standard_normal(1000)
plt.hist(a, bins=100, alpha = 0.5, density = True)
plt.hist(b, bins=100, alpha = 0.5, density= True)
plt.clf()

#  Scatter 
x = np.random.normal(1, 1, size=(1000,1))
y = np.random.normal(-2, 4, size=(1000,1))
#plt.scatter(x,y,alpha=0.5)
data = np.concatenate((x,y), axis=1)
df = pd.DataFrame(data,columns=["X","Y"])

plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.clf()

# Box Plot
import seaborn as sns
iris = sns.load_dataset("iris")
#print(iris)
data = [iris [ iris["species"]== "setosa"]["sepal_length"],
            iris [ iris["species"]== "versicolor"]["sepal_length"],
            iris [ iris["species"]== "virginica"]["sepal_length"]]
        
#print(data)
plt.boxplot( data, labels=["setosa","versicolor","virginica"],showmeans=True)
plt.clf()

# 옵션
fig = plt.figure()
fig.figsize = (200,100)
ax1 = fig.add_subplot(2,2,1)
s = pd.Series(np.random.randn(50), index = np.arange(0,50))
ax1.plot(s)

ax2 = fig.add_subplot(2,2,2)
s = pd.Series(np.random.randn(50))
ax2.bar(s.index,height=s.values)

ax3 = fig.add_subplot(2,2,3)
ax3.hist(s , bins=50)

ax4 = fig.add_subplot(2,2,4)
x = np.random.normal(1,2,size=(100,1))
y = np.random.normal(2,1,size=(100,1))
ax4.scatter(x,y,alpha=0.5)
plt.clf()

fig = plt.figure()
fig.size = (200,200)
x = np.random.normal(1,2,size=(200,1))
y = np.random.normal(2,5,size =(200,1))
ax = fig.add_subplot(1,1,1)
#ax.scatter(x,y,alpha=0.5)
ax.scatter(x,y,alpha=0.5,c="r",marker="p")
ax.set_xlim(-10,10)
ax.set_ylim(-20,20)
ax.set_title("Distance")
ax.set_xlabel("x_point")
ax.set_ylabel("y_point")
ax.set_xticks(np.arange(x.min(), x.max(),2))
ax.set_yticks(np.arange(y.min(), y.max(),2))



plt.show()


