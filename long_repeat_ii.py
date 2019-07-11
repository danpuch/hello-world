def long_repeat(line):

    contador=0
    larga=1
    letra=None

    for i in line:
        if letra == None:
            letra=i
            contador+=1
        elif letra == i:
            contador+=1
            

    return longest



# bloque principal

line = 'sdsffffse'
print(long_repeat(line))