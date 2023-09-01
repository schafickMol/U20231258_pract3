# Definir la tupla de meses
meses_del_anio = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
)

# Solicitar al usuario un número entre 1 y 12
numeroMes = int(input("Ingrese un número entre 1 y 12: "))


if numeroMes >= 1 and numeroMes <= 12:
    
    nombre_mes = meses_del_anio[numeroMes - 1]
    print(f"Ese numero corresponde al mes de  {numeroMes} es {nombre_mes}.")
else:
    print("Error: Numero no valido.")