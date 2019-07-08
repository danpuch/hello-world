def absolute(numbers_array):

    newlist = []

    for k in numbers_array:
        for i, x in enumerate(newlist):
            if abs(k) < abs(x):
                newlist.insert(i, k)
                break
        else:
            newlist.append(k)

    return newlist

# Bloque principal

numbers = (-20, -5, 15, 10)
print(absolute(numbers))

