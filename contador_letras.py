def contador_lista(lista):
    resultado = 0
    for i in lista:
        resultado +=1
    return resultado

tu_frase = input("Introduce tu palabra: ")
print(contador_lista(tu_frase))