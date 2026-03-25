import numpy as np
import matplotlib.pyplot as plt

# Parameters
B = 1e8
gamma = 1 / np.sqrt(1 - 0.999**2)

# Cyclotron frequency (normalized)
omega_B = 1.0

# Frequency range
omega = np.logspace(-1, 6, 500)

# Cyclotron spectrum (discrete spikes)
cyclotron = np.zeros_like(omega)
harmonics = np.arange(1, 10)

for n in harmonics:
    cyclotron += np.exp(-(omega - n*omega_B)**2 / 0.01)

# Synchrotron spectrum
omega_c = gamma**3 * omega_B
synch = omega**(1/3) * np.exp(-omega / omega_c)

# Plot
plt.figure()
plt.loglog(omega, cyclotron, label='Cyclotron')
plt.loglog(omega, synch, label='Synchrotron')

plt.xlabel('Frequency (arb units)')
plt.ylabel('Power (arb units)')
plt.legend()
plt.title('Cyclotron vs Synchrotron Spectrum')
plt.show()
