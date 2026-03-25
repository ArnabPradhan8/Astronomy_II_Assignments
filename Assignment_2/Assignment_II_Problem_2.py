import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 1.0
q = 1.0

# Velocities
velocities = [0.1, 0.999]

theta = np.linspace(0, np.pi, 500)

def E_theta(beta, theta):
    return (1 - beta**2) / (1 - beta**2 * np.sin(theta)**2)**(3/2)

# Electric field
plt.figure()
for v in velocities:
    beta = v
    E = E_theta(beta, theta)
    plt.plot(theta, E, label=f'v={v}c')

plt.xlabel(r'$\theta$')
plt.ylabel('E (normalized)')
plt.legend()
plt.title('Angular Distribution of Electric Field')
plt.show()

# Magnetic field
plt.figure()
for v in velocities:
    beta = v
    E = E_theta(beta, theta)
    B = beta * E * np.sin(theta)
    plt.plot(theta, B, label=f'v={v}c')

plt.xlabel(r'$\theta$')
plt.ylabel('B (normalized)')
plt.legend()
plt.title('Magnetic Field Distribution')
plt.show()

# Bremsstrahlung spectrum (FIXED scaling)
h = 6.626e-27
k = 1.38e-16

nu = np.logspace(6, 20, 200)
T = 1e7

def spectrum(nu, gamma):
    return gamma**6 * np.exp(-h*nu/(k*T))

plt.figure()
for v in velocities:
    gamma = 1 / np.sqrt(1 - v**2)
    plt.loglog(nu, spectrum(nu, gamma), label=f'v={v}c')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Intensity (arb units)')
plt.legend()
plt.title('Bremsstrahlung Spectrum (γ⁶ scaling)')
plt.show()
