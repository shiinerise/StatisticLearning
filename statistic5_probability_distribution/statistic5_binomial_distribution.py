import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
# 设置正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# 重复实验的次数
num_trials = 60
x = np.arange(num_trials)
plt.plot(x, binom.pmf(x, num_trials, 0.2), 'o-', label='p=0.2')
plt.plot(x, binom.pmf(x, num_trials, 0.5), 'o-', label='p=0.5')
plt.plot(x, binom.pmf(x, num_trials, 0.7), 'o-', label='p=0.7')
plt.title('二项分布，p对结果的影响')
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#        ncol=1, mode="expand", borderaxespad=0.)
plt.show()