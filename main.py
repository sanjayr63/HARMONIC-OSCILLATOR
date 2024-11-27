import numpy as np
import matplotlib.pyplot as plt

# Constants
x = np.linspace(-5, 5, 1000)  # Position range
hbar = 1.0  # Reduced Planck's constant
m = 1.0  # Mass of the particle
omega = 1.0  # Angular frequency of the oscillator


# Function to calculate the wavefunction
def psi_n(x, n):
    prefactor = np.sqrt(2.0 / (2 * n * np.emath.factorial(n))) * (m * omega / (np.pi * hbar)) * 0.25


    return prefactor * np.exp(-0.5 * m * omega * x ** 2 / hbar) *np.polynomial.hermite.hermval(np.sqrt(m * omega / hbar) * x, np.array([0] * n[1]))


# Function to calculate the probability density
def probability_density(psi):
    return np.abs(psi) ** 2


# Input quantum number 'n' from the user
n = int(input("Enter the quantum number 'n': "))
# Create the figure
plt.figure(figsize=(8, 6))
plt.title(f"Quantum Harmonic Oscillator (n = {n})")
plt.xlabel("Position (x)")
plt.ylabel("ψ(x) and |ψ(x)|^2")
# Calculate and plot the wavefunction
wavefunction = psi_n(x, n)
plt.plot(x, wavefunction, label=f'ψ{str(n)}(x)')
# Calculate and plot the probability density
prob_density = probability_density(wavefunction)
plt.plot(x, prob_density, label=f'|ψ{str(n)}(x)|^2', color='orange')
# Highlight the energy level
plt.axhline(0, color='k', linestyle='--', label=f'Energy Level {n + 0.5}ħω')
# Add legends
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()
