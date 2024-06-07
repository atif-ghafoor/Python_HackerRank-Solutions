def solve(s):
    lis = list(s)
    ls_str = []
    c_str = ''
    for i in lis:
        if i == ' ':
            c_str = c_str.capitalize()
            ls_str.append(c_str)
            c_str = ''
        else:
            c_str += i
    c_str = c_str.capitalize()
    ls_str.append(c_str)
    capitalize_str = ' '.join(ls_str)
    return capitalize_str

s = input()
result = solve(s)
print(result)