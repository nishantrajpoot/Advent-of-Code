def get_maxval(arr, type):
    z=0
    o=0
    for i in arr:
        if i == '0':
            z+=1
        else:
            o+=1

    if type ==1:
        if z>o:
            return '0'
        elif o>z:
            return '1'
        else:
            return '1'
    else:
        if z<o:
            return '0'
        elif o<z:
            return '1'
        else:
            return '0'


def diagnostics(array):

    # array_trans = list(zip(*array))


    # gamma = ['0' if (x.count('0') >= x.count('1')) else '1' for x in array_trans]
    # epsilon = ['1' if (x.count('0') >= x.count('1')) else '0' for x in array_trans]

    arr_oxygen = array.copy()
    arr_co2 = array.copy()
    pos=0

    while len(arr_oxygen)!=1:
        # [0, 1, 1, 1, 0]

        max_val = [x[pos] for x in arr_oxygen]

        val = get_maxval(max_val, 1)
        arr_oxygen = [x for x in arr_oxygen if x[pos] == val]

        print(pos, val, len(arr_oxygen), arr_oxygen)
        pos += 1

    pos = 0

    while len(arr_co2) != 1:
        # [0, 1, 1, 1, 0]
        max_val = [x[pos] for x in arr_co2]
        # occurance
        val = get_maxval(max_val, 2)
        arr_co2 = [x for x in arr_co2 if x[pos] == val]

        print(pos, val, len(arr_co2), arr_co2)
        pos += 1


    print(''.join(arr_oxygen[0]), ''.join(arr_co2[0]))
    return int(''.join(arr_oxygen[0]), 2) * int(''.join(arr_co2[0]), 2)

input = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

input = open("C:/Users/nishant.rajpoot/Downloads/input.txt")
arr=[]
for i in input:
    arr.append([x for x in i.strip()])

print(diagnostics(arr))
print(list(zip(*arr)))