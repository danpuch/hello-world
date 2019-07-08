def checkio(words):

    words2=words.split()
    conta = 0
    for elem in words2:
        if elem.isalpha():
            conta+=1
            if conta > 2:
                return True
        else:
            conta=0
    return False


# bloque principal
words=("Hello World 123 Hello Bla ")
print(checkio(words))