#juego adivina un numero

import random

tries = 0
tries_left = 5
pc_number = random.randint(1,10)
print("Hello!, Como te llamas?")
name = input()
print("Hola " + name + ". Adivina un numero entre 1 y 10.")

while tries < 5:
    print("Pon aquí tu numero")
    my_number = input()
    my_number = int(my_number)

    tries += 1
    tries_left -=1

    if my_number < pc_number:
        print("Tu número es más pequeño. Te quedan " + str(tries_left) + " intentos")
    if my_number > pc_number:
        print("Tu número es más grande. Te qudan " + str(tries_left) + " intentos")
    if my_number == pc_number:
        break
if my_number == pc_number:
    tries = str(tries)
    print("Felicidades. Has acertado mi número en " + tries + " intentos!! ")
if my_number != pc_number:
    pc_number = str(pc_number)
    print("Lo siento. No has adivinado mi número. Era el " + pc_number)