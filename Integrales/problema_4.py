from sympy import symbols, integrate, expand, sqrt, simplify

#crear variable simbolica para poder trabajar con integrales

x = symbols('x')

#Definicion de la integral
integral = (4 * x**2)/sqrt(529 - 4 * x**2)
#calculo de la integral con la funcion integrate
resultado_integral = integrate(integral, x)

#Expandir el resultado para ser mas legible

resultado_expandido = expand(resultado_integral)

#Resultado simplificado
resultado_simplificado = simplify(resultado_integral)

def imprimir_resultados():
     print(f"Resultado: {resultado_simplificado}")

#imprimir resultados
imprimir_resultados()
