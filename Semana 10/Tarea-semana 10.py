# Programa para recorrer e imprimir una matriz de 3x3

# Declarar matriz de 3x3 con números enteros
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Recorrer la matriz con ciclos anidados
print("Valores de la matriz:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j])

# Recorrer la matriz con ciclo extendido
print("\nMatriz formateada por filas:")
for i in range(4):
    if i < 3:
        print(f"Fila {i}: {matriz[i]}")
    else:
        print(f"Total de filas: {i}")

