class Empleado():

    def __init__(self):
        self.name=input("Nombre: ")
        self.salary=float(input("Salary: "))

    def imprimir(self):
        print("Name:",self.name,"Salary", self.salary)

    def paga_impuestos(self):
        if self.salary>3000:
            print("Paga impuestos")
        else:
            print("No paga impuestos")

#bloque principal

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

empleado2=Empleado()
empleado2.imprimir()
empleado2.paga_impuestos()