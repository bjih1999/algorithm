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
    
    if (board[i][j] == 'Y' and s >= 3):
        return False

    return True

def func(i, j):
    global board, answer, y, s, moves

    if board[i][j] == 'Y':
        y += 1
    else:
        s += 1
    
    if y + s == 7:
        for v in visited:
            print(v)
        answer += 1

    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if (0 <= ni < 5 and 0 <= nj < 5) and not visited[ni][nj]:
            if board[ni][nj] == 'Y' and y > 3:
                continue
            visited[ni][nj] = True
            if board[ni][nj] == 'Y':
                y += 1
            else:
                s += 1
            func(ni, nj)
            visited[ni][nj] = False
            if board[ni][nj] == 'Y':
                y -= 1
            else:
                s -= 1

func(0, 0)

print(answer)