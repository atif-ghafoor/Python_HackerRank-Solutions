if __name__ == '__main__':
    s = input()
    a=b=c=d=e=False
    for char in s:
        if char.isalnum():
            a = True
        if char.isalpha():
            b = True
        if char.isdigit():
            c = True
        if char.islower():
            d = True
        if char.isupper():
            e = True
        if all([a, b, c, d, e]):
            break
    print(a, b, c, d, e, sep="\n")
