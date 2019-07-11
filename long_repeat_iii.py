def long_repeat(line):

    count = 0
    longest = 0
    letter = None

    for c in line:
        if letter is None:  # starting
            letter = c
            count += 1

        elif c == letter:  # in a substring; count the match
            count += 1

        else:   # finished a substring; record and reset
            if count > longest:
                longest = count
                        # reset to the new substring
                letter = c
                count = 1

    if count > longest:  # check last count
        longest = count
    return longest




# bloque principal

line = 'abababaab'
print(long_repeat(line))