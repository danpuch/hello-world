def second_index(text, symbol):

    if text.count(symbol)<2:
        return None
    first = text.find(symbol)
    return text.find(symbol, first + 1)

# bloque principal


text = 'find the river'
symbol = 'e'
reply = second_index(text, symbol)
print(reply)
