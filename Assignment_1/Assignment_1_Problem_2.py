import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# PARAMETERS
# -------------------------------------------------

R0 = 1
a0 = 1
alpha0 = 1
r1 = R0/2
r2 = R0/4

r = np.linspace(0.01, R0, 200)
theta = np.linspace(0, 2*np.pi, 200)

# -------------------------------------------------
# RADIAL DEPENDENCE : tau(r)
# -------------------------------------------------

# Case (a)
tau_a_r = (a0*np.pi/2)*(R0**2 - r**2)

# Case (b)
tau_b_r = a0*(R0*(r+R0)*np.exp(-r/R0) - 2*R0**2*np.exp(-1))
tau_b_r = 2*np.pi*tau_b_r

# Case (c)
tau_c_r = a0*(-R0**2/4 - (r**2/2)*np.log(r/R0) + r**2/4)
tau_c_r = 2*np.pi*tau_c_r


plt.figure(figsize=(6,4))

plt.plot(r, tau_a_r, label="Case (a)")
plt.plot(r, tau_b_r, label="Case (b)")
plt.plot(r, tau_c_r, label="Case (c)")

plt.xlabel("Radius r")
plt.ylabel("Optical Depth τ(r)")
plt.title("Radial Dependence of Optical Depth")

plt.legend()
plt.grid()

plt.show()


# CASE (a)

dtaudtheta_r1 = -(3/4)*alpha0*R0**2*np.cos(theta)*np.sin(theta)
dtaudtheta_r2 = -(15/16)*alpha0*R0**2*np.cos(theta)*np.sin(theta)

# CASE (b) and (c)

zero = np.zeros_like(theta)

plt.figure(figsize=(6,4))

plt.plot(theta, dtaudtheta_r1, label="Case (a), r=R0/2")
plt.plot(theta, dtaudtheta_r2, label="Case (a), r=R0/4")

plt.plot(theta, zero, '--', label="Case (b)")
plt.plot(theta, zero, ':', label="Case (c)")

plt.xlabel("Angle θ")
plt.ylabel("∂τ/∂θ")
plt.title("Angular Variation of Optical Depth")

plt.legend()
plt.grid()

plt.show()
