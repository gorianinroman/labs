from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt


def line(b):
    return (((b - 17.65)/12.37)**2)
    


mm_40 = np.loadtxt("wave_40_mm.txt", dtype=complex)
mm_80 = np.loadtxt("wave_80_mm.txt", dtype=complex)
mm_120 = np.loadtxt("wave_120_mm.txt", dtype=complex)
x_120 = np.arange(1, 975, 1)
x_80 = np.arange(1, 1041, 1)
x_40 = np.arange(1, 1130, 1)
x_40 = x_40 * 15/ 1131
x_80 = x_80 * 15/ 1041
x_120 = x_120*15/976



i = 0
while i < 1129:
    mm_40[i] =  line(mm_40[i])
    i = i+1

while i < 1040: 
    mm_80[i] =  line(mm_80[i])
    i = i+1
    
while i < 974:
    mm_120[i] =  line(mm_120[i])
    i = i+1
plt.figure(figsize=(10, 5))
#plt.plot(x_40, mm_40)
#plt.plot(x_80, mm_80)
plt.plot(x_120, mm_120)
plt.xlabel(r'$Время, с$')
plt.ylabel(r'$Уровень воды, мм$')
#plt.savefig('120_mm.png')
plt.grid(True)


plt.show()



