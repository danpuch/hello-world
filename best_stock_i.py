def best_stock(data):

    answer=''
    index=0
    for i in data:
        if data[i] > index:
            index = data[i]
            answer=i
    return answer


# bloque principal

data = {
'CAC': 10.0,
'ATX': 390.2,
'WIG': 1.2

}

print(best_stock(data))