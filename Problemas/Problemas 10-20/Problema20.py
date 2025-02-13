#Problema 20 
#Descripcion: Este programa implementa busqueda binaria y lineal
 #Busqueda linel: 

from random import randint 

listaP = list()
ListaN = list()
elementos = int(input("introduce la canridad de elementos: ") )

for count in range(-elementos,elementos):
    if count < 0: 
        ListaN.append(randint(-100,0))
    elif count > 0: 
            listaP.append(randint(1,100))
    else: 
            listaP.append (randint(0,1))

            """Sirve para sumar la listaP y listaN para obtener la lista completa """
            listacompleta = ListaN + listaP 

            print(listacompleta)

            ListaN.extend (listaP)

            print(ListaN)

num = int(input("introduzca un numero a buscar: "))

for itm in listacompleta: 
    if itm == num: 
      print("El numero se encontraba en la posicion ", listacompleta.index(itm))
      break 