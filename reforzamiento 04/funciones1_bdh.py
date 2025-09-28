# Pedir dos números positivos mediante terminal al usuario. Mostrar
# como salida el número cuya sumatoria de dígitos es el mayor y los números
# cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
# sea conveniente.

def suma_digitos(numero):
    return sum(int(d) for d in str(numero))

n1 = int(input("Ingresar primer número positivo: "))
n2 = int(input("Ingresar segundo número positivo: "))

# Calcular sumas de dígitos
s1 = suma_digitos(n1)
s2 = suma_digitos(n2)

# Mostrar el número con mayor sumatoria de dígitos
if s1 >= s2:
    print("{} tiene la mayor sumatoria: {}".format(n1,s1))
else:
    print("{} tiene la mayor sumatoria: {}".format(n2,s2))

# Mostrar los números cuya sumatoria de dígitos es menor que 10
if s1 < 10:
    print(n1, "tiene sumatoria menor que 10")
if s2 < 10:
    print(n2, "tiene sumatoria menor que 10")
