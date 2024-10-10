def south_move(grid):
    moved = False

    col_size = len(grid[0])
    row_size = len(grid)

    for col in range(col_size):
        row=0
        while row < row_size:
            if grid[row][col] == 'v' and grid[(row+1) % row_size][col] == '.':
                grid[row][col] = '.'
                grid[(row+1) % row_size][col] = 'v'
                moved = True
                # if replaced then skip these 2 col values
                if row <= row_size - 2:
                    row += 1
            row += 1

    return grid, moved

def east_move(grid):
    moved = False
    col_size = len(grid[0])
    row_size = len(grid)

    for row in range(row_size):
        col=0
        while col < col_size:
            if grid[row][col] == '>' and grid[row][(col+1) % col_size] == '.':
                grid[row][col]='.'
                grid[row][(col+1) % col_size]= '>'
                moved = True
                # if replaced then skip these 2 col values
                if col <= col_size-2:
                    col += 1
            col+=1

    return grid, moved

# inp = open('C:/Users/nishant.rajpoot/Downloads/cucumber.txt')

inp = ['v...>>.vv>',
'.vv>>.vv..',
'>>.>v>...v',
'>>v>>.>.v.',
'v>v.vv.v..',
'>.>>..v...',
'.vv..>.>v.',
'v.v..>>v.v',
'....v..v.>']

# inp = ['...>...',
# '.......',
# '......>',
# 'v.....>',
# '......>',
# '.......',
# '..vvv..']

grid = [list(x) for x in inp]
# print(np.array(grid))
# print(list('...>>>>>...'))

moved_east, moved_south = True, True
step=0
while any([moved_east, moved_south]):
    grid, moved_east = east_move(grid)
    grid, moved_south = south_move(grid)

    # if step==1800:
    #     break

    if step <= 4:
        print(step)
        for i in grid:
            print(''.join(i))


    if step==3:
        break

    step+=1

    # print(step, moved_east, moved_south)

print('after %s steps'%(step - 1))