

palabra1= input("Introduce la primera palabra: ")
palabra2= input("Introduce la segunda palabra: ")

def rimas(palabra1, palabra2):
    if palabra1[-3:]==palabra2[-3:]:
        print("Las palabras riman mucho!!! ")
    elif palabra1[-2:]==palabra2[-2:]:
        print("Las palabras riman un poquito!!!")
    elif palabra1[-1:]==palabra2[-1:]:
        print("Las palabras no riman")
    else:
        print("Nada de nada!!!!")


#bloque principal

rimas(palabra1, palabra2)





