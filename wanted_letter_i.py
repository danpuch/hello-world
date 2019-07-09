def checkio(text):

    text=text.lower()
    text=sorted(text, key=lambda x: -x[1], x[0])
    print(text)




if __name__ == '__main__':

    text="Hello World"
    print(checkio(text))