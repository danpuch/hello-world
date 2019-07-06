class Familia():

    def __init__(self, padre, madre, hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        cadena=self.padre + "," + self.madre
        for h in self.hijos:
            cadena=cadena+","+ h
        return cadena

#bloque principal
familia1=Familia("Pedro", "Ana", ["Emilio", "Marcos"])
familia2=Familia("Jose", "Lucia", ["Bea"])
familia3=Familia("Andres", "Sara")

print(familia1)
print(familia2)
print(familia3)