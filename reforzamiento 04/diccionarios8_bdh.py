# Crear la agenda (diccionario vacío)
agenda = {}

cantidad = int(input("Indica número de contactos a registrar: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    telefono = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = telefono

print("Agenda:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

buscar = input("\nIngrese el nombre que desea buscar: ")

if buscar in agenda:
    print("{} está registrado con el número {}".format(buscar, agenda[buscar]))
else:
    print("No se encuentra registrado en la agenda")
