# Ingresar por consola 4 números mediante consola, crear un diccionario
# donde los ‘key’ serán los números indicados y los valores serán los cubos de
# las estos keys. Mostrar finalmente este diccionario.
numeros = []
for i in range(4):
    n = int(input(f"Número {i+1}: "))
    numeros.append(n)

diccionario = {num: num**3 for num in numeros}

print("Diccionario con números al cubo: {}".format(diccionario))
