# Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
# datos mediante consola también (5 compañías relacionadas con al mundo de TI)
# y harás una copia donde adrede agregarás nombres que estarán repetidos
# (mediante consola) para que finalmente muestres otra lista donde
# solo se mostrará los nombres no repetidos y también te mostrará la lista inicial

# Ingresar tamaño de la lista
n = int(input("Ingrese el tamaño de la lista: "))

# Ingresar compañías
companias = []
for i in range(n):
    nombre = input(f"Ingrese nombre de la compañía {i+1}: ")
    companias.append(nombre)

# Indicar número de repetidos
m = int(input("¿Cuántos nombres repetidos desea ingresar?: "))

# Crear copia y agregar repetidos
companias_repetidas = companias.copy()
for i in range(m):
    nombre = input(f"Ingrese el nombre repetido {i+1}: ")
    companias_repetidas.append(nombre)

# Lista solo con los que no se repiten
no_repetidos = []
for c in companias_repetidas:
    if companias_repetidas.count(c) == 1:
        no_repetidos.append(c)

print("Lista inicial: {}".format(companias))
print("Lista con repetidos: {}".format(companias_repetidas))
print("Lista final solo con los no repetidos: {}".format(no_repetidos))