#Problema 12
#Descripcion Encontrar el mayor entre tres numeros dados.

print("Mayor de tres numeros")
a = int(input("ingresa el valor de la primera variable:\n"))
b = int(input("ingresa el valor de la primera variable:\n"))
c = int(input("ingresa el valor de la primera variable:\n"))
if a > b and a > c: 
    print("El mayor es: ",a)
elif b > a and b > c:
    print("El mayor es: ",b)
else:
    print("El mayor es: ",c)

    print("Fin del programa")