from matplotlib import pyplot as plt


x = [1,2,4,6,8,10,12,15,18]
y = [5,14,5,8,8,89,4,5,7]
print(len(x), len(y))

#plt.plot(x,y)
plt.scatter(x,y)
plt.show()