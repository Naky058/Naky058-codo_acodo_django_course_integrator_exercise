class Account:
    def __init__(self, titular, age=0, balance=0):
        self.titular = titular
        self.balance = balance
        self.age = age

    def get_titular(self):
        return self.titular

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print(f'Edad NO VALIDA')

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        if balance < 0:
            print("Monto de apertura NO puede ser negativa.")
        else:
            self.balance = balance

    def show_data(self):
        print("Estado de cuenta")
        print(f'Titular: {self.get_titular()}')
        print(f'Saldo: {self.get_balance()}')

    def are_you_over_eighteen(self):
        if self.age >= 18:
            return True
        else:
            return False

    def get_in(self, credit):
        if credit > 0:
            print(f'+++ Ingresaron: {credit}')
            self.balance += credit

    def take_out(self, credit):
        if credit > 0:
            print(f'--- Egresaron: {credit}')
            self.balance -= credit


class YoungAccount(Account):
    def __init__(self, titular, balance=0, bonus=0, age=0):
        super().__init__(titular, balance)
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, bonus):
        self.bonus = bonus

    def is_validate_titular(self):
        return super().are_you_over_eighteen() and super().get_age() < 25

    def take_out(self, credit):
        if self.is_validate_titular():
            super().take_out(credit)
        else:
            print("El titular de la cuenta no es válido para realizar un retiro.")

    def show_data(self):
        print("=========================================================")
        print("Cuenta Joven")
        super().show_data()
        print("Bonificación:", self.bonus, "%")


print("Ingrese los datos del cliente")
name_input = input("Nombre: ")
age_input = int(input("Edad: "))
opening_amount_input = float(input("Monto de apertura: "))
bonus_input = float(input("Bonificación: "))

client_one = YoungAccount(name_input)
client_one.set_age(age_input)
client_one.set_balance(opening_amount_input)
client_one.set_bonus(bonus_input)
client_one.show_data()
client_one.take_out(500)
client_one.show_data()
