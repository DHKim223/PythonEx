# 반증법에 의한 분석
# 키의 평균은 175다                    귀무가설    증명하고자 하는 가설    
# 키의 평균은 175가 아니다          대립가설
import numpy as np
np.random.seed(1)

#heights = [175 + np.random.normal(0,5) for i in range(100)]
heights = [180 + np.random.normal(0,5) for i in range(100)]
#print(heights)
from scipy import stats 
result = stats.ttest_1samp(heights,175)
print(result)
# p-value > 0.05  -> 신뢰할 수 없다 -> 대립가설 기각 -> 귀무가설 채택
# p-value < 0.05  -> 신뢰할 수 있다 -> 대립가설 채택 -> 귀무가설 기각

import pandas as pd
import random
df = pd.DataFrame({"a":[i*100 for i in range(1,100)],
                                "b":[i*-100 for i in range(1,100)],
                                "c":[i*random.randint(1,100) for i in range (1,100)]
                   })
corr = df.corr(method="pearson")
print(corr)

import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(corr, cbar=True, annot=True, annot_kws={"size":20},\
                        fmt=".2f", square=True, cmap="Blues" )
plt.show()