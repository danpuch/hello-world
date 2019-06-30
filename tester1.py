
def carga_datos():
    lenteros=[]
    for i in range(10):
        num1=int(input("añade numero: "))
        lenteros.append(num1)
    return lenteros

def cambio_lista(lenteros):
    lenteros2=lenteros[:5]
    return lenteros2

#bloque principal

lenteros=carga_datos()
print(lenteros)
lenteros2=cambio_lista(lenteros)
print(lenteros2)

