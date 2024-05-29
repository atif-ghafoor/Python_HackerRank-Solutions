# for finding octal number

def octal(n):
    l = []
    while n!= 0:
        q = int(n / 8)
        r = n % 8
        n = q
        l.append(r)
    l.reverse()
    l1 = []
    for i in l:
        l1.append(str(i))
    result = ''.join(l1)
    return result
# for finding hexadecimal number

def hexadecimal(n):
    l = []
    while n!= 0:
        q = int(n / 16)
        r = n % 16
        n = q
        l.append(r)
    l.reverse()
    l1 = []
    for i in l:
        l1.append(str(i))
    for i in l1:
        if i == '10':
            index = l1.index('10')
            l1[index] = 'A'
        if i == '11':
            index = l1.index('11')
            l1[index] = 'B'
        if i == '12':
            index = l1.index('12')
            l1[index] = 'C'
        if i == '13':
            index = l1.index('13')
            l1[index] = 'D'
        if i == '14':
            index = l1.index('14')
            l1[index] = 'E'
        if i == '15':
            index = l1.index('15')
            l1[index] = 'F'
    result = ''.join(l1)
    return result
# for finding binary number

def binary(n):
    l = []
    while n!= 0:
        q = int(n / 2)
        r = n % 2
        n = q
        l.append(r)
    l.reverse()
    l1 = []
    for i in l:
        l1.append(str(i))
    result = ''.join(l1)
    return result
    
def print_formatted(number):
    # your code goes here
    a = binary(number)
    b = len(a)
    for i in range(1, number + 1):
        print(str(i).rjust(b, ' '), octal(i).rjust(b, ' '), hexadecimal(i).rjust(b, ' '), binary(i).rjust(b, ' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)