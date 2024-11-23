from sympy import symbols, integrate, expand
import sympy as sp

# Definir la variable simbólica
x = symbols('x')

# Definir la integral original
integrand = x**3 * (x**4 - 1)**2

# Calcular la integral
result = integrate(integrand, x)


expanded_result = expand(result)

# Verificar la integral derivando el resultado
derivative = sp.diff(result, x)
derivative_expanded = expand(derivative)

# Función para imprimir los resultados de manera legible
def print_results():
    print("Integral original:")
    print(f"∫ x³(x⁴ - 1)² dx")

    print("\nResultado de la integración:")
    print(f"= {result}")

    print("\nResultado expandido:")
    print(f"= {expanded_result}")

# Ejecutar la verificación
print_results()

# Realizar la integración por sustitución manual (para verificar el método)
u = symbols('u')
# u = x⁴ - 1
# du = 4x³ dx
# x³ dx = du/4

substitution_integral = integrate(u**2/4, u)
print("\nResultado usando sustitución u = x⁴ - 1:")
print(f"= {substitution_integral}")
