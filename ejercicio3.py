# Inicializar una lista para almacenar las notas
notas = []


for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
    
    # Verificar que la nota esté en el rango válido
    while nota < 0 or nota > 10:
        print("Error: La nota debe estar entre 0 y 10.")
        nota = float(input(f"Ingrese la nota {i+1} nuevamente: "))
    
    notas.append(nota)

# Mostrar todas las notas
print("Notas obtenidas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

# Calcular la nota media
nota_media = sum(notas) / len(notas)

# Encontrar la nota más alta y la menor
nota_maxima = max(notas)
nota_minima = min(notas)

# Mostrar los resultados
print(f"Nota media: {nota_media:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")