# Escribe un programa que reciba dos flotantes, luego estos
# pasarán a ser convertidos en enteros. Indique si el primero es
# múltiplo del segundo. Usar mod para la verificación si el residuo
# es 0

num1 = 3.22
num2 = 96.1

num1 = int(num1)
num2 = int(num2)

if num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}")
if num2 % num1 != 0:
    print(f"{num1} no es múltiplo de {num2}")
