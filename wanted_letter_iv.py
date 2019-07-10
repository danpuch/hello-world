def checkio(text):
    from collections import Counter
    import re
    sorted_text=sorted(re.findall(r'[a-zA-Z]', text.lower()))
    c=Counter(sorted_text).most_common()
    return c[0][0]

if __name__ == '__main__':

    text="Hello World"
    print(checkio(text))