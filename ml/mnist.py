#t10k-images.idx3-ubyte            test_data
#t10k-labels.idx1-ubyte            test_label
#train-images.idx3-ubyte        train_data
#train-labels.idx1-ubyte        train_label

#csv 로 변환
# import struct
# def to_csv(name,maxdata):
    # imagefile = open(name + "-images.idx3-ubyte","rb")
    # labelfile = open(name + "-labels.idx1-ubyte","rb")
    # csvfile = open(name+".csv","w",encoding="utf-8")
    # mag, imagecount = struct.unpack(">II",imagefile.read(8))
    # mag, labelcount = struct.unpack(">II",labelfile.read(8))
    # rows, cols = struct.unpack(">II",imagefile.read(8))
    # pixels = rows * cols
    #
    # for i in range( labelcount ):
        # if i > maxdata :
            # break
        # label = struct.unpack("B",labelfile.read(1))[0]
        # data = imagefile.read(pixels)
        # sdata = list(map(lambda n: str(n), data))
        # csvfile.write(str(label)+",")
        # csvfile.write(",".join(sdata)+"\n")
    # imagefile.close()
    # labelfile.close()
    # csvfile.close()
    #
    #
# to_csv("train",50000)                   # train.csv
# to_csv("t10k",10000)                    # t10k.cvs
# print("csv 변환완료")

def load_csv(file):
    labels = []
    data = []
    with open(file, "r") as f :
        for line in f :
            cols = line.split(",")
            if(len(cols) < 2) :
                continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n : int(n)/255, cols))
            data.append(vals)
            
    return {"labels":labels,"data":data}
            
    
train = load_csv ( "train.csv")
test = load_csv ( "t10k.csv")
print("CSV 로드완료")

from sklearn import svm, metrics
# svc = svm.SVC()
# train_data = train["data"]
# train_label = train["labels"]
# test_data = test["data"]
# test_label = test["labels"]
# model = svc.fit( train_data, train_label)
# predicts = model.predict(test_data)
# score = metrics.accuracy_score(test_label, predicts)
# print(score)
# report = metrics.classification_report( test_label, predicts)
# print(report)

# 0.9785
              # precision    recall  f1-score   support
              #
           # 0       0.98      0.99      0.99       980
           # 1       0.99      0.99      0.99      1135
           # 2       0.97      0.98      0.98      1032
           # 3       0.97      0.98      0.98      1010
           # 4       0.98      0.98      0.98       982
           # 5       0.98      0.97      0.98       892
           # 6       0.99      0.98      0.99       958
           # 7       0.98      0.97      0.97      1028
           # 8       0.97      0.98      0.97       974
           # 9       0.97      0.96      0.97      1009
           #
    # accuracy                           0.98     10000
   # macro avg       0.98      0.98      0.98     10000
# weighted avg       0.98      0.98      0.98     10000

import pandas as pd
train = pd.read_csv("train.csv",header=None)
test = pd.read_csv("t10k.csv",header=None)
def change(data) :
    output = []
    for d in data :
        output.append(float(d)/255)
        return output
train_data = list(map(change, train.iloc[:,1:].values))
test_data = list(map(change, test.iloc[:,1:].values))
train_label = train[0].values
test_label = test[0].values

svc = svm.SVC()
model = svc.fit( train_data, train_label)
predicts = model.predict(test_data)
score = metrics.accuracy_score(test_label, predicts)
print(score)
report = metrics.classification_report( test_label, predicts)
print(report)

#     0.1135
#                 precision    recall  f1-score   support
#
           # 0       0.00      0.00      0.00       980
           # 1       0.11      1.00      0.20      1135
           # 2       0.00      0.00      0.00      1032
           # 3       0.00      0.00      0.00      1010
           # 4       0.00      0.00      0.00       982
           # 5       0.00      0.00      0.00       892
           # 6       0.00      0.00      0.00       958
           # 7       0.00      0.00      0.00      1028
           # 8       0.00      0.00      0.00       974
           # 9       0.00      0.00      0.00      1009
           #
    # accuracy                           0.11     10000
   # macro avg       0.01      0.10      0.02     10000
# weighted avg       0.01      0.11      0.02     10000