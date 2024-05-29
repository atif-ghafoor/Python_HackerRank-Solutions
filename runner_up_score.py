# i code my self max function, you can use built in function max
def max(arr):
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    a = max(ar)
    max_v2 = ar[0]
    for i in ar:
        if max_v2 == a:
            if i < max_v2:
                max_v2 = i
        if i != a:
            if max_v2 < i:
                max_v2 = i
    print(max_v2)