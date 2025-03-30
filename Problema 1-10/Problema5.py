#Problema 5
#Descripcion Verificar si un numero es primo.

print ("El verificador del primo")
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Ingresa un número: "))
print(f"{num} {'es' if es_primo(num) else 'no es'} primo")
print ("Fin del verificador del primo")