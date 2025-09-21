#3. Crear una variable tipo string, luego súmala con otra variable tipo int,
#para esto convertir una de las variables para realizar este procedimiento
#sin errores. Mostrar la suma en pantalla.

#Caso 1: Convertir var1: str a un entero (int)
var1 = "3"
var2 = 22
var3 = int(var1) + var2

print("Suma: {}".format(var3))

#Caso 2: Convertir var2: int a una cadena (str)
var1 = "3"
var2 = 22
var3 = var1 + str(var2)

print("Suma: {}".format(var3))