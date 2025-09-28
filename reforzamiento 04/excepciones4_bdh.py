# Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una
# excepción para el siguiente bloque de código y tu programa no se bloquee.
# Además, imprime un mensaje al usuario la causa y/o solución (Pedir
# nombre, día, mes, año por consola):
# Nombre: No debe recibir un dato numérico, sino decírselo al usuario Día, mes
# y año: No debe recibir un dato string, sino decírselo al usuario
#
# cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# # Hello Leonardo, hoy estamos 04 de agosto del 2025
#
# Independientemente del resultado, debe imprimir “Operación
# finalizada” al final
# - Usar try, except, finally
# Usar la función al menos 3 veces, incluyendo casos de error

def saluda_fecha(nombre, dia, mes, ano):
    try:
        if nombre.isdigit():
            raise ValueError("El nombre no debe ser numérico")
        if not dia.isdigit() or not ano.isdigit():
            raise TypeError("Día y año deben ser números")
        if mes.isdigit():
            raise TypeError("El mes debe ser un texto")

        print("Hello {}, hoy estamos {:02d} de {} del {}".format(nombre, int(dia), mes, ano))

    except (ValueError, TypeError) as e:
        print("Error:", e)

    finally:
        print("Operación finalizada")

saluda_fecha("Leonardo", "4", "agosto", "2025")
saluda_fecha("1234", "4", "agosto", "2025")
saluda_fecha("Lucía", "4", "08", "2025")