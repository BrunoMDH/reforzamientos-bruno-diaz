#9.Elevar una base al exponente de 6 (que estará dentro una variable), este
#número el cual su valor estará asignado a una variable y luego restar este
#mismo valor multiplicado por dos (usar pow o **). Mostrar el resultado final
#en pantalla.

var1 = 3
var2 = pow(var1, 6)
var3 = var2 - (var2 * 2)
print("Resultado final: {}".format(var3))