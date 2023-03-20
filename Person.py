class Person:
    def __init__(self, name="", age=0, document_number=""):
        self.name = name
        self.age = age
        self.document_number = document_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print(f'Edad NO VALIDA')

    def get_document_number(self):
        return self.document_number

    def set_document_number(self, document_number):
        if len(document_number) != 8:
            print(f'DNI NO VALIDO')
        else:
            self.document_number = document_number

    def are_you_over_eighteen(self):
        if self.age >= 18:
            return True
        else:
            return False

    def show_data(self):
        print("--------------------------------------------------------")
        name_field = self.get_name()
        print(f'Nombre: {name_field}')

        document_number_field = self.get_document_number()
        if len(document_number_field) == 8:
            print(f'DNI: {document_number_field}')

        age_field = self.get_age()
        if age_field > 0:
            print(f'Edad: {age_field}')

            if self.are_you_over_eighteen():
                print(f'{name_field} ES mayor de edad.')
            else:
                print(f'{name_field} NO ES mayor de edad.')


print("Ingrese los datos de la Persona")
person_one_name = input("Nombre: ")
person_one_age = int(input("Edad: "))
person_one_document = input("DNI: ")

person_one = Person()
person_one.set_name(person_one_name)
person_one.set_age(person_one_age)
person_one.set_document_number(person_one_document)
person_one.show_data()
