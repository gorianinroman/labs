from math import log
import matplotlib.pyplot as plt
import numpy as np

#139 см
t_40 = 82/1129*15
t_80 = 56/1140*15
t_120 = 42/974*15
x = [log(60),log(140),log(160)]
y = [log(139/t_40), log(139/t_80), log(139/t_120)]
plt.figure(figsize=(10, 5))
x = np.arange(1, 10, 0.1)
y = 0.507*x + 2.76
plt.plot(x, y)
plt.grid(True)
plt.plot(4.1,4.85,'ro') 
plt.plot(4.94, 5.24,'ro') 
plt.plot(5.08, 5.37,'ro') 
plt.xlabel(r'$log(h)$')
plt.ylabel(r'$log(c)$')
plt.savefig('end.png')
plt.show()