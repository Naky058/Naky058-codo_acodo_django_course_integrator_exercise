def get_int():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))

            return num
        except ValueError:
            print("Entrada inválida, por favor ingrese un número entero válido.")


number = get_int()
print("El número ingresado es:", number)
