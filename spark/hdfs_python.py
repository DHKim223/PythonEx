from hdfs import InsecureClient
client = InsecureClient("http://192.168.56.100:9870", user="hdfs")

import os
import time
def load_txt(path):
    files = client.list(path)
    data = []
    label = []
    for filename in files :
        #print(filename)
        lang = filename.split("-")
        label.append(lang[0])
        file = os.path.join(path,filename)
        try :
            with client.read(os.path.join(path, filename), encoding="utf-8") as f :
                print(file)
                langfile = f.read()
                langtext = langfile.lower()
                a = ord("a")        # 97
                z = ord ("z")       # 133
                counts = [i for i in range(26)]
                for char in langtext :
                    code = ord( char )
                    if code >= a and code <= z :
                        counts[code-a] += 1
                total = sum( counts )
                count = list(map(lambda x : x/total, counts))   # 정규화
                data.append(count)         
            print(data)
        except Exception:
            time.sleep(1)
    return data,label
print("finished")
train_data, train_label = load_txt("/input/lang/train/")
test_data, test_label = load_txt("/input/lang/test/")
