#Problema 11
#Descripcion Verificar si una cadena es un palındromo
print ("Verificar si una cadena es un palindromo")
cadena = input ("Ingresar una cadena:\n")
if cadena == cadena[::-1]:
    print ("La cadena es un palindromo")
else:
  print("La cadena no es un palindromo")