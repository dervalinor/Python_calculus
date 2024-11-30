from sympy import symbols, integrate, oo

# Definir las variables simbólicas
x = symbols('x')

# Definir la función a integrar
integrand = -4 / (5 * x - 2)**2

# Calcular la integral con límites
result = integrate(integrand, (x, 0, oo))

# Imprimir el resultado
print("Resultado de la integral:")
print(result)
