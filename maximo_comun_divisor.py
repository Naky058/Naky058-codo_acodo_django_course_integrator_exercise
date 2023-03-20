# EL ALGORITMO DE EUCLIDES
# Los divisores comunes de dos números naturales a y b, con a > b y b != 0 , son los divisores
# del último resto no nulo, de las sucesivas divisiones entre a y b, y los restos.

import math


def mcd(max, min):
    while min != 0:
        res = min
        min = max % min
        max = res
    return max


print('Este programa cálcula el MCD entre dos números a y b , con a > b y b != 0')

firstNumber = int(input("Ingrese el primer número: "))
secondNumber = int(input("Ingrese el segundo número: "))

if secondNumber > 0:
    maximum = max(firstNumber, secondNumber)
    minimum = min(firstNumber, secondNumber)

    print(f'El M.C.D de {firstNumber} y {secondNumber} es: {mcd(firstNumber, secondNumber)}')
else:
    print('Por favor, el menor de los números debe ser mayor a cero')
