import math
import numpy as np
import matplotlib.pyplot as plt


def line(b):
    return (-b/0.788571429)


   
    


mm_40 = np.loadtxt("test_40_mm.txt", dtype=float)
mm_80 = np.loadtxt("test_80_mm.txt", dtype=float)
mm_120 = np.loadtxt("test_120_mm.txt", dtype=float)
x_120 = np.arange(1, 609, 1)
x_80 = np.arange(1, 630, 1)
x_40 = np.arange(1, 716, 1)
x_40 = x_40 * 15/ 715
x_80 = x_80 * 15/ 629
x_120 = x_120*15/608



i = 0
while i < 715:
    mm_40[i] =  line(141.1333-mm_40[i])
    i = i+1

while i < 629:
    mm_80[i] =  line(141.1333-mm_80[i])
    i = i+1
while i < 608:
    mm_120[i] =  line(141.1333-mm_120[i])
    i = i+1
plt.plot(x_40, mm_40)
plt.plot(x_80, mm_80)
plt.plot(x_120, mm_120)


plt.show()



