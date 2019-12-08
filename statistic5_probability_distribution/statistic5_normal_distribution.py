import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
mu, sigma = 0, 1
sampleNo = 1000
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo)
plt.hist(s, bins=100)
plt.show()