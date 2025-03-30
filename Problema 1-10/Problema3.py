#Problema 3
#Descripcion Calcular el factorial de un numero dado.

print("Calculadora de factorial")
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
num = int(input("Ingresa un número: "))
print(f"El factorial de {num} es {factorial(num)}")
print("Fin de la calculadora de factorial")