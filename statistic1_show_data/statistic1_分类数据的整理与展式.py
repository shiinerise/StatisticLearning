# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
# 设置正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('data/1_table3.xlsx')
print(df)

# 频数分布表
data = [(df.loc[:, x].value_counts()) for x in df.columns]
# print(data)

# 条形图
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
plt.subplot2grid((1, 2), (0, 0))  # 在一张大图里分列几个小图，位置是(0，0)
data1 = df['顾客性别'].value_counts(ascending=True)
data1.plot(kind='bar',
           title='顾客性别')
print(data1)
plt.xlabel("顾客性别")
plt.ylabel("频数")

plt.subplot2grid((1, 2), (0, 1))
data2 = df['饮料类型'].value_counts(ascending=True)
data2.plot(kind='bar',
           title='饮料类型')
plt.xlabel("顾客性别")
plt.ylabel("频数")
print(data2)

plt.show()

# 饼图
# 控制饼图为正圆
plt.axes(aspect='equal')
# plot方法对序列进行绘图
data2.plot(kind='pie',  # 选择图形类型
           autopct='%.1f%%',  # 饼图中添加数值标签
           radius=1,  # 设置饼图的半径
           startangle=180,  # 设置饼图的初始角度
           counterclock=False,  # 将饼图的顺序设置为顺时针方向
           title='不同类型饮料构成的饼图',  # 为饼图添加标题
           wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
           textprops={'fontsize': 10, 'color': 'black'})  # 设置文本标签的属性值
# 显示图形
plt.show()
