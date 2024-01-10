import sys
import math

n = int(sys.stdin.readline().rstrip())
pow = int(math.log(n, 3))

board = []
answer = {
    -1: 0,
    0: 0,
    1: 0,
}

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

def check(x, y, n):
    global answer
    global board
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != board[x][y]:
                return False
    
    return True


def func (x, y, k):
    if check(x, y, k) or k == 1:
        answer[board[x][y]] += 1
        return
    
    for i in range(3):
        for j in range(3):
            func(x/3 + k/3 * i, y/3 + k/3 * j, k/3)

func(0, 0, n)
print(answer)





