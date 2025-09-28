# Crear una función funciona_indice(persona, indice) y dentro la respectiva
# excepción para el siguiente bloque de código para que tu programa no se
# bloquee y además imprime un mensaje al usuario: “El índice “nombre_indice”
# ingresado no existe en el diccionario”, tipo de datos, etc que más pueden
# incurrir para este caso (los datos se pedirán por consola):
#
# persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
# persona['profesion'] #El índice en este caso no existe
#
# Usar la función al menos 2 veces incluyendo un caso de error

# Diccionario inicial
persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}

def funciona_indice(diccionario, indice):
    try:
        valor = diccionario[indice]
        print("El valor en '{}' es: {}".format(indice, valor))

    except KeyError:
        print("El índice '{}' ingresado no existe en el diccionario.".format(indice))

    except TypeError:
        print("Error: El índice debe ser una cadena de texto (str).")


indice1 = input("Ingrese un índice a consultar: ")
funciona_indice(persona, indice1)

indice2 = input("Ingrese otro índice a consultar: ")
funciona_indice(persona, indice2)
