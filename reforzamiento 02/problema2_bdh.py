#2.Crea una variable tipo int. Luego, multiplica por 10 y restarle el valor de
#10. Debes hacer todo esto en dos pasos. Finalmente convertirlo a float y
#mostrar el resultado por pantalla y el tipo de variable también.
var1 = 7
var1 = var1 * 10
var1 = var1 - 10

resultado_float = float(var1)
print("Resultado: {}, tipo: {}".format(resultado_float, type(resultado_float).__name__))