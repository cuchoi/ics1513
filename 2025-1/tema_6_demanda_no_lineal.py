# /// script
# dependencies = [
#     "numpy",
#     "matplotlib"
# ]
# ///

import numpy as np
import matplotlib.pyplot as plt

def demand_function(P, A, epsilon):
    """
    Demand function: Q_D(P) = A * P^(ε)
    
    Parameters:
    P: Price
    A: Positive constant
    ε: Elasticity parameter (positive)
    """
    return A * (P ** epsilon)

# Set parameters
A = 2  # Constant 
epsilon = -0.5  # Elasticity parameter (positive)

# Create price range
P = np.linspace(0.1, 5, 100)

# Calculate quantity demanded
Q_D = demand_function(P, A, epsilon)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(Q_D, P, 'b-', linewidth=2)
plt.title('Demand Function: $P(Q_D)$', fontsize=14)
plt.xlabel('Quantity Demanded $(Q_D)$', fontsize=12)
plt.ylabel('Price (P)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(6, 3, f'A = {A}\nε = {epsilon}', bbox=dict(facecolor='white', alpha=0.7))
plt.xlim(0, 10)
plt.ylim(0, 5)

plt.tight_layout()
plt.show()
