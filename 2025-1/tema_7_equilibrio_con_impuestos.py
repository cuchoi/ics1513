# /// script
# dependencies = [
#     "sympy",
#     "numpy",
#     "matplotlib",
#     "sympy"
# ]
# ///
import numpy as np
import sympy as sp
from sympy import symbols, Eq, solve, sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Definir funciones de oferta y demanda
def Q_s(p_s):
    return sqrt(10*p_s) - 1

def Q_d(p_d):
    return (100 - p_d) / p_d

# Valor del impuesto t = 5
t = 5

# Crear rango de precios para graficar
p_range = np.linspace(1, 30, 1000)

# Calcular cantidades correspondientes
q_s_values = [Q_s(p) if p > 0.1 else 0 for p in p_range]
q_d_values = [Q_d(p) if p > 0 else 0 for p in p_range]

# Calcular el equilibrio con impuesto
ps = sp.Symbol('ps', real=True, positive=True)
eq = sp.sqrt(10*ps) - 1 - (100-(ps+5))/(ps+5)
solutions = sp.solve(eq, ps)

# Mostrar todas las soluciones
print("Todas las soluciones encontradas:")
print(f"ps = {solutions}")

p_s_eq = solutions[0] # 6.9743
p_d_eq = p_s_eq + t
q_eq = Q_s(p_s_eq)

# Crear la figura
plt.figure(figsize=(10, 6))

# Graficar curvas de oferta y demanda
plt.plot(q_s_values, p_range, 'b-', label='Oferta (Q_s)', linewidth=2)
plt.plot(q_d_values, p_range, 'r-', label='Demanda (Q_d)', linewidth=2)


# Marcar puntos de equilibrio
plt.scatter([q_eq], [p_s_eq], color='blue', s=100, zorder=5)
plt.scatter([q_eq], [p_d_eq], color='red', s=100, zorder=5)

# Líneas de referencia
plt.axhline(y=p_s_eq, color='gray', linestyle='--', alpha=0.7)
plt.axhline(y=p_d_eq, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=q_eq, color='gray', linestyle='--', alpha=0.7)

# Área de impuesto
tax_rect = Rectangle((0, p_s_eq), q_eq, t, linewidth=1, 
                     edgecolor='black', facecolor='green', alpha=0.3)
plt.gca().add_patch(tax_rect)

# Anotaciones
plt.annotate(f'p_s = {p_s_eq:.2f}', xy=(q_eq+0.5, p_s_eq-0.5), fontsize=12)
plt.annotate(f'p_d = {p_d_eq:.2f}', xy=(q_eq+0.5, p_d_eq+0.5), fontsize=12)
plt.annotate(f'Q = {q_eq:.2f}', xy=(q_eq-2, 2), fontsize=12)
plt.annotate('Impuesto (t=5)', xy=(q_eq/2, p_s_eq+t/2), fontsize=12, 
             ha='center', va='center', color='darkgreen')

# Etiquetas y título
plt.xlabel('Cantidad (Q)', fontsize=14)
plt.ylabel('Precio (P)', fontsize=14)
plt.title('Equilibrio de Mercado con Impuesto', fontsize=16)
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Cálculo adicional para mostrar la incidencia del impuesto
print(f"Precio sin impuesto (equilibrio): {(p_s_eq + p_d_eq - t)/2:.4f}")
print(f"Precio que paga el vendedor: {p_s_eq:.4f}")
print(f"Precio que paga el comprador: {p_d_eq:.4f}")
print(f"Cantidad de equilibrio: {q_eq:.4f}")
print(f"Impuesto total recaudado: {t * q_eq:.4f}")
print(f"Carga del impuesto para el vendedor: {((p_s_eq + p_d_eq - t)/2 - p_s_eq):.4f} ({((p_s_eq + p_d_eq - t)/2 - p_s_eq)/t*100:.2f}%)")
print(f"Carga del impuesto para el comprador: {(p_d_eq - (p_s_eq + p_d_eq - t)/2):.4f} ({(p_d_eq - (p_s_eq + p_d_eq - t)/2)/t*100:.2f}%)")