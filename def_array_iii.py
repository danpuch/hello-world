def checkio(array):
    nlista=[]
    for i in range(len(array)):
        if i % 2 ==0:
            nlista.append(array[i])

    sumarray=0
    for k in nlista:
        sumarray+=k

    totarray=sumarray * array[-1]

    return totarray


lista=[6]
resultado=checkio(lista)
print(resultado)
