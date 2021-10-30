import matplotlib.pyplot as plt
import numpy as np

height = np.array([163,175,134,175,147,198,145,126,174,132])
weight = np.array([37,97,23,98,34,76,23,78,28,65])
plt.xlim(120,200)
plt.ylim(10,100)
plt.scatter(height,weight)
plt.title("Scatter plot")
plt.xlabel("Height")
plt.ylabel("Weight")
ax = plt.axes(projection='3d')
ax.scatter3D(height,weight)#có thể thay scatter=plot để chuyển sang dạng đường
ax.set_xlabel("Height")
ax.set_ylabel("weight")
plt.show()