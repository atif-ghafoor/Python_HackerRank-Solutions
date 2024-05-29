# Enter your code here. Read input from STDIN. Print output to STDOUT



from collections import Counter
shoes_count = int(input())
shoes_sizes = list(map(int, input().split()))
custCount = int(input())
list1 = []
for i in range(0, custCount):
    size, price = list(map(int, input().split()))
    list1.append((size, price))
sum1 = []
for i in list1:
    if i[0] in shoes_sizes:
        sum1.append(i[1])
        position = shoes_sizes.index(i[0])
        shoes_sizes[position] = 0
result = sum(sum1)
print(result)
