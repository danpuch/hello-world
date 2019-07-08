def left(text1):

    text=','.join(text1)
    text=text.lower()
    text=text.replace("right", "left")
    ','.join(text)

    return text



# bloque principal

text="left","Right", "Left", "stop"
text1=left(text)
print(text1)

