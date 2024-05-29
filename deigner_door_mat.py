# Enter your code here. Read input from STDIN. Print output to STDOUT
thickness, mat_size1 = map(int, input().split())
c = '.|.'
mat_size = int(mat_size1/2)
mid_number = int(thickness/2) + 1
for i in range(thickness):
    print((c*i).rjust(mat_size-1, '-')+c+(c*i).ljust(mat_size-1, '-'))
    if i == mid_number - 2:
        print('WELCOME'.center(mat_size1, '-'))
        break
l = []
for i in range(mid_number-1):
    l.append(i)
l.reverse()
for i in l:
    print((c*i).rjust(mat_size-1, '-')+c+(c*i).ljust(mat_size-1, '-'))
