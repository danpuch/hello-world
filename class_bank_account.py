#hacer un programa como Banco

class Persona():

    def __init__(self):
        self.nombre=None
        self.edad=None
        self.dni=None
        self.savings=None

    def menu(self):
        sele=0
        while sele != 5:
            print("Welcome to the Bank Puchau")
            print()
            print("1. Open an account")
            print("2. Make a deposit")
            print("3. Make a withdraw")
            print("4. Print account")
            print("5. Exit")
            print()
            sele=int(input("Select: "))
            if sele ==1:
                self.open_account()
                print("Your request is done succesfully!")

            if sele==2:
                self.deposit()
                print("Your request is done succesfully!")

            if sele==3:
                self.withdraw()
                print("Your request is done succesfully!")

            if sele==4:
                self.imprimir()
                print("Your request is done succesfully!")

            if sele==5:
                self.salir()
                print("Your request is done succesfully!")
            else:
                sele=0
        exit()

    def open_account(self):
        print("Do you want to open an account. Follow the instructions: ")
        self.nombre=input("Your name: ")
        self.edad=int(input("Age: "))
        self.dni=int(input("Dni: "))
        self.savings=float(input("¿How much money?: "))

    def deposit(self):
        print("Do you want to add more money to your account. Follow the instructions: ")
        newsav=float(input("How much do you want to add?: "))
        self.savings=self.savings + newsav

    def withdraw(self):
        print("Do you want to extract money. Follow the instructions: ")
        newret=float(input("How much do you want to retire?: "))
        if newret > self.savings:
            print("You do not have enough money in your account. Please, do a deposit first or retire less money.")
        else:
            self.savings=self.savings-newret

    def imprimir(self):
        print("Do you want to actualize your account")
        print(self.nombre)
        print(self.edad)
        print(self.dni)
        print(self.savings)

    def salir(self):
        print("THanks for using Bank Puchau")


#bloque principal

customer1=Customer()
persona1=Persona()
persona1.menu()
