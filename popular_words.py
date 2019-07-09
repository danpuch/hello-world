def popular_words(text, words):

    text=text.lower()
    text=text.split()
    newdict={}

    for elem in text:
        if elem in words:

    return text





# bloque principal

words=['i', 'was', 'three', 'near']
text="When I was One I had just begun When I was Two I was nearly new"

print(popular_words(text, words))