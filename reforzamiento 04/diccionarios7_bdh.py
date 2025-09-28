# Realizar un programa donde se ingresarán por consola los nombres de los
# alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y
# las notas de c/u. Guardarás la información en un diccionario donde las claves
# serán los nombres de c/u de estos alumnos y sus valores serán las notas de
# esto alumnos.
# Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
# “Pedro tiene la nota de 15” y también la media de todas las notas.

cantidad = int(input("Indica la cantidad de personas en el diccionario: "))

notas = {}

for i in range(cantidad):
    nombre = input(f"Nombre del alumno {i+1}: ")
    nota = float(input(f"Nota de {nombre}: "))
    notas[nombre] = nota

print("Notas de los alumnos:")
for alumno, nota in notas.items():
    print("{} tiene la nota de {}".format(alumno, nota))


media = sum(notas.values()) / len(notas)
print("Media de todas las notas: {:.2f}".format(media))
