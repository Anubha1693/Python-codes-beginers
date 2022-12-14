from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 100000  # number of steps to take

gravity = 9.8
length = 100


state = np.zeros([2])

state[0] = 0
state[1] = 1

time = np.linspace(0, 500, N)


def pendulum(state, time):

    # Differential equation for an undamped pendulum.
    # state[0] should be angular position, state[1]
    # should be angular velocity.

    g0 = state[1]
    g1 = - gravity / length * state[0] - 0.1 * state[1] + 10 * np.sin(2*time)
    return np.array([g0, g1])


answer = odeint(pendulum, state, time)

fig, ax = plt.subplots()  # Create a figure and an axes.
#ax.plot(time, answer[:, 0], label="")  # Plot some data on the axes.
#ax.plot(time, answer[:, 0], label="Phase Space")  # Plot some data on the axes.

ax.set_xlabel("Angle")  # Add an x-label to the axes.
ax.set_ylabel("Anglular Frequency")  # Add a y-label to the axes.
ax.set_title(
    "Simple Pendulum with gravity variation linearly with time"
)  # Add a title to the axes.
ax.legend()  # Add a legend.
#plt.show()
plt.plot(answer[:,0], answer[:, 1], label="Phase Space")  # Plot some data on the axes.
plt.show()
