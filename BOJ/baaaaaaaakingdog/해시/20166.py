import sys

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m, k = list(map(int, sys.stdin.readline().rstrip().split()))

board = []
answers = []
result = {}
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

for _ in range(k):
    answers.append(sys.stdin.readline().rstrip())

def dfs(cur_str, x, y):
    global board

    if not cur_str in result.keys():
        result[cur_str] = 1
    else:
        result[cur_str] += 1

    if len(cur_str) == 5:
        return
    
    for move in moves:
        nx, ny = (x + move[0] + n) % n, (y + move[1] + m) % m
        dfs(cur_str + board[nx][ny], nx, ny)


for i in range(n):
    for j in range(m):
        dfs(board[i][j], i, j)

for answer in answers:
    if answer in result.keys():
        print(result[answer])
    else:
        print(0)
