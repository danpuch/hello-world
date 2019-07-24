class Coche:

    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            return '** El coche esta en marcha'
        else:
            return '** El coche esta parado'

    def estado(self):
        print('El coche tiene ', self.__ruedas, ' ruedas, un ancho de ', self.__ancho_chasis, ' y un largo de ',
              self.__largo_chasis)

    def chequeo interno


micoche = Coche()
print(micoche.arrancar(True))
micoche.estado()

print('-------------segundo objeto---------------')

micoche2 = Coche()
print(micoche2.arrancar(False))
micoche2.estado()
