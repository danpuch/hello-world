class Operaciones():

    def __init__(self):
        self.valor1=int(input("Primer valor: "))
        self.valor2=int(input("Segundo valor: "))

    def imprimir(self):
        self.suma()
        self.resta()
        self.multi()
        self.divi()

    def suma(self):
        sumamos=self.valor1 + self.valor2
        print("La suma es:", sumamos )

    def resta(self):
        restamos=self.valor1 - self.valor2
        print("La resta es: ", restamos)

    def multi(self):
        multiplicamos=self.valor1 * self.valor2
        print("La multiplicacion es: ", multiplicamos)

    def divi(self):
        dividimos=self.valor1 / self.valor2
        print("La division es: ", dividimos)

#bloque principal

operamos=Operaciones()
operamos.imprimir() 