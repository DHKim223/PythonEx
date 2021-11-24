#pandas
#Series                1차원
#Dataframe        2차원

import pandas as pd
from pickle import NONE

s = pd.Series([1, 2, 3, 4,5,6,7,8,9,10 ])
print(s.index)
print(s.values)
print(type(s))
print(s.dtype)

ss = pd.Series([1, 2, 3, 4,5,6,7,8,9,10 ], \
              ["a","b","c","d","e","f","g","h","i","j"])
print(type(ss))
print(ss.index)
print(ss.values)
print(ss[0])
print(ss["c"])
print(ss.g)
print(ss[0:5])

dict = { "A":10, "B":20, "C":30, "D":40}
print (type(dict))
print(dict)
print(dict["A"])
# print(dict.A)         dict 이라 에러

sd = pd.Series(dict)        # dict -> Series
print(type(sd))
print(sd["A"])
print(sd.A)         #  Series라 가능
print(type(sd.values))

# Dictionary - > DataFrame
d = {"name":["kim","Lee","Park","Choi"], "age":[20,30,40,50] , "tel":["1111-1111","1111-2222","2222-3333","3333-4444"] }

df = pd.DataFrame(d)
print(type(df))     # Dataframe
print(df)
print(df.columns)
print(df.index)
print(df.values)        # numpy array
df.index.name = "Num"
df.columns.name = "User"
print (df)
print(df.index)
print(df.columns)

# ndarray -> DataFrame
import numpy as np
n = np.array ([["kim",20,"1111-2222"],
                        ["lee",30,"1111-3333"],
                        ["hong",40,"2222-3333"],
                        ["park",50,"3333-4444"]   ])
print(type(n))
df = pd.DataFrame(n)
print(type(df))
print(df.index)
print(df.columns)
print(df)
df = pd.DataFrame(n,columns=["name","age","tel"],\
                                        index =["a","b","c","d"])
print(df)
print(df.describe())
desc = df.describe()
print(desc.index)
print(desc.name)
print(desc.name[1])
print()

print(df["name"])
print(df["age"])
print(type(df["age"]))
print(df["name"][0])
print(df[["name","age"]]) # 2차원 배열이라 [] 두개
print(df[["name","tel"]])
print(df[:][:])
print(df[:2])
print(df[:2][:1])
print(df.name, df.age)

df["address"] = ["서울","수원","인천","안산"]       #col 추가
print(df)

for i, age in enumerate( df["age"]):
    df["age"][i] = int(age)
    
df["age"] = [int(age) for age in df["age"]]    
    
df["adult"] = df["age"] < 30

df["age"][0] = 28
print(df)

print("##################")
print()

#iloc
df = pd.DataFrame(np.arange(10,26).reshape(4,4), columns=["a","b","c","d"])
print(df)
print(df[0:1])
print(df[["a","c"]])
# print( df[["a":"c"]])        에러
# print( df[1][0:2])            에러
# print( df[[1]["a","c"]])    에러
# print( df[1][["a","c"]])    에러
# print( df[1,1] )                에러
# print(df.loc[1,1])            에러
print(df.iloc[1,1])
print(df.iloc[0:2, 0:2])
print(df.iloc[0:2, :-1])
print(df.iloc[2: , 2:])

# loc
print(df[0:2])
print(df["a"][1])
print(df.loc[:2,:"b"])
print(df.loc[0,"a":"c"])
df.loc[:,"e"] = [30,31,32,33]
df["f"]=[40,41,42,43]
df.loc[4] = [50,51,52,53,54,55]
df.loc[0,"a"] = 99
df.loc[4, ["a","b","c"]] = [90,91,92]
df = df.drop("f",axis=1)
df = df.drop(4, axis=0)
print(df.iloc[::,::])
print(df.iloc[::2,::2])
print(df.iloc[::-1,::-1])

#print(df)

# boolean indexing
df = pd.DataFrame([["Kim",20,"1111-2222"],
                                ["Lee",30,"2222-3333"],
                                ["Park",40,"1111-3333"],
                                ["Hong",20,"3333-1111"],
                                ["Jung",30,"3333-3333"]             
                   ],columns=["name","age","tel"])

#print(df.loc[:,["name","age"]])
#print(df.iloc[:,0:2])

print(df.loc[df["age"]>20,["name","age"] ])
print(df.loc[df["name"] == "kim",["name","tel"]])
print(df.loc[ (df["age"] >=20) & (df["age"]<=30),["name","age"] ])

# 결측값 대체
df["address"]=""

df.loc[ df["address"] == "",["address"]] = "서울"
df.loc[::2,["address"]] = None
df.loc[ df["address"].isnull(),["address"]]= "수원"

# 결측값 제거
df.loc[:,"income"] = [400,500,None,200,np.NaN]
df.loc[5,:] = [np.NaN, np.NaN,np.NaN,np.NaN,np.NaN ]

#df = df.dropna(how="all")
#df.dropna(how="any")
#df.dropna(how= "any", inplace=True)

# df["income"].fillna(value = 0 , inplace=True )
# df["income"].fillna( value=np.mean(df["income"]), inplace=True)

#print(df.isnull())

# 분석용 함수
print(df)
print(df.count())
print(df.count(axis=1))
print(df.min())
print(df.max())
print(df.sum())
print(df.mean())

df = pd.DataFrame( [["kim",75,89,45],
                                    ["lee",65,77,83],
                                    ["park",np.NaN,85,np.NaN],
                                    ["hong",75,np.NaN,70],
                                    ["jung",np.NaN,np.NaN,np.NaN],
                                    ["kang",67,88,97]],
                                    columns=["name","kor","eng","mat"])

df["tot"] = df.sum(axis=1)
df["avg"] = df.loc[:,"kor":"eng"].mean(axis=1)
print(df)

print(df.median())
print(df.mad()) # 편차
print(df.std()) #표준편차
print(df.var() )    #분산
print(df.loc[:,"kor":"mat"].cumsum(axis=1)) # 누적합
print(df.loc[:,"kor":"mat"].cumprod(axis=1)) # 누적곱
print(df.loc[:,"kor":"mat"].idxmin(axis=1))
print(df.loc[:,"kor":"mat"].idxmax(axis=1))

#상관관계 분석
# 양수 1에 가까우면 양의 상관관계
# 음수 1에 가까우면 음의 상관관계
print(df["kor"].corr(df["mat"]))
print(df["kor"].corr(df["eng"]))

# 공분산
# 값이 클수록 관계가 깊다
print( df["kor"].cov(df["mat"]))
print(df["mat"].cov(df["avg"]))

#sort
print(df.sort_index(axis=0,ascending=False))
print(df.sort_values(by="avg", axis=0, ascending=False))

print(df["mat"].unique())
print(df["mat"].value_counts()) #NaN 제외
print(df["name"].isin(["kim","lee"]))
print(df.loc[ df["name"].isin(["kim","lee"])])