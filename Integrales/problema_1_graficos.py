from sympy import symbols, integrate, expand
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import plot
from sympy.utilities.lambdify import lambdify

# Definir la variable simbólica
x = symbols('x')

# Definir la integral original
integrand = x**3 * (x**4 - 1)**2

# Calcular la integral
result = integrate(integrand, x)

# Expandir el resultado para mejor visualización
expanded_result = expand(result)

# Verificar la integral derivando el resultado
derivative = sp.diff(result, x)
derivative_expanded = expand(derivative)

# Función para imprimir los resultados de manera legible
def print_results():
    print("Integral original:")
    print(f"∫ x³(x⁴ - 1)² dx")
    print("\nResultado:")
    print(f"∫ x³(x⁴ - 1)² dx = {expanded_result}")
    print("\nDerivada del resultado:")
    print(f"Derivada: {derivative_expanded}")

# Función para crear la visualización
def plot_functions():
    # Convertir expresiones simbólicas a funciones numéricas
    f_integrand = lambdify(x, integrand, 'numpy')
    f_result = lambdify(x, result, 'numpy')

    # Crear rango de valores x
    x_vals = np.linspace(-2, 2, 1000)

    # Calcular valores y
    y_integrand = f_integrand(x_vals)
    y_result = f_result(x_vals)

    # Crear la figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # Graficar la función original
    ax1.plot(x_vals, y_integrand, 'b-', label='Función Original')
    ax1.set_title('Función Original: x³(x⁴ - 1)²')
    ax1.grid(True)
    ax1.legend()
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    # Graficar la integral
    ax2.plot(x_vals, y_result, 'r-', label='Integral')
    ax2.set_title('Función Integral')
    ax2.grid(True)
    ax2.legend()
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')

    # Ajustar el diseño
    plt.tight_layout()
    plt.show()

# Imprimir resultados y mostrar gráficas
print_results()
plot_functions()

# Crear una visualización simbólica adicional usando SymPy
def plot_sympy():
    p1 = plot(integrand, (x, -2, 2), show=False, label='Función Original')
    p2 = plot(result, (x, -2, 2), show=False, label='Integral')
    p1.extend(p2)
    p1.show()

# Mostrar la visualización simbólica
plot_sympy()
