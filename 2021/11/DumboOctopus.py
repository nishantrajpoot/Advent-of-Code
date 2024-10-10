import numpy as np
import re

# Octopus blink problem
def change_to_matrix(inp):
    new_matrix = []
    for i in inp:
        new_matrix.append(list(map(int, re.findall(r"[0-9]", str(i)))))

    return np.array(new_matrix)


def illuminate_octopus(matrix, x, y):
    arr = []
    # running for all positions and add +1 else 0 to illuminate
    for i in range(x):
        for j in range(y):
            if matrix[i][j] < 9:
                matrix[i][j] = matrix[i][j] + 1
            else:
                matrix[i][j] = 0
                arr.append([i, j])

    return matrix, arr


def neighbour_illuminate(matrix, flash_index, i, j, x, y):
    # condition when either of these become zero
    neighbour_flash = []
    # UL
    if i > 0 and j > 0 and [i - 1, j - 1] not in flash_index:
        num = matrix[i - 1][j - 1] + 1
        if num < 10:
            matrix[i - 1][j - 1] = num
        else:
            matrix[i - 1][j - 1] = 0
            neighbour_flash.append([i - 1, j - 1])

    # U
    if i > 0 and [i - 1, j] not in flash_index:
        num = matrix[i - 1][j] + 1
        if num < 10:
            matrix[i - 1][j] = num
        else:
            matrix[i - 1][j] = 0
            neighbour_flash.append([i - 1, j])
    # UR
    if i > 0 and j < y - 1 and [i - 1, j + 1] not in flash_index:
        num = matrix[i - 1][j + 1] + 1
        if num < 10:
            matrix[i - 1][j + 1] = num
        else:
            matrix[i - 1][j + 1] = 0
            neighbour_flash.append([i - 1, j + 1])
    # L
    if j > 0 and [i, j - 1] not in flash_index:
        num = matrix[i][j - 1] + 1
        if num < 10:
            matrix[i][j - 1] = num
        else:
            matrix[i][j - 1] = 0
            neighbour_flash.append([i, j - 1])
    # R
    if j < y - 1 and [i, j + 1] not in flash_index:
        num = matrix[i][j + 1] + 1
        if num < 10:
            matrix[i][j + 1] = num
        else:
            matrix[i][j + 1] = 0
            neighbour_flash.append([i, j + 1])

    # BL
    if i < x - 1 and j > 0 and [i + 1, j - 1] not in flash_index:
        num = matrix[i + 1][j - 1] + 1
        if num < 10:
            matrix[i + 1][j - 1] = num
        else:
            matrix[i + 1][j - 1] = 0
            neighbour_flash.append([i + 1, j - 1])
    # B
    if i < x - 1 and [i + 1, j] not in flash_index:
        num = matrix[i + 1][j] + 1
        if num < 10:
            matrix[i + 1][j] = num
        else:
            matrix[i + 1][j] = 0
            neighbour_flash.append([i + 1, j])
    # BR
    if i < x - 1 and j < y - 1 and [i + 1, j + 1] not in flash_index:
        num = matrix[i + 1][j + 1] + 1
        if num < 10:
            matrix[i + 1][j + 1] = num
        else:
            matrix[i + 1][j + 1] = 0
            neighbour_flash.append([i + 1, j + 1])

    return matrix, neighbour_flash


def neighbour_illuminate_alt(matrix, arr, neighbour_flash, x, y):
    # break condition
    if not neighbour_flash:
        return matrix, arr

    flash = []
    for pos in neighbour_flash:
        i, j = pos[0], pos[1]

        # UL
        if i > 0 and j > 0 and [i - 1, j - 1] not in arr and [i - 1, j - 1] not in flash:
            num = matrix[i - 1][j - 1] + 1
            if num < 10:
                matrix[i - 1][j - 1] = num
            else:
                matrix[i - 1][j - 1] = 0
                flash.append([i - 1, j - 1])

        # U
        if i > 0 and [i - 1, j] not in arr and [i - 1, j] not in flash:
            num = matrix[i - 1][j] + 1
            if num < 10:
                matrix[i - 1][j] = num
            else:
                matrix[i - 1][j] = 0
                flash.append([i - 1, j])
        # UR
        if i > 0 and j < y - 1 and [i - 1, j + 1] not in arr and [i - 1, j + 1] not in flash:
            num = matrix[i - 1][j + 1] + 1
            if num < 10:
                matrix[i - 1][j + 1] = num
            else:
                matrix[i - 1][j + 1] = 0
                flash.append([i - 1, j + 1])
        # L
        if j > 0 and [i, j - 1] not in arr and [i, j - 1] not in flash:
            num = matrix[i][j - 1] + 1
            if num < 10:
                matrix[i][j - 1] = num
            else:
                matrix[i][j - 1] = 0
                flash.append([i, j - 1])
        # R
        if j < y - 1 and [i, j + 1] not in arr and [i, j + 1] not in flash:
            num = matrix[i][j + 1] + 1
            if num < 10:
                matrix[i][j + 1] = num
            else:
                matrix[i][j + 1] = 0
                flash.append([i, j + 1])

        # BL
        if i < x - 1 and j > 0 and [i + 1, j - 1] not in arr and [i + 1, j - 1] not in flash:
            num = matrix[i + 1][j - 1] + 1
            if num < 10:
                matrix[i + 1][j - 1] = num
            else:
                matrix[i + 1][j - 1] = 0
                flash.append([i + 1, j - 1])
        # B
        if i < x - 1 and [i + 1, j] not in arr and [i + 1, j] not in flash:
            num = matrix[i + 1][j] + 1
            if num < 10:
                matrix[i + 1][j] = num
            else:
                matrix[i + 1][j] = 0
                flash.append([i + 1, j])
        # BR
        if i < x - 1 and j < y - 1 and [i + 1, j + 1] not in arr and [i + 1, j + 1] not in flash:
            num = matrix[i + 1][j + 1] + 1
            if num < 10:
                matrix[i + 1][j + 1] = num
            else:
                matrix[i + 1][j + 1] = 0
                flash.append([i + 1, j + 1])

    for i in flash:
        arr.append(i)

    return neighbour_illuminate_alt(matrix, arr, flash, x, y)


def octopus_blink(matrix, count: int):
    # print(matrix)
    x, y = matrix.shape[0], matrix.shape[1]
    p = 0

    for i in range(count):
        # for p in range(1, count + 1):
        print("After Step %s" % p)
        p = p + 1

        # increase by +1 and return list with 0 as arr
        matrix, arr = illuminate_octopus(matrix, x, y)

        # recursive function to get the neighbor illumination
        matrix, arr = neighbour_illuminate_alt(matrix, arr, arr, x, y)

    print(matrix)


inp = [5483143223,
       2745854711,
       5264556173,
       6141336146,
       6357385478,
       4167524645,
       2176841721,
       6882881134,
       4846848554,
       5283751526]

mtr = change_to_matrix(inp)

octopus_blink(mtr, 10)
