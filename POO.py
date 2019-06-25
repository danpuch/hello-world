class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha=False

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos
        if (self.enmarcha==True):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas")
        print("Un ancho de", self.anchoChasis, "y largo de", self.largoChasis)

miCoche=Coche()

print("EL largo del coche es", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas, "ruedas")
print(miCoche.arrancar(True))
miCoche.estado()

print("**************** A continuación cremanos el segundo objeto ***********************")

mi2Coche =Coche()
print("EL largo del coche es", mi2Coche.largoChasis)
print("El coche tiene", mi2Coche.ruedas, "ruedas")
print(mi2Coche.arrancar(False))
mi2Coche.estado()




