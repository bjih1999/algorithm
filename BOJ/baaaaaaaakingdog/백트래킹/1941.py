import sys

board = []
moves = [(-1, 0), (1, 0), (0, -1), (-1, 0)]
y = 0
s = 0
answer = 0
visited = [[False for _ in range(5)] for _ in range(5)]

for _ in range(5):
    board.append(list(sys.stdin.readline().rstrip()))

def promising(i, j):
    global board

    if i < 0 or i >= 5 or j < 0 or j >= 5:
        return False
    
    if (board[i][j] == 'Y' and y <= 3):
        return False

    return True

def func(i, j):
    global board, answer, y, s
    if board[i][j] == 'Y':
        y += 1
    else:
        s += 1
    
    if y + s == 7:
        print(y, s)
        answer += 1


for i in range(5):
    for j in range(5):
        for move in moves:
            ni, nj = i + move[0], j + move[1]

            if promising(ni, nj) and not visited[ni][nj]:
                visited[ni][nj] = True
                func(ni, nj)
                visited[ni][nj] = False

print(answer)