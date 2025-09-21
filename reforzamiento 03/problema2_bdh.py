# Crea un programa que calcule el Índice de Masa Corporal
# (IMC) de una persona.
# La fórmula es:

nombre = "Bruno Díaz"
peso = 70
estatura = 1.75

imc = peso / (estatura ** 2)

print("{}, tu IMC es: {:.2f}".format(nombre, imc))
