def verificar_Par_impar(numero):
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"
    return resultado
print("verificardor de numeros")
mi_numero = int(input("Ingrese un numero: "))
respuesta = verificar_Par_impar(mi_numero)
print(f"El resultado es: {respuesta}")
