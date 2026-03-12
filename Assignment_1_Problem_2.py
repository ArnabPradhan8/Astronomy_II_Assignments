import numpy as np
import matplotlib.pyplot as plt

R0=1
a0=1

r=np.linspace(0.01,R0,200)

# case a
tau_a = (a0*np.pi/2)*(R0**2-r**2)

# case b
tau_b = a0*(R0*(r+R0)*np.exp(-r/R0)-2*R0**2*np.exp(-1))
tau_b = 2*np.pi*tau_b

# case c
tau_c = a0*(-R0**2/4 - (r**2/2)*np.log(r/R0) + r**2/4)
tau_c = 2*np.pi*tau_c

plt.plot(r,tau_a,label="case a")
plt.plot(r,tau_b,label="case b")
plt.plot(r,tau_c,label="case c")

plt.xlabel("r")
plt.ylabel("tau(r)")
plt.legend()
plt.show()
