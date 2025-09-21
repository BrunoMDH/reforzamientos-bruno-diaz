# Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
# pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
# inicial en caso que no exista en la lista mostrar un mensaje donde indique
# que no se encuentre en la lista y luego esta será agregada a la lista.
# Finalmente mostrar la lista actualizada en consola.

estudiantes = ["Bruno", "Miguel", "Bryan", "Fernando", "José"]

nombre = input("Ingrese estudiante: ")

if nombre in estudiantes:
    estudiantes.remove(nombre)
    print("{} fue eliminado de la lista.".format(nombre))
else:
    estudiantes.append(nombre)
    print("{} no estaba en la lista, fue agregado.".format(nombre))

print("Lista actualizada: {}".format(estudiantes))
