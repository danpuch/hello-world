
def carga_datos(numero):
    sumando=0
    for i in range(1,numero,4):
        sumando=+numero*numero
    return sumando

#bloque principal

numero=int(input("Numero: "))
sumando=carga_datos(numero)
print(sumando)