import numpy as np
import matplotlib.pyplot as plt
# 设置正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# Poisson分布
x = np.random.poisson(lam=5, size=10000)  # lam为λ size为k
pillar = 15
a = plt.hist(x, bins=pillar, range=[0, pillar], color='g', alpha=0.5)
plt.title("泊松分布")
plt.plot(a[1][0:pillar], a[0], 'r')
plt.grid()
plt.show()