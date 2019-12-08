import pandas as pd
from collections import Counter
import numpy as np
df = pd.read_excel('data/2_table1.xlsx')
# print(df)
# 众数
count = Counter(df['月收入'])
mode = count.most_common(1)[0][0]
# print(mode)

# 中位数
median = np.median(df['月收入'])
# print(median)

def calculateQuartile(data, index):
    if isinstance(index, int):
        quartile = data[index]
    elif (index*100 % 100) == 50.0:
        quartile = (data[int(index) - 1] + data[int(index)])/2
    else:
        quartile = data[int(index)-1] + (data[int(index)] - data[int(index)-1]) * (index*100%100) / 100
    return quartile

if __name__ == '__main__':
    df = pd.read_excel('data/2_table1.xlsx')
    # 四分位数
    data = np.sort(df['月收入'])
    # 下四分位数
    index1 = len(data)/4
    print('下四分位数为', calculateQuartile(data, index1))
    # 上四分位数
    index2 = 3 * len(data) / 4
    print('上四分位数为', calculateQuartile(data, index2))