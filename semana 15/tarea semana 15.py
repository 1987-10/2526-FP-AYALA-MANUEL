# Tarea: Gestión de productos en una tienda
# Estructura utilizada: Diccionario

def gestionar_tienda():

    inventario = {
        "Manzanas": 1.50,
        "Arroz": 0.80,
        "Leche": 1.10
    }

    # 2. Agregar datos
    print("--- Agregando un nuevo producto ---")
    inventario["Pan"] = 0.50

    # 3. Mostrar la información almacenada
    print("\nInventario actual:")
    for producto, precio in inventario.items():
        print(f"- {producto}: ${precio}")

    # 4. Operación básica: Buscar un elemento
    buscar = "Arroz"
    print(f"\n--- Buscando producto: {buscar} ---")
    if buscar in inventario:
        print(f"El precio de {buscar} es: ${inventario[buscar]}")
    else:
        print("Producto no encontrado.")

    # Operación básica: Eliminar un elemento
    print("\n--- Eliminando 'Leche' del inventario ---")
    if "Leche" in inventario:
        del inventario["Leche"]

    # Mostrar inventario final
    print("Inventario final optimizado:", inventario)


# Ejecutar el programa
if __name__ == "__main__":
    gestionar_tienda()