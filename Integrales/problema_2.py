from sympy import symbols, integrate, expand
import sympy as sp

#crear variable simbolica para poder trabajar con integrales

z = symbols('z')

#Definicion de la integral
integral = 2*z/(z**2-2)

#calculo de la integral con la funcion integrate
resultado_integral = integrate(integral, z)

#Expandir el resultado para ser mas legible

resultado_expandido = expand(resultado_integral)

def imprimir_resultados():
    print(f"Resultado: {resultado_expandido}")

#imprimir resultados
imprimir_resultados()
