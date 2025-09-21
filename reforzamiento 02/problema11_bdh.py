#11. Identificar qué tipo de dato se obtiene al elevar tu edad con
#exponente 5 y luego dividirlo por 10. Mostrar el resultado de su módulo con
#3 en pantalla

edad = 21
var1 = (edad ** 5) / 10
var2 = var1 % 3

print("Resultado: {}, tipo de dato: {}".format((var2), type(var2).__name__))