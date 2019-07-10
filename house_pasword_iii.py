def checkio(data: str) -> bool:

    #replace this for solution

    if re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)^[a-zA-Z\d]{10,63}$",data):

        return True

    else:

        return False



if __name__ == '__main__':

    data='bAse730onE43'
    print(checkio(data))