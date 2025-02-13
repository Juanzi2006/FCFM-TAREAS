#Problema 13 
#Descripcion Convertir una temperatura entre distintas escalas.

print("Convertir una temperatura entre distancias escalas")
temp= float(input("Ingresa la tempertura a convertir:\n"))
print("1.Celsius a Fahrenheit")
print("2.Celsius a Kelvin")
print("3.Fahrenheit a Celsius")
print("4.Fahrenheit a Kelvin")
print("5.Kelvin a Celsius")
print("6.Kelvin a Fahrenheit")
opcion = int(input("Seleccione una opcion:\n"))
if opcion == 1:
    print("La temperatura en Fahrenheit es: ",(temp*9/5)+32)
elif opcion == 2:
     print("La temperatura en Kelvin es ", temp+273.15)
elif  opcion == 3:
     print("La temperatura en Celsuis es:", (temp-32)*5/9)
elif opcion == 4:
     print("La temperatura en Kelvin es:", (temp-32)*5/9+273.15)
elif opcion == 5:
     print("La temperatura en Celsius es:", temp-273.15)
elif opcion == 6:
     print("La temperatura en Fahrenheit es:", (temp-273.15)*9/5+32)
else:
     print("Opcion no valida")
     print("Fin del programa")     