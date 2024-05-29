if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        arr = list(input().split())
        if arr[0] == "insert":
            x = int(arr[1])
            y = int(arr[2])
            list1.insert(x, y)
        elif arr[0] == "print":
            print(list1)
        elif arr[0] == "remove":
            x = int(arr[1])
            list1.remove(x)
        elif arr[0] == "append":
            x = int(arr[1])
            list1.append(x)
        elif arr[0] == "sort":
            list1.sort()
        elif arr[0] == "pop":
            list1.pop()
        elif arr[0] == "reverse":
            list1.reverse()
