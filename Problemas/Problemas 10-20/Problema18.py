#Problema 18
#Descripcion Resolver ecuaciones cuadraticas
print ("Resolucion de ecuaciones cuadraticas")

import math
def EcuacionCuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        X1 = (-b + math.sqrt(discriminante)) / (2*a)
        X2 = (-b - math.sqrt(discriminante)) / (2*a)
        return X1, X2
    elif discriminante == 0:
        X = -b / (2*a)
        return X
    else:
        return "No tiene solucion real"
    
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    print(EcuacionCuadratica(a, b, c))

    print("Fin del programa")
