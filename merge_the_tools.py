def merge_the_tools(string, k):
    # your code goes here
    k_len = int(len(string)/k)
    ind_1 = 0
    ind_2 = k
    lis_sub_string = []
    for i in range(k_len):
        lis_sub_string.append(string[ind_1:ind_2])
        ind_1 = ind_2
        ind_2 = ind_2 + k
    for i in lis_sub_string:
        i = ''.join(list(set(list(i))))
        print(i)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)