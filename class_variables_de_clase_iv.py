class Jugador():

    tiempo=30

    def __init__(self, name, puntos):
        self.name=name
        self.puntos=puntos

    def pasar_tiempo(self):
        Jugador.tiempo-=1

    def imprimir(self):
        print("Nombre:", self.name)
        print("Puntos:", self.puntos)
        print("Fin de juego en", Jugador.tiempo, "minutos")



#bloque principal

jugador1=Jugador("Pedro", 100)
jugador2=Jugador("Ana", 50)
while Jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_tiempo()
