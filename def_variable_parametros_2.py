'''confecciona lista que reciba entre 2 y n (siendo n = 2,3,4,5,6 ...
valores enteros,
retomar la suma de dichos parametros'''

def sumar(v1, v2, *lista):
    suma = v1 + v2
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

#bloque principal

print("Suma 1 + 2 + 3")
print(sumar(1, 2, 3))
print("Suma del 1 al 10")
print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

