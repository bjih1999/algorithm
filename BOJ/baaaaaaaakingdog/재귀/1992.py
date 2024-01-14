import sys

n = int(sys.stdin.readline().rstrip())

board = []
answer = ''

for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

def check(x, y, k):
    for i in range(x, x + k):
        for j in range(y, y + k):
            if board[x][y] != board[i][j]:
                return False
    
    return True

def func(x, y, n):
    global answer
    if check(x, y, n):
        answer += str(board[x][y])
        return

    answer += '('
    k = n // 2
    for i in range(2):
        for j in range(2):
            func(x + k*i, y + k*j, k)

    answer += ')'

func(0, 0, n)
print(answer)