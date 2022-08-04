from cProfile import label
from matplotlib import pyplot as plt
import numpy as np
filename = 'xrd.CSV'

with open(filename,"r") as f:
    lines = f.readlines()
    theta = []
    intensity = []
    for line in lines[1:]:
        words = line.split(',')
        theta.append(float(words[1]))
        intensity.append(float(words[2]))

#print(theta, intensity)
print(len(theta),len(intensity))
baseline = np.zeros_like(intensity)
for i in range(400):
    baseline[i] = 0.4-0.01*theta[i] 
theta = np.array(theta)
intensity = np.array(intensity)
intensity = intensity / np.max(intensity)
plt.plot(theta, intensity-baseline, label='Sample A')
plt.scatter(theta, intensity-baseline)
plt.xlabel(r"2$\theta$")
plt.ylabel("Intensity")
plt.title("XRD data plot")
plt.legend()
plt.grid()
plt.show()