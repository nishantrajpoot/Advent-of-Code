import re
import numpy as np
from functools import reduce


# Function to perform DFS and label the connected components
def dfs(grid, x, y, visited):
    # If it's out of bounds, or already visited, or not part of a region, return
    if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or grid[x][y] >= 9:
        return 0
    visited[x][y] = True  # Mark the cell as visited
    # The size of this region (initially 1 for the current cell)
    size = 1
    # Check all four possible directions (up, down, left, right)
    size += dfs(grid, x - 1, y, visited)  # up
    size += dfs(grid, x + 1, y, visited)  # down
    size += dfs(grid, x, y - 1, visited)  # left
    size += dfs(grid, x, y + 1, visited)  # right
    return size


def lowest_point(matrix):
    low = 0
    arr_low = []
    for i in range(rows):
        for j in range(cols):
            a = b = c = d = True
            # U
            if i > 0:
                a = matrix[i - 1][j] > matrix[i][j]
            # B
            if i < rows - 1:
                b = matrix[i + 1][j] > matrix[i][j]
            # L
            if j > 0:
                c = matrix[i][j - 1] > matrix[i][j]
            # R
            if j < cols - 1:
                d = matrix[i][j + 1] > matrix[i][j]

            if all([a, b, c, d]):
                low += matrix[i][j] + 1
                arr_low.append([i, j])

    region_sizes = []
    # 2D list to mark visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # find the size of basins
    # tracing all low points
    for i in range(rows):
        for j in range(cols):
            if [i, j] not in arr_low or matrix[i][j] != 9:
                region_size = dfs(matrix, i, j, visited)

                if region_size > 0:
                    region_sizes.append(region_size)

                # check distance of i,j from all the low points

    return region_sizes


input = open('smoke.txt')

d = []
for i in input:
    d.append(list(map(int, re.findall(r'[0-9]', i))))

arr = np.array(d)
rows, cols = arr.shape[0], arr.shape[1]
size = lowest_point(arr)
size.sort()
print(reduce(lambda a, b: a*b, size[-3:]))
