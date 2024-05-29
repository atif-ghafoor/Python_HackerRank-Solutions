thickness = int(input())
c = 'H'
# This must be an odd number
# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness - 1, ' ')+c+(c*i).ljust(thickness - 1, ' '))
# top pillers
for i in range(thickness + 1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
# middle belt
for i in range((thickness + 1)//2):
    print((c*thickness*5).center(thickness*6))
# bottom pillers
for i in range(thickness + 1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
# lower cone
n = thickness
thickness = []
for i in range(n):
    thickness.append(i)
thickness.reverse()
for i in thickness:
    print(((c*i).rjust(n - 1, ' ')).rjust((n * 5)-1)+c+(c*i).ljust(n - 1, ' '))

