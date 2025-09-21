# Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
# este tamaño servirá para ingresar una cantidad X de nombres de alumnos.
# Ingresarás los nombres mediante consola también.
# Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la
# lista que fueron ingresados.

n = int(input("Número de alumnos: "))
alumnos = []

for i in range(n):
    nombre = input(f"Nombre del alumno {i+1}: ")
    alumnos.append(nombre)

print("Tamaño de la lista: {}".format(len(alumnos)))
print("Nombres: {}".format(alumnos))
