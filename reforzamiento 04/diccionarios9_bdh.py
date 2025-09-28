# Una empresa desea gestionar las facturas pendientes que tiene por pagar,
# para esto se creará un diccionario donde tendrá por key el número de factura
# “00054” y su value será el coste de la factura. El programa tendrá la opción
# de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
# que el área de contabilidad pague una factura se pedirá el número de factura
# que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
# ya está cancelada” caso contrario “El número de factura no existe”

facturas = {"00054": 1200.0}
print("Facturas iniciales:", facturas)

# Ingresar nueva factura
num = input("Ingrese número de factura: ")
costo = float(input("Ingrese costo de la factura: "))
facturas[num] = costo
print("Diccionario actualizado:", facturas)

# Pagar una factura
pagar = input("Ingrese número de factura a pagar: ")
if pagar in facturas:
    del facturas[pagar]
    print("La factura ya está cancelada")
else:
    print("El número de factura no existe")

print("Diccionario actualizado:", facturas)

