def checkio(*args):

    if args == ():
        return 0

    imax= max(args)
    imin= min(args)

    diference= imax - imin
    return diference


print(checkio(1,2,3))