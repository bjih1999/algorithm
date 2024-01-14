import sys

n = int(sys.stdin.readline().rstrip())

board = []

for i in range(n):
    board.append([' '] * n)

def func(x, y, k):
    global board
    if k < 3:
        return
    
    unit = k//3
    for i in range(k):
        for j in range(k):
            if unit <= i < unit * 2 and unit <= j < unit * 2:
                board[x + i][y + j] = ' '
            else:
                board[x + i][y + j] = '*'
    
    # for i in range(n):
    #     print(''.join(board[i]))
    
    # print(' ')
    for i in range(3):
        for j in range(3):
                if i != 1 or j != 1:
                    func(x + unit * i, y + unit * j, unit)

func(0, 0, n)
for i in range(n):
    print(''.join(board[i]))