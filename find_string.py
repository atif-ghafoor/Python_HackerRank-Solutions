def count_substring(string, sub_string):
    count = 0
    current_index = 0
    string = list(string)
    lis = []
    len_string = len(string)
    len_sub_string = len(sub_string)
    for x in range(0, len_string):
        if len_sub_string <= len(string):
            for i in range(0, len_sub_string):
                lis.append(string[current_index])
                current_index = current_index + 1
        else:
            break
        current_index = 0
        string.remove(string[0])
        lis = "".join(lis)
        if lis == sub_string:
            count = count + 1
        lis = []
        
    
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)