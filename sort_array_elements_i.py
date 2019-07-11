from collections import*

def frequency_sort(items1, items2):

    items=str(items1)

    # si items es un digito
    l = [x for x in items if x.isdigit()]
    d = {x:0 for x in l}
    for i in l:
        d[i] += 1
    nl=[]
    for elem in d:
        nl.append(elem * d[elem])

    #a = [(d[i], i) for i in d]
    #a.sort(reverse=True)

    '''si items es una cadena'''

    l2=items2
    d1={t:int(0) for t in l2}
    for f in l2:
        d1[f] += 1

    nl2=[]
    for elem2 in d1:
        nl2.append(elem2 * d1[elem2], )


    print(items2)
    print(d1)
    print(l)
    print(d)
    print(nl)
    print(nl2)




if __name__ == '__main__':
    items1=[4, 6, 3 ,2, 2, 6, 4, 4, 6, 3, 3, 3, 3, 3]
    items2=['bob', 'bob', 'carl', 'alex', 'bob', 'alex', 'alex', 'alex']
    frequency_sort(items1, items2)