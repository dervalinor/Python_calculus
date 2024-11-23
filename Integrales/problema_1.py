from sympy import symbols, integrate, expand
import sympy as sp

# Definir la variable simbólica
#una variable simbólica es una variable que se puede manipular algebraicamente
#para operaciones como integracion, derivacion o operaciones algebraicas.

x = symbols('x')

# Definir la integral original
integrand = x**3 * (x**4 - 1)**2

# Calcular la integral
#usar la funcion integrate para realizar la integral
result = integrate(integrand, x)

# Expandir el resultado para mejor visualización
#reescribe el resultado para obtener un resultado mas legible
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

    print("Derivada del resultado")
    print(f"Derivada: {derivative_expanded}")

# Imprimir resultados
print_results()
