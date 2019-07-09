from typing import List, Any

def all_the_same(elements):

    if elements == []:
        return True

    copu=elements[0]
    conta=0
    for i in elements:
        if i == copu:
            conta += 1

    if conta == len(elements):
        return True
    else:
        return False


if __name__ == '__main__':

    elements = [1,1,1,1]
    print(all_the_same(elements))