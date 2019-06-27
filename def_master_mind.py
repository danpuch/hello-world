import random

def gen_aleatorio(largonum):
    numero=''
    for i in range(largonum):
        numero1=str(random.randint(1,4))
        numero+=numero1
    return numero

def pruebas(num_aleatorio, largonum):
    my_numero=input("Ingrese su numero: ")
    while num_aleatorio != my_numero:
        contador=0
        for i in range(largonum):
            if num_aleatorio[i]==my_numero[i]:
                contador+=1
        print("El numero", my_numero, "tienen", contador, "coincidencias")
        my_numero=input("Ingrese nuevo numero: ")
    return my_numero

#bloque principal

largonum=int(input("Introduce largo de numero: "))
num_aleatorio=gen_aleatorio(largonum)
my_numero=pruebas(num_aleatorio, largonum)

if my_numero==num_aleatorio:
    print("CONGRATULATIONS!!!!! You did it!!! ")




