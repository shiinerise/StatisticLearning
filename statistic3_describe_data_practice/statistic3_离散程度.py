import pandas as pd
import numpy as np
from collections import Counter
df = pd.read_excel('data/3_table1.xlsx')
data = df['月收入']
# 异众比率
# 众数
count = Counter(data)
modeCount = count.most_common(1)[0][1]
totalCount = len(data)
# 异众比率
ratio = (totalCount - modeCount) / totalCount
print('异众比率为：', ratio)

# 四分位差
# 法一
print('四分位差为：', np.percentile(data, 75) - np.percentile(data, 25))
# 法二
print('四分位差为：', data.quantile(.75) - data.quantile(.25))

# 极差
print('极差为：', data.max() - data.min())

# 平均差
meanData = data.mean()
s = 0
for i in data:
    s += (abs(i - meanData))
print('平均差为：', s/len(data))

# 方差
print('方差为：', np.var(data))

# 标准差
print('标准差为：', np.std(data))

# 偏度
from scipy import stats
print('偏度为：', stats.skew(data))

# 峰度
print('峰度为：', stats.kurtosis(data))