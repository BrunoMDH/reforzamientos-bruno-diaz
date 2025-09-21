# Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
# finalmente muestra la suma y la media de los números ingresado insertados en
# la terminal

numeros = []

for i in range(10):
    valor = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(valor)

suma = sum(numeros)
media = suma / len(numeros)

print("Suma: {}".format(suma))
print("Media: {}".format(media))
