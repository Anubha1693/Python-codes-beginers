from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt


def calc_derivative(ypos, time):
    return -2 * ypos


time_vec = np.linspace(0, 4, 40)
y = odeint(calc_derivative, y0=1, t=time_vec)
print(y[:])
plt.scatter(time_vec,y)
plt.plot(time_vec, np.exp(-2*time_vec))
plt.show()

