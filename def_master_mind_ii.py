#juego Master Mind

import random

def crear_aleatorio():
    global longitud
    pc_cadena=''
    for i in range(longitud):
        pc_num=str(random.randint(1,4))
        pc_cadena+=pc_num
    return pc_cadena

def adivinar(pc_cadena, longitud):
    print("Introduce tu numero de",longitud, "valores: ")
    my_num=str(input())
    while my_num != pc_cadena:
        contador=0
        for i in range(longitud):
            if my_num[i]==pc_cadena[i]:
                contador+=1
        print(contador)
        my_num=str(input("Introduce un nuevo valor: "))
    return my_num

#bloque principal

longitud=int(input("Cuantos digitos tiene tu numero?: "))
pc_cadena=crear_aleatorio()
print(pc_cadena)
adivinar(pc_cadena, longitud)
print("Enhorabuena!!!")
