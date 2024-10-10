def decode_pattern(inp, last):
    if all(x == 0 for x in inp):
        return 0

    diff = []
    for i in range(1, len(inp)):
        diff.append(inp[i] - inp[i - 1])

    last += decode_pattern(diff, diff[-1])

    return last


input = ['0 3 6 9 12 15',
         '1 3 6 10 15 21',
         '10 13 16 21 30 45']

# input = open('mirage_input.txt')
#
total = 0
for i in input:
    d = list(map(int, i.split(' ')))
    # print(d[::-1])
    total += d[0] + decode_pattern(d[::-1], 0)
#
print('total:', total)