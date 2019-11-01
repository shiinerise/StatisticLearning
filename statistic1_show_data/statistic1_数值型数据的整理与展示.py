# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import math
from itertools import groupby
import numpy as np
# 设置正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

# 按照固定区间长度绘制频率分布直方图
# bins_interval 区间的长度
# margin        设定的左边和右边空留的大小
def probability_distribution(data, bins_interval=1, margin=1):
    bins = range(min(data)-1, max(data) + bins_interval, bins_interval)
    # print(len(bins))
    for i in range(0, len(bins)):
        print(bins[i])
    plt.xlim(min(data) - margin, max(data) + margin)
    plt.title("某电脑公司销售量分布的直方图")
    plt.xlabel('销售量（台）')
    plt.ylabel('频数（天）')
    # 频率分布density=True，频次分布density=False
    prob,left,rectangle = plt.hist(x=data, bins=bins, density=False, histtype='bar', color=['r'])
    # for x, y in zip(left, prob):
        # 字体上边文字
        # plt.text(x + bins_interval / 2, y + 0.003, '%.2f' % y, ha='center', va='top')
        # plt.text(x + bins_interval / 2, y + 0.25, '%.2f' % y, ha='center', va='top')
    plt.show()

# 茎叶图
def stem(data, n):
    for k,g in groupby(sorted(data),key = lambda x: math.floor(x/n)):
        lst = map(str, [d % n for d in list(g)])
        print(k, '|', ' '.join(lst))

# 箱线图
def boxplot(data):
    plt.boxplot(data, labels=['销售量（台）'])
    plt.title('某电脑公司销售量数据的箱线图')
    plt.show()

if __name__ == '__main__':
    df = pd.read_excel('data/1_table4.xlsx')
    data = df['销售量'].values
    # print(data)
    probability_distribution(data=data, bins_interval=10, margin=10)
    stem(data, 10)
    boxplot(data)
