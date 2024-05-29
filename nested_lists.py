if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    score_list = []
    for i in records:
        score_list.append(i[1])
    score_list = set(score_list)
    min1 = min(score_list)
    score_list.remove(min1)
    min2 = min(score_list)
    name_list = []
    for i in records:
        if i[1] == min2:
            name_list.append(i[0])
    name_list.sort()
    for i in name_list:
        print(i)