import random
import time

puntos=0

def intro():
    print("Empieza el juego")

def seleccionar_cueva():
    cueva=''
    while cueva != 1 and cueva != 2:
        cueva=int(input("Selecciona cueva: "))
    return cueva

def explorar_cueva(numero_cueva):
    print("Vamos a ver como andas de suerte...")
    pc_number=random.randint(1,2)
    pc_number=int(pc_number)

    if pc_number == numero_cueva:
        print("Has ganado 100 puntos!!!")
        global puntos
        puntos+=100

    else:
        print("Has perdido 50 puntos!!!")
        puntos-=50

again='y'
while again == 'y':
    intro()
    explorar_cueva(seleccionar_cueva())
    print(puntos)
    again= input("Quieres volver a jugar?: ")



