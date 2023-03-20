import re


def clean_string(string):
    lower = string.lower()
    new_string = re.sub(r"[^a-zA-Z0-9]\s", " ", lower)

    return new_string


def count_words(string):
    new_string = clean_string(string)
    mylist = new_string.split()
    dictionary = {}

    for word in mylist:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def view_frequency(recurrence):
    for key, value in recurrence.items():
        print(f'La palabra "{key}", esta {value} veces')


print('Este programa muestra la cantidad de veces que se encuentra cada palabra en un oración')

string_input = (input("Ingrese su oración: "))
frequency = count_words(string_input)
view_frequency(frequency)
