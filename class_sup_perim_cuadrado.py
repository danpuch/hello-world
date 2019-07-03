class Cuadrado():

    def __init__(self):
        self.lado=int(input("Introduce valor del lado: "))

    def imprimir(self):
        self.superficie()
        self.perimetro()

    def superficie(self):
        superficie=self.lado*self.lado
        print("Su superficie es: ", superficie)

    def perimetro(self):
        perimetro=self.lado*4
        print("Su perimetro es: ", perimetro)


#bloque principal:
cuadrado1=Cuadrado()
cuadrado1.imprimir() 