# Sistema de Reserva de Asientos en una Sala de Cine
# Matriz 3x4 (3 filas, 4 columnas)
# 0 = asiento libre
# 1 = asiento reservado

# Paso 1: Crear la matriz de 3x4 inicializada con 0 (todos los asientos libres)
asientos = [
    [0, 0, 0, 0],  # Fila 0
    [0, 0, 0, 0],  # Fila 1
    [0, 0, 0, 0]   # Fila 2
]

print("="*50)
print("   BIENVENIDO AL SISTEMA DE RESERVA DE ASIENTOS")
print("="*50)
print("\nSala de cine: 3 filas x 4 columnas (12 asientos)")
print("0 = Asiento libre")
print("1 = Asiento reservado\n")

# Paso 2: Mostrar la matriz inicial
print("Estado inicial de la sala:")
print("-" * 20)
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()  # Salto de línea después de cada fila

print("\n" + "="*50)

# Paso 3: Pedir al usuario que reserve asientos
while True:
    try:
        # Solicitar fila y columna
        fila = int(input("\nIngrese la fila del asiento (0-2): "))
        columna = int(input("Ingrese la columna del asiento (0-3): "))

        # Validar que los valores estén en el rango correcto
        if fila < 0 or fila > 2 or columna < 0 or columna > 3:
            print("❌ Error: La fila debe estar entre 0-2 y la columna entre 0-3")
            continue

        # Verificar si el asiento ya está reservado
        if asientos[fila][columna] == 1:
            print("❌ Error: Este asiento ya está reservado")
            continue

        # Marcar el asiento como reservado (1)
        asientos[fila][columna] = 1
        print(f"✓ Asiento [{fila}][{columna}] reservado exitosamente")

    except ValueError:
        print("❌ Error: Ingrese números válidos")
        continue

    # Mostrar la matriz actualizada
    print("\nEstado actual de la sala:")
    print("-" * 20)
    for i in range(3):
        for j in range(4):
            print(asientos[i][j], end=" ")
        print()  # Salto de línea después de cada fila
    print("="*50)

    # Preguntar si desea reservar otro asiento
    continuar = input("\n¿Desea reservar otro asiento? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar resumen final
print("\n" + "="*50)
print("           RESUMEN FINAL DE LA SALA")
print("="*50)

# Contar asientos libres y reservados
asientos_libres = 0
asientos_reservados = 0

for i in range(3):
    for j in range(4):
        if asientos[i][j] == 0:
            asientos_libres += 1
        else:
            asientos_reservados += 1

print("\nÚltimo estado de la sala:")
print("-" * 20)
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

print("\nEstadísticas:")
print(f"Total de asientos: 12")
print(f"Asientos libres: {asientos_libres}")
print(f"Asientos reservados: {asientos_reservados}")
print("="*50)
print("Gracias por usar nuestro sistema de reservas.")
print("="*50)

