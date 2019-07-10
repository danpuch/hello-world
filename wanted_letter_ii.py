def checkio(x):
    if len(x) >10e5 :
        return 'sentence is extremely long'
    x = x.lower()
    #    l = []
    #    d ={}
    #    for u in x:
    #        if u in 'aqwertyuioplkjhgfdszxcvbnm' :
    #            l.append(u)
    #            d[u] =0
    l = [c for c in x if c.isalpha()]
    d = {c: 0 for c in l}
    for i in l :
        d[i] +=1
    #    a=[[i, d[i]] for i in d]
    #    a.sort(key=lambda x:x[1], reverse=True)
    a = [(-d[i], i) for i in d]
    a.sort()
    return a[0][1]
#    for i in a:
#        return i[0]

if __name__ == '__main__':

    text="Hello World"
    print(checkio(text))