def get_int():
    try:
        num = int(input("Ingrese un número entero: "))

        return num
    except ValueError:
        print("Entrada inválida, por favor ingrese un número entero válido.")
        return get_int()


number = get_int()
print("El número ingresado es:", number)
