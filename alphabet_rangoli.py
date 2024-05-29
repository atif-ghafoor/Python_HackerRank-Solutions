def abc(n):
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    for i in range(0, n):
        result.append(l[i])
    return result 

def reverse1(c):
    c = list(c)
    c.reverse()
    c = ''.join(c)
    return c

def minus(c):
    c = list(c)
    c.pop()
    c.pop()
    c = ''.join(c)
    return c
    
def print_rangoli(size):
    # your code goes here
    n_v = size*2
    n_h = n_v-2
    l = abc(size)
    l.reverse()
    c = ''
    index_l = 1
    index_1_c = 1
    a = l[0]
    for i in range(size):
        if size == 1:
            print(a.center(1, '-'))
            break
        print(c.rjust(n_h-1, '-')+a.center(3, '-')+(reverse1(c)).ljust(n_h-1, '-'))
        if i == size-1:
            break
        if c == '': 
            c = l[0]
        a = l[index_l]
        index_l = index_l + 1
        if i >= 1:
            c += '-'+l[index_1_c]
            index_1_c = index_1_c + 1
    index_l = 1
    index_1_c = 1
    l = abc(size)
    l.remove(l[0])
    if l == []:
        l = None
    else:
        a = l[0]
    for i in range(size-1):
        if i <= size-3:
            c = minus(c)
        if i == size - 2:
            c = ''
        print(c.rjust(n_h-1, '-')+a.center(3, '-')+(reverse1(c)).ljust(n_h-1, '-'))
        if i == size - 2:
            break
        a = l[index_l]
        index_l = index_l + 1
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)