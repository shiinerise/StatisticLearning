import pandas as pd
df = pd.read_excel('data/3_table1.xlsx')
data = df['月收入']
# 众数
# 法一
print('众数为：', data.mode().iloc[0])
# 法二
from collections import Counter
counts = Counter(data)
print('众数为：', counts.most_common(1)[0][0])
# 法三
from scipy.stats import mode
mode_num = mode(data)
print('众数为：', mode_num[0][0])

# 中位数
# 法一
print('中位数为：', data.median())
# 法二
import numpy as np
print('中位数为：', np.percentile(data, 50))
# 法三
print('中位数为：', data.quantile(.50))

# 分位数
# 法一
print('下四分位数为：', np.percentile(data, 25))
print('上四分位数为：', np.percentile(data, 75))
# 法二
print('下四分位数为：', data.quantile(.25))
print('上四分位数为：', data.quantile(.75))

# 平均数
# 算数平均数
print('算数平均数为：', data.mean())
# 几何平均数
import math
s = 1
for i in data:
    s *= i
print('几何平均数为：', math.pow(s, 1/len(data)))