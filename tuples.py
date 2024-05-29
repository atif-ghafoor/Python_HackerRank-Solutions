if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    t = tuple(arr)
    result = hash(t)
    print(result)