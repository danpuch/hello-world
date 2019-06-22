#game of the Dragon
import random
import time

def escenario_intro():
    print("Texto 1")
    time.sleep(1)
    print("Texto 2")
    time.sleep(1)

def escenario_seleccion_cueva():
    my_num_cueva = ''
    while my_num_cueva != '1' and my_num_cueva != '2':
        print("Selecciona la cueva 1 o 2:")
        my_num_cueva = input()

    return my_num_cueva

def escenario_explorar_cueva(var1):
    print("Texto 3")
    time.sleep(1)
    print("Texto 4")
    time.sleep(1)

    pc_number = random.randint(1,2)

    if var1 == str(pc_number):
        print("You win!")
    else:
        print("You Lose!")

play_again = 'yes'
while play_again == "yes" or play_again == 'y':
    escenario_intro()

    nueva_cueva = escenario_seleccion_cueva()
    escenario_explorar_cueva(nueva_cueva)

    print("Play again?")
    play_again = input()