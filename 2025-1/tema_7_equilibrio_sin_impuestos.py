# /// script
# dependencies = [
#     "numpy",
#     "matplotlib",
#     "sympy"
# ]
# ///

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, sqrt

# Define the supply and demand functions
def Q_s(p):
    return np.sqrt(10 * p) - 1

def Q_d(p):
    return (100 - p) / p

# Generate price values
p_values = np.linspace(1, 100, 500)  # Avoid division by zero
q_s_values = Q_s(p_values)
q_d_values = Q_d(p_values)

# Solve algebraically using sympy
p = symbols('p', real=True, positive=True)
equation = Eq(sqrt(10 * p) - 1, (100 - p) / p)
equilibrium_price_sympy = solve(equation, p)[0]
equilibrium_quantity_sympy = float(sqrt(10 * equilibrium_price_sympy) - 1)

# Plot the curves
plt.figure(figsize=(8, 6))
plt.plot(q_s_values, p_values, label=r'Curva de Oferta: $Q_S(p) = \sqrt{10p} - 1$', color='blue')
plt.plot(q_d_values, p_values, label=r'Curva de Demanda: $Q_D(p) = \frac{100 - p}{p}$', color='red')

# Mark equilibrium point
plt.scatter(equilibrium_quantity_sympy, equilibrium_price_sympy, color='green', zorder=5, label=f'Equilibrio (sympy): (p={equilibrium_price_sympy:.2f}, Q={equilibrium_quantity_sympy:.2f})')

plt.ylabel('Precio (p)')
plt.xlabel('Cantidad (Q)')
plt.title('Curvas de Oferta y Demanda')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.legend()
plt.grid()
plt.show()