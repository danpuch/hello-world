def checkio(words):
    if (word.isalpha() for word in words) and (len(words) > 2):
        return True
    return False


# bloque principal
words=("Hello World 123 Hello Bla 12")
print(checkio(words))