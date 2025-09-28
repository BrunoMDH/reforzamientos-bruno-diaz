# Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
# el valor del salario y DNI en consola. También elimina el key edad de tu
# diccionario, incluyendo su valor. Mostrar finalmente el diccionario
# actualizado.
persona = {"nombre": "Bruno","edad": 21,"salario": 2500}

persona["dni"] = "12345678"

print("Salario: {}".format(persona["salario"]))
print("DNI: {}".format(persona["dni"]))

persona.pop("edad")

print("Diccionario actualizado: {}".format(persona))
