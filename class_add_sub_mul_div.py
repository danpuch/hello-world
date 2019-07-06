class Cliente():
    def __init__(self, name, monto):
        self.name=name
        self.monto=monto

    def __add__(self, other):
        e=self.monto + other.monto
        return e


cliente1=Cliente("Ana", 1200)
cliente2=Cliente("Luis", 1500)
cliente3=Cliente("Petra", 1500)
print("El total depositado por los tres clientes es")
print(cliente1 + cliente2)