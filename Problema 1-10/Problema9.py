#Problema 9
#Descripcion Generar una lista de numeros pares e impares hasta un limite dado.
print ("Lista")
limite = int(input("Ingresa el límite: "))
pares = [i for i in range(limite + 1) if i % 2 == 0]
impares = [i for i in range(limite + 1) if i % 2 != 0]
print("Números pares:", pares)
print("Números impares:", impares)
print("Fin de la lista")