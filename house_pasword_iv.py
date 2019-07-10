import re

def checkio(data):
    return True if re.search('[a-z]',data) and re.search('[A-Z]',data) and re.search('[0-9]',data) and len(data)>=10 else False




if __name__ == '__main__':

    data='bAse730onE43'
    print(checkio(data))