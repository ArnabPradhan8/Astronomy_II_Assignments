import numpy as np
import matplotlib.pyplot as plt

# Constants (cgs)
h = 6.626e-27
k = 1.38e-16
c = 3e10

# Parameters
r0 = 1.0
n = 1e10
gff = 1.0
T_floor = 1e-10  # small floor to avoid divergence

# Frequency range
nu_vals = np.logspace(6, 16, 50)

# Impact parameter grid
b_vals = np.linspace(0, r0, 50)

# Temperature profiles
def T1(r):
    return 1e4 * (r / r0)

def T2(r):
    return 1e6 * np.exp(-r / r0)

# Emissivity (fixed behavior at low T)
def j_nu(nu, T):
    if T < 1e-6:
        return 0.0
    return n**2 * T**(-0.5) * np.exp(-h*nu/(k*T)) * gff

# Absorption
def alpha_nu(nu, T):
    T = max(T, T_floor)
    return n**2 * T**(-1.5) * nu**(-2) * (1 - np.exp(-h*nu/(k*T))) * gff

# Radiative transfer
def compute_intensity(nu, T_func):
    I_b = []

    for b in b_vals:
        smax = np.sqrt(r0**2 - b**2)
        s_vals = np.linspace(-smax, smax, 200)

        tau = np.zeros_like(s_vals)
        integrand = np.zeros_like(s_vals)

        for i, s in enumerate(s_vals):
            r = np.sqrt(b**2 + s**2)
            T = T_func(r)

            j = j_nu(nu, T)

            tau[i] = np.trapz([
                alpha_nu(nu, T_func(np.sqrt(b**2 + sp**2)))
                for sp in s_vals[i:]
            ], s_vals[i:])

            integrand[i] = j * np.exp(-tau[i])

        I = np.trapz(integrand, s_vals)
        I_b.append(I)

    return np.array(I_b)

# Compute
for nu in [1e8, 1e12, 1e16]:
    I1 = compute_intensity(nu, T1)
    I2 = compute_intensity(nu, T2)

    plt.plot(b_vals, I1, label=fr'$T_1$, $\nu=${nu:.0e}')
    plt.plot(b_vals, I2, '--', label=fr'$T_2$, $\nu=${nu:.0e}')

plt.xlabel('Impact parameter b')
plt.ylabel(r'Intensity $I_\nu$')
plt.legend()
plt.show()