import numpy as np
import matplotlib.pyplot as plt

# Constants (cgs)
h = 6.626e-27
k = 1.38e-16
c = 3e10

# Parameters
L = 1e17
T = 1e7
gff = 1.0

# Frequency range
nu = np.logspace(8, 18, 300)

# Densities
densities = [1e9, 1e12, 1e15, 1e18, 1e20]

# Planck function
def B_nu(nu, T):
    return (2*h*nu**3/c**2) / (np.exp(h*nu/(k*T)) - 1)

# Emissivity (scaled)
def j_nu(nu, n):
    return n**2 * T**(-0.5) * np.exp(-h*nu/(k*T)) * gff

# Absorption (scaled)
def alpha_nu(nu, n):
    return n**2 * T**(-1.5) * nu**(-2) * (1 - np.exp(-h*nu/(k*T))) * gff

# Plot intensity
plt.figure()

for n in densities:
    tau = alpha_nu(nu, n) * L
    I = B_nu(nu, T) * (1 - np.exp(-tau))
    plt.loglog(nu, I, label=f'n={n:.0e}')

# Blackbody
plt.loglog(nu, B_nu(nu, T), 'k--', label='Blackbody')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Intensity')
plt.legend()
plt.title('Bremsstrahlung Spectrum with Absorption')
plt.show()


# Relative difference
plt.figure()

for n in densities:
    tau = alpha_nu(nu, n) * L
    delta = np.exp(-tau)
    plt.loglog(nu, delta, label=f'n={n:.0e}')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Relative Difference')
plt.legend()
plt.title('Deviation from Blackbody')
plt.show()
