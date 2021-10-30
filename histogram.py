import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.title("Histogram")
plt.xlabel("random data")
plt.ylabel("frequency")
plt.hist(x,10)
plt.show()