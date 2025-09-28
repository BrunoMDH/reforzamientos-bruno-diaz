# Pedir al usuario que ingrese un nombre y apellidos el cual será usada
# por un parámetro para una función que se creará e indicará cuantas letras
# tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
# personas e indicar quien tiene el nombre con mayor número de caracteres
# (condicional)

def contar_letras(nombre_completo):
    nombre = nombre_completo.split()[0]
    return len(nombre)

persona1 = input("Ingresar nombre y apellidos de la primera persona: ")
persona2 = input("Ingresar nombre y apellidos de la segunda persona: ")

len1 = contar_letras(persona1)
len2 = contar_letras(persona2)

print("El nombre de {} tiene {} letras".format(persona1.split()[0], len1))
print("El nombre de {} tiene {} letras".format(persona2.split()[0], len2))

if len1 > len2:
    print("{} tiene más letras en su nombre".format(persona1.split()[0]))

if len2 > len1:
    print("{} tiene más letras en su nombre".format(persona2.split()[0]))

if len1 == len2:
    print("Ambos nombres tienen la misma cantidad de letras")
