# Crear un programa en Python donde tendrás una lista con 6 departamentos,
# el programa te pedirá ingresar 2 departamentos el cual el segundo
# departamento que ingreses sustituirá al primero de la lista.

departamentos = ["Lima", "Piura", "Amazonas", "Madre de Dios", "Ica", "Junín"]

dep1 = input("Departamento a reemplazar: ")
dep2 = input("Nuevo departamento: ")

if dep1 in departamentos:
    pos = departamentos.index(dep1)
    departamentos[pos] = dep2
else:
    print("El departamento no está en la lista.")

print("Lista actualizada: {}".format(departamentos))
