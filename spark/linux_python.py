import os.path, glob

def load_txt(path):
    files = glob.glob(path)
    data = []
    label = []
    for filename in files:
        file = os.path.basename(filename)
        lang = file.split("-")
        langfile = open(filename,"r",encoding="utf-8").read()
        langtext = langfile.lower()     # 소문자로 바꿔라
        code_a = ord("a")
        code_z = ord("z")
        count = [i for i in range(0, 26)]
        for char in langtext :
            char_code = ord(char)
            if code_a <= char_code and code_z >= char_code :
                count[char_code - code_a] += 1
        total = sum(count)
        #print(lang[0], count)
        count = list( map (lambda n : n/total, count))
        #print(lang[0],count)
        data.append(count)
        label.append(lang[0])
    return data, label 
        
        
train_data, train_label = load_txt( "./lang/train/*.txt")
test_data,test_label = load_txt("./lang/test/*.txt")
import numpy as np
#print( np.array( train_data).shape) # (1,26)
#print(np.array(test_data).shape)    # (1,26)
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svc = SVC()
model = svc.fit(train_data, train_label )
predicts = model.predict(test_data)
score = accuracy_score(test_label, predicts)
print(score)

import matplotlib.pyplot as plt
import pandas as pd
graph_dict = {}
for i in range (0,len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not label in graph_dict :
        graph_dict[label] = data
asclist = [ [chr(i) for i in range (97, 97+26)]]
df = pd.DataFrame( graph_dict, index=asclist)
plt.style.use("ggplot")
df.plot(kind="bar", subplots=True, ylim=(0,0.15))
plt.savefig("lang.png")
plt.show()


