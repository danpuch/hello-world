#carga lista con 5 enteros. Localiza el menor y dime posicion

lista_enteros = []

for i in range(5):
    entero = int(input("Ingresa valor: "))
    lista_enteros.append(entero)

menor = lista_enteros[0]
posicion = 0
for i in range(1,5):
    if lista_enteros[i]<menor:
        menor = lista_enteros[i]
        posicion = i

print("La lista entera: ", lista_enteros)
print("El valor menor de la lista es: ", menor)
print("El valor menor se encuentra en : ", posicion)