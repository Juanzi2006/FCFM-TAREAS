#Problema 14
#Descripcion implementar distintos metodos de ordenamiento

print("Implementar distintos metodos de ordenamiento")
print("1. Bob")
print("2. Jordan")
print("3. Louis")
opcion = int(input("Seleccione una opcion:\n"))
if opcion == 1:
    def Bob (Lista):
        n = len(Lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if Lista[j] > Lista[j+1]:
                    Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
        return Lista
    Lista = [64, 34, 25, 12, 22, 11, 90] 
    print("Lista original:", Bob (Lista))

elif opcion == 2: 
    def Jordan (Lista):
        if len(Lista) <= 1:
            return Lista
        else:
            pivote = Lista[0]
            menores=[x for x in Lista[Lista.index(pivote)+1:]if x<=pivote]
            mayores = [x for x in Lista[Lista.index(pivote)+1:]if x > pivote]
            return Jordan(menores)+[pivote]+Jordan(mayores)
        Lista =[64,34,25,12,22,11,90]
        print("Lista original:", Lista)
        print("Lista ordenada:", Jordan(Lista))

elif opcion == 3:
    def Louis(Lista):
        if len(Lista) > 1:
            mitad = len(Lista)//2
            L = Lista[:mitad]
            R = Lista[mitad:]
            Louis(L)
            Louis(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    Lista[k] = L[i]
                    i += 1
                else:
                    Lista[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                Lista[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                Lista[k] = R[j]
                j += 1
                k += 1
        return Lista
    Lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:" , Lista)
    Louis(Lista)
    print("Lista ordenada:" , Lista)
else:
    print("opicion no valida")
    print("Fin del programa")
