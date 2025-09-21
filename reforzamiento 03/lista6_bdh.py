# Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
# de llegada:
# guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
# Se requiere reorganizar esta lista.
# Primero los que tienen número impar y en el orden que fueron llegando
# Segundo las personas que tienen número par de letras
# Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
# Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]

guests = ["Ana", "Pedro", "Raúl", "Fiorella", "Katherine", "Miguel", "Luis"]

# Separar por impar y par de letras
lista_impar = [g for g in guests if len(g) % 2 == 1]
lista_par = [g for g in guests if len(g) % 2 == 0]

# Reorganizar: primero impar, luego par
resultado = lista_impar + lista_par
print(resultado)


