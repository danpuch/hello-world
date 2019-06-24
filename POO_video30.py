'''Herencia- video 30 de curso youtube'''

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha
              ,"\nAcelerando:", self.acelera,"\nFrena:", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado == True:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha
          ,"\nAcelerando:", self.acelera,"\nFrena:", self.frena, "\n", self.hcaballito)

class Velectricos():

    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True


miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(Velectricos,Vehiculos):

    pass

miBici=BicicletaElectrica()
