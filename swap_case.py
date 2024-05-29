def swap_case(s):
    v = []
    for i in s:
        a = i.lower()
        if i == a:
            b = i.upper()
            v.append(b)
        elif i != a:
            b = i.lower()
            v.append(b)
    result = "".join(v)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)