import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D"]
divisions_average_marks = [10, 70, 80, 56]

plt.bar(divisions, divisions_average_marks, color='blue')
plt.title("Bar Graph")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()