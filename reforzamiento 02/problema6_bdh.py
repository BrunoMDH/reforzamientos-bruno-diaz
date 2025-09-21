#6. Calcular la media de 5 datos (floats), cada dato debe estar en una variable
#y la media también. Mostrar el resultado en pantalla y el tipo de dato
#también mostrarlo.

var1 = 3.2
var2 = 4.3
var3 = 5.4
var4 = 6.5
var5 = 7.6
media = (var1 + var2 + var3 + var4 + var5) / 5

print("Media: {}, tipo: {}".format(media, type(media).__name__))