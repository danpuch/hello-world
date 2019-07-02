class Operaciones():
    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

    def cargar1(self):
        self.valor1=int(input("Ingrese primer valor: "))
    def carga2(self):
        self.valor2=int(input("Ingrese segundo valor: "))
    def mostrar_resultado(self):
        print(self.resultado)
    def operar(self):
        pass


class Suma(Operaciones):
    def operar(self):
        self.resultado=self.valor1 + self.valor2

class Resta(Operaciones):
    def operar(self):
        self.resultado=self.valor1 - self.valor2

#bloque principal

suma1=Suma()
suma1.cargar1()
suma1.carga2()
suma1.operar()
print("La suma de valores es: ")
suma1.mostrar_resultado()