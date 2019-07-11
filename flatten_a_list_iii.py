def flat_list(array):

    l = []

    # for item in array:
    #     if type(item) is int:
    #         l.append(item)
    #     else:
    #         l = l + flat_list(item)

    for item in array:
        if isinstance(item, list):
            l= l + flat_list(item)
        else:
            l.append(item)

    return l




array=[[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
print(flat_list(array))