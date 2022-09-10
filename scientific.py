from cProfile import label
from scipy.special import gamma, factorial
import numpy as np
x = np.linspace(-3.5, 5.5, 2251)
y = gamma(x)
import matplotlib.pyplot as plt
plt.plot(x, y, 'b', alpha=0.6, label='gamma(x)')
k = np.arange(1, 7)
plt.plot(k, factorial(k-1), 'k*', alpha=0.6,
         label='(x-1)!, x = 1, 2, ...')
plt.plot(x, np.exp(x), label='exponential')
plt.xlim(-3.5, 5.5)
plt.ylim(-10, 25)
plt.grid()
plt.xlabel('x')
plt.legend(loc='lower right')
plt.show()