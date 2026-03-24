import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
I0 = 1.0       # initial intensity
S = 0.5        # source function
ratio = 0.2    # sigma_nu / alpha_nu

# absorption optical depth range
tau_abs = np.linspace(0,5,200)

# total optical depth (absorption + scattering)
tau_total = (1 + ratio) * tau_abs

# OBSERVED INTENSITY
# Case A : scattering + emission
I_A = S + (I0 - S) * np.exp(-tau_total)

# Case B : pure extinction (S = 0)
I_B = I0 * np.exp(-tau_total)

# PLOT 1 : Intensity vs Absorption Optical Depth
plt.figure(figsize=(6,4))

plt.plot(tau_abs, I_A, label="Case A: scattering + source")
plt.plot(tau_abs, I_B, label="Case B: S = 0")

plt.xlabel("Absorption Optical Depth (τ_abs)")
plt.ylabel(r"Observed Intensity $I_ν(0)$")
plt.title("Observed Intensity vs Absorption Optical Depth")

plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# PLOT 2 : Intensity vs Total Optical Depth
plt.figure(figsize=(6,4))

plt.plot(tau_total, I_A, label="Case A: scattering + source")
plt.plot(tau_total, I_B, label="Case B: S = 0")

plt.xlabel("Total Optical Depth (τ_total)")
plt.ylabel(r"Observed Intensity $I_ν(0)$")
plt.title("Observed Intensity vs Total Optical Depth")

plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# PLOT 3 : Relation Between τ_total and τ_abs
plt.figure(figsize=(6,4))

plt.plot(tau_abs, tau_total)

plt.xlabel("Absorption Optical Depth (τ_abs)")
plt.ylabel("Total Optical Depth (τ_total)")
plt.title("Increase of Optical Depth Due to Scattering")

plt.grid()

plt.tight_layout()
plt.show()
