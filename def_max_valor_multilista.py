def max_grande(valor):
    grande=0
    for i in valor:
        if i>grande:
            grande= i
    print(grande)


valor=[42,3,6,7,21,8,41,2]
max_grande(valor)