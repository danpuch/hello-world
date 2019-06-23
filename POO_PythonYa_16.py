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
        self.nombre=[]
        self.telefono=[]
        self.mail=[]

    def menu(self):
        sele=0
        while sele != 5:
            print("1.Carga de un contacto en la agenda")
            print("2.Listado completo de la agenda")
            print("3.Consulta mediante nombre")
            print("4.Modifica telefono o email del contacto")
            print("5.Finaliza programa")
            sele=int(input("Selecciona opción: "))
            if sele ==1:
                self.carga()
            elif sele ==2:
                self.listado()
            elif sele==3:
                self.consulta()
            elif sele ==4:
                self.modifica()
            elif sele==5:
                self.finaliza()
            else:
                print("Intentelo de nuevo")
                sele=0

    def carga(self):
        print("Carga contactos en la agenda")
        name=input("Ingrese un nombre: ")
        telf=int(input("Telefono: "))
        mail=input("E-mail: ")
        self.nombre.append(name)
        self.telefono.append(telf)
        self.mail.append(mail)

    def listado(self):
        print("Listado completo de la agenda")
        for i in range(len(self.nombre)):
            print("Name: ", self.nombre[i], "/ Telephone:", self.telefono[i], "/ Email:", self.mail[i] )

    def consulta(self):
        print("Consulta de datos de contacto")
        cons=input("Ingrese el nombre a consultar:")
        for i in range(len(self.nombre)):
            if cons in self.nombre[i]:
                print("Name:", self.nombre[i],"/ Telephone:", self.telefono[i], "/ Email", self.mail[i])
            else:
                print("No se encuentra contacto")

    def modifica(self):
        print("Modifica los datos de un contacto")
        modi=input("Ingrese el contacto a modificar: ")
        for i in range(len(self.nombre)):
            if modi in self.nombre[i]:
                newtel=int(input("Ingrese el nuevo telefono: "))
                newmail=input("Ingrese el nuevo email: ")
                self.telefono[i]=newtel
                self.mail[i]=newmail
            else:
                print("El contacto no se encuentra")

    def finaliza(self):
        print("Gracias por utilizar la agenda")
        exit()

#bloque principal

contacto1=Agenda()
contacto1.menu()


