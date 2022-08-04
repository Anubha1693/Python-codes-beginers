from cProfile import label
from matplotlib import pyplot as plt

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
plt.plot(theta, intensity, label='Sample A')
plt.scatter(theta, intensity)
plt.xlabel(r"2$\theta$")
plt.ylabel("Intensity")
plt.title("XRD data plot")
plt.legend()
plt.grid()
plt.show()