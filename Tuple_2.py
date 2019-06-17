'''funcion que solicite dia, mes año .
otra funcion que reciba una tupla con la
fecha para mostrarla'''

def dataTuple():
    print("Hello. Please, introduce the following information: ")
    dd = int(input("Introduce Day: "))
    mm = input("Introduce Month: ")
    yy = int(input("Introduce Year: "))
    return (dd, mm, yy)

def impDate(fecha):
    print(fecha[0], fecha[1], fecha[2])

#bloque principal

fecha = dataTuple()
impDate(fecha)