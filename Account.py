class Account:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance

    def get_titular(self):
        return self.titular

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        if balance < 0:
            print("Monto de apertura NO puede ser negativa.")
        else:
            self.balance = balance

    def show_data(self):
        print("=========================================================")
        print("Estado de cuenta")
        print(f'Titular: {self.get_titular()}')
        print(f'Saldo: {self.get_balance()}')

    def get_in(self, credit):
        if credit > 0:
            print(f'+++ Ingresaron: {credit}')
            self.balance += credit

    def take_out(self, credit):
        if credit > 0:
            print(f'--- Egresaron: {credit}')
            self.balance -= credit


print("Ingrese los datos del cliente")
name = input("Nombre: ")
opening_amount = float(input("Monto de apertura: "))

client_one = Account(name)
client_one.set_balance(opening_amount)
client_one.show_data()
if client_one.get_balance() > 0:
    client_one.get_in(500)
    client_one.show_data()
    client_one.take_out(200)
    client_one.show_data()
