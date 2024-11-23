from sympy import symbols, integrate, expand
import sympy as sp

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


# Imprimir resultados
print_results()
