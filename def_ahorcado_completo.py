#juego ahorcado
#importar bibliotecas
import random

#declarar variables
TABLERO=[''' 
    ___
   |   | 
       |
       |
       |
    ___|___''', '''
    
    ___
   |   |
   O   |
       |
       |
    ___|___''' , '''
        
    ___
   |   |
   O   |
   |   |
       |
    ___|___ ''', '''
    
    ___
   |   |
   O   |
   |   |
  /    |
    ___|___ ''', '''
    
    ___
   |   |
   O   |
   |   |
  / \  |
    ___|___''' , '''
    
    ___
   |   |
   O   |
  /|   |
  / \  |
    ___|___ ''', '''

    ___
   |   |
   O   |
  /|\  |
  / \  |
    ___|___ '''  ]
 

PALABRAS='perro gato pajaro cabra vaca cienpies python tigre leon gorila mono dinosaurio'.split()

#declarar funciones
def fpalabra_secreta(PALABRAS):
    indice_palabra=random.randint(0,len(PALABRAS)-1)
    sec_palabra=PALABRAS[indice_palabra]
    return sec_palabra

def fmostrar_Tablero(TABLERO, letras_no, letras_ok, palabra_secreta):
    print(TABLERO[len(letras_no)])
    print()
    print("Letras Descartadas: ", end='')
    for letra in letras_no:
        print(letra, end=' ')
    print()
    espacios_vacios = '_' * len(palabra_secreta)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] in letras_ok:
            espacios_vacios = espacios_vacios[:i] + palabra_secreta[i] + espacios_vacios[i+1:]

    for letra in espacios_vacios:
        print(letra, end=' ')
    print()

def fobtener_intento(letrasprobadas):
    while True:
        print('Adivina una letra: ')
        intento= input()
        intento=intento.lower()
        if len(intento)!=1:
            print("Por favor, introduce solo una letra: ")
        elif intento in letrasprobadas:
            print("Ya has probado esa letra")
        elif intento not in 'abcdefghijklmnopqrstuvwxyzñç':
            print("Por favor, ingrese una LETRA: ")
        else:
            return intento

def fjugar_de_nuevo():
    print("Quieres jugar de nuevo?: ")
    return input().lower().startswith('s')


#bloque principal

print("***********AHORCADO************")
letras_no=''
letras_ok=''
palabra_secreta= fpalabra_secreta(PALABRAS)
juego_terminado=False

while True:
    fmostrar_Tablero(TABLERO, letras_no, letras_ok, palabra_secreta)
    intento = fobtener_intento(letras_no + letras_ok)

    if intento in palabra_secreta:
        letras_ok = letras_ok + intento
        encontrado_todas=True

        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_ok:
                encontrado_todas = False
                break

        if encontrado_todas:
            print("Si, la palabra secreta es ", palabra_secreta, "Has ganado!!")
            juego_terminado = True

    else:
        letras_no = letras_no + intento
        if len(letras_no)==len(TABLERO)-1:
            fmostrar_Tablero(TABLERO, letras_ok, letras_no, palabra_secreta)
            print("Te has quedado sin intentos despues de "+ str(len(letras_no)))
            juego_terminado = True

        if juego_terminado:
            if fjugar_de_nuevo():
                letras_no = ''
                letras_ok = ''
                juego_terminado = False
                palabra_secreta = fpalabra_secreta(PALABRAS)
            else:
                break



