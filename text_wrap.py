import textwrap

def wrap(string, max_width):
    start_position = 0
    end_position = max_width
    lines = len(string)/max_width
    lines = int(lines)
    str1 = ''
    for i in range(lines + 1):
        result = string[start_position:end_position]
        start_position = end_position
        end_position = end_position + max_width
        str1 += result
        str1 += '\n'
    return str1


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)