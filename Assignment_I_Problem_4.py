import numpy as np
import matplotlib.pyplot as plt

tau = np.linspace(0,5,200)

T = 1000
Tb0_1 = 100
Tb0_2 = 1e4

Tb1 = T + (Tb0_1 - T)*np.exp(-tau)
Tb2 = T + (Tb0_2 - T)*np.exp(-tau)

plt.plot(tau,Tb1,label="Initial Tb = 100 K")
plt.plot(tau,Tb2,label="Initial Tb = 10^4 K")

plt.xlabel("Optical Depth")
plt.ylabel("Brightness Temperature")
plt.legend()
plt.grid()
plt.show()
