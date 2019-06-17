'''carga lista de 5 enteros.
1.imprime la lista completa
2.Obtener y mostrar el mayor
3.Mostrar suma de todas las componentes'''

def carta_lista():
    lista_enteros=[]
    for i in range(5):
        number = int(input("Introduzca numero: "))
        lista_enteros.append(number)
    return lista_enteros

def mostrar_mayor(lista_enteros):
    mayorde=lista_enteros[0]
    for elemento in lista_enteros:
        if elemento>mayorde:
            mayorde=elemento
    print("El elemento mayor es: ", mayorde)

def sumatorio(lista_enteros):
    suma =0
    for elemento in lista_enteros:
        suma+=elemento
    print("La suma de elementos es: ", suma)

#bloque principal
lista_enteros=carta_lista()
print(lista_enteros)
mostrar_mayor(lista_enteros)
sumatorio(lista_enteros)

