#12. Escribe un programa que almacene información de un producto: Tu
#nombre, nombre del producto, precio unitario (float), cantidad (int) e
#imprimirá finalmente algo como lo siguiente:
#Buen día Nombre, el detalle de su compra es el siguiente:
#- Producto: Pollo a la brasa
#- Precio unitario: 50.50
#- Cantidad: 2
#- Total a pagar: 101

nombre = "Bruno Díaz"
producto = "Pollo a la brasa"
precio_unitario = 50.50
cantidad = 2
total = precio_unitario * cantidad

print("Buen día {}, el detalle de su compra es el siguiente:".format(nombre))
print("- Producto: {}".format(producto))
print("- Precio unitario: {:.2f}".format(precio_unitario))
print("- Cantidad: {}".format(cantidad))
print("- Total a pagar: {:.0f}".format(total))