class Lista():

    def __init__(self, entero):
        self.entero=entero

    def imprimir(self):
        print(self.entero)

    def __add__(self, entero):
        nueva=[]
        for i in range(len(self.entero)):
            nueva.append(self.entero[i] + entero)
        return nueva

#bloque principal

operacion1=Lista([12,34,23,55])
operacion1.imprimir()
print(operacion1 + 5)

