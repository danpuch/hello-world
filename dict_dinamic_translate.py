'''Diccionario ingles, castellano
clave es ingles, valor es castellano
1.carga el diccionario
2.listado completo de diccionario
3.ingresa por teclado palabra en ingles y mostrar traduccion'''

def my_data():
    ddict={}
    playagain='y'
    while playagain =='y':
            ingles=input("Palabra Ingles: ")
            caste = input("Palabra Castellano: ")
            ddict[ingles]=caste
            playagain=input("Quieres ingresaer una nueva palabra?: ")
    return ddict

def imprimir_dict(ddict):
    print("****************************")
    print("El contenido del diccionario es: ")
    for elem in ddict:
        print(elem, ddict[elem], sep='=')

def palabra_teclado(ddict):
    playagain = 'y'
    while playagain == 'y':
        filtro = input("Que palabra quieres traducir?: ")
        if filtro in ddict:
            print(ddict[filtro])
            playagain = input("Quieres traducit otra palabra?: ")
        else:
            break

#bloque principal

ddict = my_data()
imprimir_dict(ddict)
palabra_teclado(ddict)