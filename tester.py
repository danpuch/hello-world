#elegido por la maquina

import random

def generar_numero():
    pc_num=''
    for i in range(1,long+1):
        gebe=str(random.randint(1,4))
        pc_num+=gebe
    return pc_num

def adivinar(pc_num):
    print("Ingresa tu numero. Debe tener", len(pc_num), "numeros:")
    my_number=str(input())
    while pc_num!=my_number:
        contador=0
        for i in range(len(pc_num)):
            if pc_num[i]==my_number[i]:
                contador+=1
        print("Has acertado", contador)
        my_number=str(input("Ingresa otro numero: "))
    return my_number

#bloque principal
pc_num=generar_numero()
print(pc_num)
adivinar(pc_num)
print("Congraturalios")
