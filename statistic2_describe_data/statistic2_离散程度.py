import pandas as pd
from collections import Counter
import numpy as np
df = pd.read_excel('data/3_table1.xlsx')
# 众数
count = Counter(df['月收入'])
modeCount = count.most_common(1)[0][1]
print(modeCount)
totalCount = len(df['月收入'])
nomodeCount = totalCount - modeCount
# 异众比率
ratio = nomodeCount / totalCount
print(ratio)