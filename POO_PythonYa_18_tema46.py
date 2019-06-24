''' Confeccionar una clase que administre una agenda personal.
Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa. '''

class Agenda():

    def __init__(self):
        self.contactos={}

    def menu(self):
        print("*******************************")
        print("BIENVENIDO A LA AGENDA PERSONAL")
        seleccion=0
        while seleccion!=5:
            print("1. Carga de datos")
            print("2. Listado commpledo de Agenda")
            print("3. Consulta contacto intresando nombre")
            print("4. Modificar datos de contacto")
            print("5. Salir")
            seleccion=int(input("\nSelecciona opcion deseada: "))
            if seleccion == 1:
                self.cargar()
            elif seleccion == 2:
                self.imprimir()
            elif seleccion == 3:
                self.consultar()
            elif seleccion == 4:
                self.modificar()
            elif seleccion == 5:
                self.salir()
            else:
                print("Fuera de rango, vuelve a intentarlo")
                seleccion=0

    def cargar(self):
        print("*******************************")
        again='y'
        while again=='y':
            nombre=input("Nombre del contacto: ")
            telefono=int(input("Telefono: "))
            email=input("E-mail: ")
            self.contactos[nombre]=(telefono, email)
            again=input("Carga completada. \n¿Quieres cargar otro contacto? [y/n]:")
        print("*******************************")

    def imprimir(self):
        print("*******************************")
        print("Listado completo de la Agenda")
        for elemento in self.contactos:
            print("Nombre:",elemento, "/ Telefono:", self.contactos[elemento][0],
                  "/ E-mail:", self.contactos[elemento][1])
        print("*******************************")

    def consultar(self):
        print("*******************************")
        print("Consultar datos de un contacto")
        again='y'
        while again=='y':
            nombre=input("Nombre a consultar:")
            if nombre in self.contactos:
                print(nombre, "Telefono:", self.contactos[nombre][0], "/ E-mail:", self.contactos[nombre][1])
                again=input("Quieres consultar otro contacto? [y/n]:")
            else:
                print("No se encuentra el contacto")
                again=input("Quieres consultar otro contacto? [y/n]:")
        print("*******************************")

    def modificar(self):
        print("*******************************")
        print("Modificar un contacto")
        again='y'
        while again=='y':
            nombre=input("Ingrese el contacto a modificar: ")
            if nombre in self.contactos:
                telef=int(input("Introduzca nuevo telefono: "))
                email=input("Introduzca nuevo e-mail: ")
                self.contactos[nombre]=(telef, email)
                again=input("Quieres modificar otro contacto? [y/n]:")
            else:
                print("El contacto no se encuentra en la base de datos.")
                again=input("Quieres modificar otro contacto? [y/n]:")
        print("*******************************")

    def salir(self):
        print("*******************************")
        print("GRACIAS POR UTILIZAR AGENDA PERSONAL")
        print("*******************************")
        exit()


#bloque principal

contacto1=Agenda()
contacto1.menu()
