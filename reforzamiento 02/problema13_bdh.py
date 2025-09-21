#13. Crea un programa que convierta una temperatura en grados Celsius a
#Fahrenheit. La fórmula que tiene que tener en cuenta es la siguiente:
#F = (C * 9)/5 + 32
#Deberá imprimir algo como lo siguiente:
#La temperatura en °C: 30
#Temperatura en Fahrenheit: 86.00
#Realizarlo con dos distintos datos para la temperatura en Celsius (usar dos
#variables iniciales para obtener dos temperaturas finales en Fahrenheit)

celsius1 = 30
celsius2 = -36.5

fahr1 = (celsius1 * 9) / 5 + 32
fahr2 = (celsius2 * 9) / 5 + 32

print("La temperatura en °C: {}".format(celsius1))
print("Temperatura en Fahrenheit: {:.2f}".format(fahr1))

print("La temperatura en °C: {}".format(celsius2))
print("Temperatura en Fahrenheit: {:.2f}".format(fahr2))
