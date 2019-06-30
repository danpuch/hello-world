class Coordenadas():

    def __init__(self):
        self.x=float(input("Coordenada X: "))
        self.y=float(input("Coordenada Y: "))

    def imprimir(self):

            if self.x > 0 and self.y > 0:
                print("Se encuentra en el primer cuadrante")
            elif self.x < 0 and self.y > 0:
                print("Se encuentra en el segundo cuadrante")
            elif self.x < 0 and self.y <0:
                print("Se encuentra en el tercer cuadrante")
            elif self.x > 0 and self.y < 0:
                print("Se encuentra en el cuarto cuadrante")
            else:
                print("Estas en el centro de la maya de coordenadas")


coordenadax=Coordenadas()
coordenadax.imprimir()