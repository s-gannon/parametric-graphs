import math
import matplotlib.pyplot as plt
import numpy as np

contRun = True
eq1, eq2 = "",""
fig, ax = plt.subplots()
while contRun:
    print()
    pts1, pts2 = [],[]
    interval = []
    if eq1 != "" and eq2 != "":
        if input("Keep last equations? (y/n):") == "n":
            eq1 = input("Enter equation f(z): ")
            eq2 = input("Enter equation g(z): ")
    else:
        eq1 = input("Enter equation f(z): ")
        eq2 = input("Enter equation g(z): ")
    interval.append(float(input("Enter start of interval: ")))
    interval.append(float(input("Enter end of interval: ")))
    precision = float(input("Enter in the precision: "))
    for i in np.arange(interval[0], interval[1], precision):
        pts1.append(eval(eq1.replace("z", str(i))))
        pts2.append(eval(eq2.replace("z", str(i))))
    ax.plot(pts1, pts2)
    ax.grid()
    plt.show()
    contRun = input("Continue? (y/n): ") == "y"
