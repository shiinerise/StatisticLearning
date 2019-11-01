# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 设置正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('data/1_table5.xlsx')
print(df)

# 散点图
# 输入产量与温度数据
rainfall = df['降雨量'].values
production = df['产量'].values
colors = np.random.rand(len(rainfall))  # 颜色数组
plt.scatter(rainfall, production, s=200, c=colors)  # 画散点图，大小为 200
plt.xlabel('降雨量')  # 横坐标轴标题
plt.ylabel('产量')  # 纵坐标轴标题
plt.title('小麦产量与降雨量的散点图')
plt.show()

# 气泡图
tem = df['温度'].values
size = production
plt.scatter(tem, rainfall, s=production, c=colors, alpha=0.6)  # 画散点图, alpha=0.6 表示不透明度为 0.6
plt.xlabel('温度')  # 横坐标轴标题
plt.ylabel('降雨量')  # 纵坐标轴标题
plt.title('小麦产量与降雨量和温度的气泡图(气泡大小表示产量)')
plt.show()
