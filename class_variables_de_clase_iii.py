class Clientes():

    lista_suspendidos=[]

    def __init__(self, code, name):
        self.code=code
        self.name=name

    def suspendemos(self):
        Clientes.lista_suspendidos.append(self.code)

    def cliente_suspendido(self):
        if self.code in Clientes.lista_suspendidos:
            print("Este cliente esta suspendido.")
        else:
            print("Cliente activo")
        print("__________________")

    def imprimir(self):
        print("Code: ", self.code)
        print("Name: ", self.name)
        self.cliente_suspendido()

#bloque principal

cliente1=Clientes(100, "Pedro")
cliente2=Clientes(200, "Ana")
cliente3=Clientes(300, "Juan")
cliente4=Clientes(400, "Sara")

cliente2.suspendemos()
cliente3.suspendemos()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Clientes.lista_suspendidos)