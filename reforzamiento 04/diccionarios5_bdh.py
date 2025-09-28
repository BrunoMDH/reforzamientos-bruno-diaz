# Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
# diccionario.
# - Mostrar en consola los valores de tu carrera y nombre agregándolos a
# una variable c/u
persona = {"nombre": "Bruno","salario": 2500,"dni": "75349971"}

persona["carrera"] = "Biología"

mi_nombre = persona["nombre"]
mi_carrera = persona["carrera"]

# Mostrar en consola
print("Nombre: {}".format(mi_nombre))
print("Carrera: {}".format(mi_carrera))
