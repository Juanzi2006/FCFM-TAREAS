#Problema 6
#Descripcion Calcular el interes compuesto dado un capital, tasa y tiempo.

print ("La economía")
def interes_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa / 100) ** tiempo
capital = float(input("Capital inicial: "))
tasa = float(input("Tasa de interés anual (%): "))
tiempo = int(input("Número de años: "))
print(f"Capital final: {interes_compuesto(capital, tasa, tiempo):.2f}")