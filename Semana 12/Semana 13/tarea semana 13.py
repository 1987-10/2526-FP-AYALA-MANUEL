def calcular_total(precio, cantidad):
    return precio * cantidad

if __name__ == "__main__":
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    total = calcular_total(precio, cantidad)
    print(f"El total de la compra es: {total}")
