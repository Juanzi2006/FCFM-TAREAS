#Problema 8
#Descripcion Calcular el area y la circunferencia de un circulo.
print ("Área circular")
pi = 3.1416  # Valor de pi aproximado
radio = float(input("Ingresa el radio del círculo: "))
area = pi * radio ** 2  # Fórmula del área de un círculo
circunferencia = 2 * pi * radio  # Fórmula de la circunferencia
print(f"Área: {area:.2f}, Circunferencia: {circunferencia:.2f}")
print("Fin de los calculos del área y circunferencia de un círculo")