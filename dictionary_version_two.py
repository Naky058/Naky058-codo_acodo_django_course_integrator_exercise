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


def find_most_repeated_word(recurrence):
    major_key = list(recurrence.keys())[0]
    major_value = list(recurrence.values())[0]

    for key, value in recurrence.items():
        if value > major_value:
            major_key = key
            major_value = value

    print(f'La palabra "{major_key}", es la que más se repite en la oración. Ella está {major_value} veces')


print('Este programa muestra la palabra que más se repite en una oración')

string_input = (input("Ingrese su oración: "))
frequency = count_words(string_input)
find_most_repeated_word(frequency)
