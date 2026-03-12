import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
alpha0 = 1.0
R0 = 1.0
rho = 1.0
sigma_SB = 5.67e-8

# temperature range
T = np.linspace(300,1000,200)

# radius grid
r = np.linspace(0.1,2,500)

# Rosseland opacities
kappa_a = 1.2*alpha0*r**2
kappa_b = 1.2*alpha0*r
kappa_c = 1.2*alpha0*np.exp(-r/R0)

# assume constant temperature gradient
gradT = 1

# PLOT 1 : Flux vs Temperature
r_fixed = 0.5

kappaA = 1.2*alpha0*r_fixed**2
kappaB = 1.2*alpha0*r_fixed
kappaC = 1.2*alpha0*np.exp(-r_fixed/R0)

F_A = (16*sigma_SB*T**3)/(3*kappaA*rho)*gradT
F_B = (16*sigma_SB*T**3)/(3*kappaB*rho)*gradT
F_C = (16*sigma_SB*T**3)/(3*kappaC*rho)*gradT

plt.figure(figsize=(6,4))

plt.plot(T,F_A,'-',lw=2,label=r'$\kappa \propto r^2$')
plt.plot(T,F_B,'--',lw=2,label=r'$\kappa \propto r$')
plt.plot(T,F_C,'-.',lw=2,label=r'$\kappa \propto e^{-r/R_0}$')

plt.xlabel("Temperature (K)")
plt.ylabel("Radiative Flux")
plt.title("Radiative Flux vs Temperature")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# PLOT 2 : Flux vs Radius
T_fixed = 600

F_a_r = (16*sigma_SB*T_fixed**3)/(3*kappa_a*rho)*gradT
F_b_r = (16*sigma_SB*T_fixed**3)/(3*kappa_b*rho)*gradT
F_c_r = (16*sigma_SB*T_fixed**3)/(3*kappa_c*rho)*gradT

plt.figure(figsize=(6,4))

plt.plot(r,F_a_r,'-',lw=2,label=r'$\kappa \propto r^2$')
plt.plot(r,F_b_r,'--',lw=2,label=r'$\kappa \propto r$')
plt.plot(r,F_c_r,'-.',lw=2,label=r'$\kappa \propto e^{-r/R_0}$')

plt.xlabel("Radius r")
plt.ylabel("Radiative Flux")
plt.title("Radiative Flux vs Radius")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
