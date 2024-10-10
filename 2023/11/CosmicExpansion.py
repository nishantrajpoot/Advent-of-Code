import numpy as np
from collections import defaultdict

def cosmic_pairs(loc, num):
    s = [[(x, y) for y in range(x, num + 1) if x != y] for x in range(1, num + 1)]
    # 2d to 1d
    t = [j for sub in s for j in sub]

    # print(t)
    tot = 0

    for i, j in t:
        # print(i, j)
        x = abs(loc[j][0] - loc[i][0]) + abs(loc[j][1] - loc[i][1])
        tot += x
        # print('distance from {} --> {} is {}'.format(i, j, x))

    print(tot)


def add_extra_row(matrix):
    df = []
    dot = ['.' for _ in range(len(matrix[0]))]
    empty_rows = []

    # replace # with number
    for i in range(len(matrix)):
        t = 0
        for j in matrix[i]:
            if j == '#':
                t += 1
                break

        df.append(matrix[i])
        if t == 0:
            df.append(dot)
            empty_rows.append(i)

    return df, empty_rows


input = ['...#......',
         '.......#..',
         '#.........',
         '..........',
         '......#...',
         '.#........',
         '.........#',
         '..........',
         '.......#..',
         '#...#.....']


# input = open('cosmic.txt')

input_row = [list(x) for x in input]
s, empty_rows = add_extra_row(input_row)

# transpose
input_col = [list(col) for col in zip(*s)]

s, empty_cols = add_extra_row(input_col)

# transpose again
matrix = [list(col) for col in zip(*s)]

print(empty_rows)
print(empty_cols)

k = 0
loc = defaultdict(list)
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == '#':
            k += 1
            matrix[row][col] = k
            loc[k].append(row)
            loc[k].append(col)

print(np.array(matrix))
print(loc)
cosmic_pairs(loc, k)

# 9445168
#
