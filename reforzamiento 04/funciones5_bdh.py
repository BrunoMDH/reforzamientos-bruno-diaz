# Crear una función que aceptará por parámetro dos valores que serán
# ingresados por el usuario, una lista donde los valores serán llenados por el
# usuario también y un segundo parámetro que eliminará de la lista que fue
# ingresada a la función, finalmente el output de la función será la lista
# actualizada sin el valor que se sacará de la lista. Mostrar también la lista
# original y el número que fue eliminado.

def eliminar_valor(lista, valor):
    if valor in lista:
        lista.remove(valor)
    return lista

lista_original = []
cantidad = int(input("Indicar cantidad de elementos: "))
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    lista_original.append(num)

valor = int(input("Ingrese el número que desea eliminar de la lista: "))

print("Lista original:", lista_original)
print("Número a eliminar:", valor)

lista_actualizada = eliminar_valor(lista_original.copy(), valor)
print("Lista actualizada: {}".format(lista_actualizada))
