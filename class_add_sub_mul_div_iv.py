class Lista():

    def __init__(self, lista_enteros):
        self.lista_enteros=lista_enteros

    def imprimir(self):
        print(self.lista_enteros)

    def __add__(self, entero):
        nueva=[]
        for i in range(len(self.lista_enteros)):
            if self.lista_enteros[i]<40:
                nueva.append(self.lista_enteros[i] + entero)
            else:
                nueva.append(self.lista_enteros[i])
        return nueva

#bloque principal

operacion1=Lista([12,34,54,65,76,23,2])
operacion1.imprimir()
print(operacion1 + 10)