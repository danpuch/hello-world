def second_index(text, symbol):
    if text.count(symbol) < 2:
        return None
    contador = 0
    while contador != 2:
        paralelo = 0
        for i in range(len(text)):
            if symbol == text[i]:
                contador += 1
                paralelo = i

        return paralelo


# bloque principal


text = 'find the rivere'
symbol = 'e'
reply = second_index(text, symbol)
print(reply)
