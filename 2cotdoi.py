import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
division_average_marks = [68, 67, 77, 61, 70]
boys_average_marks = [72, 97, 69, 69, 66]
index = np.arange(5)
width = 0.30
plt.bar(index, division_average_marks, width, color="green", label="Division Marks")
plt.bar(index+width, boys_average_marks, width, color="blue", label="Boys Marks")
plt.title("Horizontally Bar graphs")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.xticks(index+ width/2, divisions)
plt.legend(loc='best')
plt.show()