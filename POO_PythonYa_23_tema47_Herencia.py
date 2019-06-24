'''Plantear una clase Persona que contenga dos atributos: nombre y edad.
Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona
y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona
y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo
superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado.'''

class Persona():

    def __init__(self):
        self.name=input("Name: ")
        self.age=int(input("Age: "))

    def imprimir(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.salary=float(input("Your salary: "))

    def imprimir(self):
        super().imprimir()
        print("Salary: ", self.salary)

    def pay_taxes(self):
        if self.salary > 3000:
            print("You pay taxes!!!")
        else:
            print("You don't need to pay taxes!!")


#bloque principal

persona1=Persona()
persona1.imprimir()
print("**************")
employee1=Empleado()
employee1.imprimir()
employee1.pay_taxes()