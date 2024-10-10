from collections import defaultdict
from functools import reduce
import re

def add_star(board, match):
    for k in range(5):
        for l in range(5):
            if board[k][l] == match:
                board[k][l] = '*'
                return board

    return board

def find_match(board):
    board_flip = list(zip(*board))

    for i in board:
        if all([True if x =='*' else False for x in i]):
            val = reduce(lambda a,b: a+b, [x for x in [j for sub in board for j in sub] if x != '*'])
            return 'Match', val

    for j in board_flip:
        if all([True if x == '*' else False for x in j]):
            val = reduce(lambda a, b: a + b, [x for x in [j for sub in board for j in sub] if x != '*'])
            return 'Match', val

    return 'Nope', 0

def Bingo(numbers, boards):
    covered = set()
    for i in numbers:
        # Run all the boards for every number
        for j in range(1, len(boards)+1):
            if j not in covered:
                boards[j] = add_star(boards[j], i)

        # check if all rows/columns match
        for k in range(1, len(boards)+1):
            if k not in covered:
                res, tot =  find_match(boards[k])
                if res == 'Match':
                    covered.add(k)
                    if len(covered) == len(boards):
                        return i * tot


count = 0
numbers = []
boards = defaultdict(list)

for i in open('C:/Users/nishant.rajpoot/Downloads/squid.txt'):
    if len(i.strip()) != 0 and count == 0:
        numbers = list(map(int, re.findall(r'[0-9]+', i.strip())))
    elif len(i.strip()) != 0:
        boards[count].append( list(map(int,re.findall(r'[0-9]+', i.strip()))) )
    else:
        count+=1

print(Bingo(numbers, boards))