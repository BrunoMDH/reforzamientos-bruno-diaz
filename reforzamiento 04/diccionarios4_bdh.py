# Crear un diccionario con 6 departamentos del país.
# - Borrar cualquier departamento, usando la palabra reservada del.
# - Actualizar el penúltimo departamento por otro.
# - Comprobar que no existe este departamento borrado dentro del
# diccionario.
departamentos = {1: "Lima", 2: "Puno", 3: "Piura", 4: "Madre de Dios", 5: "Loreto", 6: "Amazonas"}

print("Diccionario inicial: {}".format(departamentos))

del departamentos[3]

print("Después de borrar Piura: {}".format(departamentos))

departamentos[5] = "La Libertad"

print("Después de actualizar penúltimo departamento: {}".format(departamentos))

print("¿Piura está en el diccionario?", "Piura" in departamentos.values())
