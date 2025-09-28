# Crea una función que al ingresar dos números por parámetro mostrará
# todos los cuadrados de los números que hay entre ellos (Usar la función una
# vez y mostrar el resultado por consola). Los números serán ingresados y
# solicitados al usuario.

def cuadrados_entre(a, b):
    for i in range(a, b + 1):
        print(i, "al cuadrado es", i**2)

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))

cuadrados_entre(n1, n2)
