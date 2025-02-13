#Problema 16
#Descripcion Contar el Numero de vocales y consonantes en una cadena

print("Contar el numero de vocales y consonantes en una cadena")

print("Ingrese una cadena")
cadena = input()
Vocales = 0
Consonantes = 0
for i in cadena:
    if i in "aeiouAEIOU": Vocales += 1 

    elif i in "bcdefghijklmnñopqrstuvwxyzBCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        Consonantes += 1
        print("El numero de vocales es", Vocales)
        print("El numero de consonantes es", Consonantes)

        print("Fin del programa")