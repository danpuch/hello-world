def checkio(text):
    if len(text) > 10e5:
        return "Es demasiado largo"
    text=text.lower()
    l = [x for x in text if x.isalpha()]
    d = {x:0 for x in l}

    for i in l:
        d[i] += 1

    a = [(-d[i], i) for i in d]
    a.sort()
    return a[0][1]





if __name__ == '__main__':

    text="Hello World"
    print(checkio(text))