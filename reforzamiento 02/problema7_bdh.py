#7.De 3 números asignados mayores a 30 (entre positivos y negativos tú los
#propones) a 3 variables, se pide hallar la suma de los valores de los módulos
#con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma.

var1 = 37
var2 = 100
var3 = -32

mod_var1 = var1 % 3
mod_var2 = var2 % 5
mod_var3 = var3 % 7

suma_mod = mod_var1 + mod_var2 + mod_var3
print("Suma: {}".format(suma_mod))