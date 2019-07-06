class Jugador():

    def __init__(self, name, puntos):
        self.name=name
        self.puntos=puntos

    def __str__(self):
        cadena=self.name + "-"
        if self.puntos<1000:
            cadena=cadena + " es principiante"
        else:
            cadena=cadena + " es experto"
        return cadena


#bloque principal

jugador1=Jugador("Willy", 400)
jugador2=Jugador("Toledo", 1200)

print(jugador1)
print(jugador2)