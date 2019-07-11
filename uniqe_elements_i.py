from collections import *

def checkio(data):

    l = []
    for i in data:
        if data.count(i)>1:
            l.append(i)

    return l

if __name__ == '__main__':
    data=[5,5,1, 1,5, 1, 2, 2, 3]
    print(checkio(data))