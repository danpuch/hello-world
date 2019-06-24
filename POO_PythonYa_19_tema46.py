'''Un banco tiene 3 clientes que pueden hacer depósitos y extracciones.
También el banco requiere que al final del día calcule la cantidad de dinero
que hay depositado.'''

class Cliente():

    def __init__(self):
        self.cliente={}

    def menu(self):
        print("***************************")
        print("Bienvenido al BANCO PUCHAU.")
        seleccion=0
        while seleccion != 5:
            print("1. Alta de cliente")
            print("2. Realizar un ingreso ")
            print("3. Realizar una retirada ")
            print("4. Consultar saldo actual ")
            print("5. salir")
            seleccion = int(input("Ingrese su selección: "))
            if seleccion == 1:
                self.alta_cliente()
            elif seleccion == 2:
                self.ingresar()
            elif seleccion == 3:
                self.retirar()
            elif seleccion == 4:
                self.consultar()
            elif seleccion == 5:
                self.salir()
            else:
                print("Por favor, selecciona una opción válida:")
                seleccion = 0

    def alta_cliente(self):
        print("****************************")
        nombre=input("Introduce tu nombre: ")
        monto=int(input("Primer ingreso: "))
        self.cliente[nombre]=monto

    def ingresar(self):
        print("****************************")
        nombre=input("Nombre del cliente: ")
        if nombre in self.cliente:
            monto=int(input("Cuanto quieres ingresar?: "))
            self.cliente[nombre]=self.cliente[nombre] + monto
            print("Tu saldo actual es", self.cliente[nombre])
        else:
            print("No se encuentra el cliente", nombre)
        print("****************************")

    def retirar(self):
        print("****************************")
        nombre=input("Nombre del cliente: ")
        if nombre in self.cliente:
            monto=int(input("Cuanto quieres retirar?: "))
            if self.cliente[nombre] - monto >=0:
                self.cliente[nombre]=self.cliente[nombre] - monto
                print("Tu saldo actual es", self.cliente[nombre])
            else:
                print("No dispones de tanto saldo para retirar")
        else:
            print("EL cliente no está dado de alta")

    def consultar(self):
        print("****************************")
        print("Impresión del estado del cliente")
        nombre=input("Nombre del cliente: ")
        if nombre in self.cliente:
            print(nombre, self.cliente[nombre])
        else:
            print("El cliente no está dado de alta")

    def salir(self):
        print("****************************")
        print("GRACIAS POR UTILIZAR LA APLICACIÓN DEL BANCO PUCHAU")
        print("****************************")
        exit()


#bloque principal

cliente1=Cliente()
cliente1.menu()




