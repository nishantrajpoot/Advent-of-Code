from statistics import median

# Syntax scoring
def reverse(sym):
    dic_rev = {'(': ')', '{': '}', '[': ']', '<': '>'}

    if sym == ')':
        return '('
    elif sym == '}':
        return '{'
    elif sym == ']':
        return '['
    elif sym == '>':
        return '<'


def check_syntax(input, total):
    # ( ) [ ] { } < >
    # legal [<>({}){}[([])<>]]
    # not legal <([]){()}[{}])

    arr_open = []
    arr_close = []
    sum = 0
    symbols = ['(', '[', '{', '<']
    symbols_rev = {')': '(', '}': '{', ']': '[', '>': '<'}
    symbols_cost = {')': 3, ']': 57, '}': 1197, '>': 25137}
    symbols_open_cost = {'(': 1, '[': 2, '{': 3, '<': 4}

    for i in input:
        if i == "\n":
            continue
        if i.strip() in symbols:
            arr_open.append(i.strip())
        else:
            # if at the top
            if arr_open[-1] == symbols_rev[i]:
                arr_open = arr_open[:-1]

            # if not found at the top but at other position then remove the first from last
            # elif rev_i in arr_open:
            #     arr_open.reverse()
            #     arr_open.remove(rev_i)
            #     arr_open.reverse()
            else:
                # print('close', i)
                arr_open = arr_open[:-1]
                arr_close.append(i.strip())
        # print(i)
        # print(arr_open)
        # print(arr_close)

    # print(arr_open)
    # print(arr_close)
    if arr_close:
        return
    for i in arr_open[::-1]:
        sum *= 5
        sum += symbols_open_cost[i]
        # print(i, sum)

    # print('open-> ', arr_open)
    total.append(sum)
    # 436497



ip = open('syntax.txt')

total = []
ct = 0
for i in ip:
    ct+=1
    # print('input-> ', i.strip())
    check_syntax(i, total)

print('lines', ct)
total.sort()
print(median(total))
total = []
check_syntax('<{([{{}}[<[[[<>{}]]]>[]]', total)
print(total)