import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# PARAMETERS
R0 = 1.0          # system radius
I0 = 1.0          # boundary intensity
j0 = 1.0          # emission constant
alpha0 = 1.0      # absorption constant

theta = np.linspace(0, 2*np.pi, 200)
r = np.linspace(0.01, R0, 200)

# CASE (a)
# j_nu = j0 cos^2(theta) / r
# alpha_nu = alpha0 r cos^2(theta)

def alpha_a(r, th):
    return alpha0 * r * np.cos(th)**2

def j_a(r, th):
    return j0 * np.cos(th)**2 / r

def tau_a(r, th):
    return alpha0 * np.cos(th)**2 * (R0**2 - r**2) / 2

def intensity_a(th):

    integral, _ = quad(
        lambda rp: j_a(rp, th) *
        np.exp(-alpha0*np.cos(th)**2*(R0**2-rp**2)/2),
        0.01, R0
    )

    return I0*np.exp(-tau_a(0, th)) + integral


I_a = [intensity_a(th) for th in theta]

# CASE (b)
# j_nu = j0 cos(theta) sin(theta)
# alpha_nu = alpha0 r exp(-r/R0)

def alpha_b(r):
    return alpha0 * r * np.exp(-r/R0)

def tau_b(r):

    return alpha0*(R0*(r+R0)*np.exp(-r/R0) - 2*R0**2*np.exp(-1))

def j_b(th):
    return j0*np.cos(th)*np.sin(th)

def intensity_b(th):

    integral, _ = quad(
        lambda rp: j_b(th)*np.exp(-tau_b(rp)),
        0.01, R0
    )

    return I0*np.exp(-tau_b(0)) + integral


I_b = [intensity_b(th) for th in theta]

# CASE (c)
# j_nu = j0 r
# alpha_nu = alpha0 r ln(r/R0)

def alpha_c(r):
    return alpha0*r*np.log(r/R0)

def tau_c(r):

    r_safe = np.maximum(r,1e-5)

    return alpha0*(-R0**2/4 - (r_safe**2/2)*np.log(r_safe/R0) + r_safe**2/4)

def intensity_c():

    integral, _ = quad(
        lambda rp: j0*rp*np.exp(-tau_c(rp)),
        0.01, R0
    )

    return I0*np.exp(-tau_c(0)) + integral


I_c = intensity_c()
I_c = np.ones_like(theta)*I_c

# PLOT 1
# Observed intensity vs angle

plt.figure(figsize=(6,4))

plt.plot(theta, I_a, label="Case A")
plt.plot(theta, I_b, label="Case B")
plt.plot(theta, I_c, label="Case C")

plt.xlabel("Angle θ")
plt.ylabel(r"Observed Intensity $I_ν$(0,θ)")
plt.title("Observed Intensity at Center")

plt.legend()
plt.grid()

plt.show()

# PLOT 2
# Optical depth vs radius

tauA = alpha0*(R0**2 - r**2)/2
tauB = tau_b(r)
tauC = tau_c(r)

plt.figure(figsize=(6,4))

plt.plot(r, tauA, label="Case A")
plt.plot(r, tauB, label="Case B")
plt.plot(r, tauC, label="Case C")

plt.xlabel("Radius r")
plt.ylabel("Optical Depth τ")
plt.title("Optical Depth vs Radius")

plt.legend()
plt.grid()

plt.show()

# PLOT 3
# Emission and absorption profiles

plt.figure(figsize=(6,4))

plt.plot(r, alpha0*r**2, label="Case A absorption")
plt.plot(r, alpha0*r*np.exp(-r/R0), label="Case B absorption")
plt.plot(r, alpha0*r*np.log(r/R0), label="Case C absorption")

plt.xlabel("Radius r")
plt.ylabel("Absorption coefficient")
plt.title("Absorption Profiles")

plt.legend()
plt.grid()

plt.show()
