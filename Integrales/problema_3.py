from sympy import symbols, integrate, expand

#crear variable simbolica para poder trabajar con integrales

x = symbols('x')

#Definicion de la integral
integral = (3*x +1)/(x*(x**2 + x - 6))
#calculo de la integral con la funcion integrate
resultado_integral = integrate(integral, x)

#Expandir el resultado para ser mas legible

resultado_expandido = expand(resultado_integral)

def imprimir_resultados():
     print(f"Resultado: {resultado_expandido}")

#imprimir resultados
imprimir_resultados()

