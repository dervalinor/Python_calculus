from sympy import symbols, integrate

# Definir las variables simbólicas
x = symbols('x')

# Definir la función a integrar
integrand = x**3 + x - x**2

# Calcular la integral con límites
result = integrate(integrand, (x, 0, 3))

# Imprimir el resultado
print("Resultado de la integral:")
print(result)
