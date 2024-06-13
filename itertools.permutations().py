# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, l = input().split(' ')
lis = list(permutations(s, int(l)))
lis = sorted(lis)
for i in lis:
    i = ''.join(i)
    print(i)
