# El Mínimo Común Múltiplo de dos números enteros positivos a y b es un valor c entero y positivo tal que
# al dividir c/a y c/b, el resto es 0, y además no existe otro número menor que c que cumpla esta condición.
# mcm(a,b) = (a / mcd(a,b)) * b

import math


def mcd(numberOne, numberTwo):
    maximum = max(numberOne, numberTwo)
    minimum = min(numberOne, numberTwo)
    while minimum != 0:
        res = minimum
        minimum = maximum % minimum
        maximum = res
    return maximum


def mcm(numberOne, numberTwo):
    maximum = max(numberOne, numberTwo)
    minimum = min(numberOne, numberTwo)
    return (maximum / mcd(maximum, minimum)) * minimum


print('Este programa cálcula el MCM entre dos números enteros positivos a y b')

firstNumber = int(input("Ingrese el primer número: "))
secondNumber = int(input("Ingrese el segundo número: "))

if firstNumber > 0 and secondNumber > 0:
    print(f'El M.C.M de {firstNumber} y {secondNumber} es: {mcm(firstNumber, secondNumber)}')
else:
    print('Por favor, ingrese números positivos.')
