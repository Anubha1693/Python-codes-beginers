import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)


x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})
print(res.x)

x = np.linspace(-1,1,100)


plt.plot(x, rosen(x))
plt.show()
