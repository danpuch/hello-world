
def seleccion_producto():
    print('''
    PRODUCTO                        CODIGO
    
    CAMISA............................1
    CINTURON..........................2
    ZAPATOS...........................3
    PANTALON..........................4
    CALCETINES........................5
    FALTA.............................6
    GORRA.............................7
    SUETER............................8
    CORBATA...........................9
    CHAQUETA.........................10
    
    ''')
    select=int(input("INTRODUZCA SELECCIÓN: "))
    return select

def compra(select):
    ropa={
        1:25,
        2:30,
        3:35,
        4:50,
        5:25,
        6:15,
        7:45,
        8:40,
        9:35,
        10:70
    }
    print("El precio es: $", ropa[select])
    unidades=int(input("Cuantas unidades quieres?: "))
    print('')
    tot_parcial=ropa[select]*unidades
    print("El total a pagar es $", tot_parcial)
    global cesta_compra
    cesta_compra+=tot_parcial



#BLOQUE PRINCIPAL

cesta_compra=0

again='y'
while again=='y':
    select=seleccion_producto()
    compra(select)
    again=input("Do you want to buy more products?: ")
print("The total amount is ", cesta_compra)
