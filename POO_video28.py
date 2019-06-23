'''POO video 28 el curso python youtube'''

class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if self.__enmarcha==True:
            chequeo=self.__chequeo_interno()

        if self.__enmarcha==True and chequeo ==True:
            return "El coche esta en marcha"
        elif self.__enmarcha==True and chequeo == False:
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis,
              "y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=='ok' and self.aceite=='ok' and self.puertas=='cerradas':
            return True
        else:
            return False


#crear primera instancia de clase
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()
print("******** A continuacion creamos el segundo objeto ********")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()