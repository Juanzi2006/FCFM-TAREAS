#Problema 4
#Descripcion Generar la secuencia de Fibonacci hasta un numero dado de terminos.

print ("La secuencia de Fibonacci")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Ingresa el número de términos: "))
fibonacci(n)
print ("Fin de la secuencia de Fibonacci")