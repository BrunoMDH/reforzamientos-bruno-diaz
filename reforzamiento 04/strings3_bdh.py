# Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está
# dentro de la oración sin importar si está en mayúsculas o minúsculas.
# En caso que aparezca, indica la posición del primer carácter en donde
# empieza
# Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
# Output: “Python aparece en la posición 0”
# Métodos útiles: lower() y find()


frase = "Python y sus enormes ventajas"
palabra = "Python"

posicion = frase.lower().find(palabra.lower())

if posicion != -1:
    print('"{}" aparece en la posición {}'.format(palabra, posicion))
else:
    print('"{}" no aparece en la frase'.format(palabra))
