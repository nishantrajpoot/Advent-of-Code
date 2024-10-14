from functools import reduce

def roll_dice(pos_a, pos_b):
    tot_a, tot_b = 0, 0
    dice = 0
    start = 1
    end = 7
    while True:

        x = [100 if (x % 100 == 0) else x % 100 for x in range(start, end)]

        temp_a = '+'.join([str(x) for x in x[:3]])
        temp_b = '+'.join([str(x) for x in x[3:]])

        pos_a += reduce(lambda a, b: a+b, x[:3])
        pos_b += reduce(lambda a, b: a+b, x[3:])

        start += 6
        end += 6

        if pos_b % 10 != 0:
            pos_b = pos_b % 10
        else:
            pos_b = 10

        if pos_a % 10 != 0:
            pos_a = pos_a % 10
        else:
            pos_a = 10

        tot_a += pos_a
        dice +=3

        if tot_a >= 1000:
            return tot_b * dice

        tot_b += pos_b
        dice +=3

        if tot_b >= 1000:
            return tot_a * dice

        print('Player {} rolls {} and moves to space {} for a total score of {}'.format(1, temp_a,pos_a, tot_a ))
        print('Player {} rolls {} and moves to space {} for a total score of {}'.format(2, temp_b, pos_b, tot_b))



input = \
    ['Player 1 starting position: 5',
'Player 2 starting position: 6']

print(roll_dice(5, 6))

