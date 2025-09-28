# Crear una función y dentro la respectiva excepción o excepciones para el
# siguiente bloque de código para que tu programa no se bloquee, ya que solo
# aceptará datos tipos entero y además imprimir un mensaje al usuario la causa
# y/o solución. También debe indicar el índice donde ingresarás este nuevo dato,
# si el índice está fuera de rango indicárselo al usuario:
# lista = [2, 6, 10, 4, 5, 23, 1]
# lista[10]: No es posible ingresar el dato, índice fuera de rango
# - Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
# - Usarás la función al menos 3 veces incluyendo un caso de error

lista = [2, 6, 10, 4, 5, 23, 1]

def insertar_dato(indice, valor):
    try:
        if not isinstance(valor, int):
            raise TypeError("Solo se permiten datos enteros.")

        lista[indice] = valor
        print("Dato {} ingresado en el índice {}".format(valor, indice))
        print("Lista actualizada: {}".format(lista))

    except IndexError:
        print("No es posible ingresar el dato, índice {} fuera de rango.".format(indice))

    except TypeError as e:
        print("Error:", e, "Por favor ingrese un número entero.")


insertar_dato(2, 43)
insertar_dato(10, 55)
insertar_dato(3, "bruno")
