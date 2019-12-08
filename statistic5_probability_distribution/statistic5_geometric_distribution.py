import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# 设置正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# n次实验，第k次才取得成功
k = 5
p = 0.6
X = np.arange(1, k+1, 1)
pList = stats.geom.pmf(X, p)
plt.plot(X, pList, marker='o', linestyle='None')
plt.vlines(X, 0, pList)
plt.xlabel("随机变量，第K次才成功")
plt.ylabel("概率")
plt.title("几何分布：p=%.2f"%p)
plt.show()