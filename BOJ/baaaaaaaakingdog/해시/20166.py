import sys

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m, k = list(map(int, sys.stdin.readline().rstrip().split()))

board = []
answers = []
result = []
count = 0
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

for _ in range(k):
    answers.append(sys.stdin.readline().rstrip())

def dfs(cur_str, x, y, answer):
    global count, board

    if len(cur_str) > 5:
        return

    if cur_str == answer:
        count += 1
        return
    
    temp = cur_str + board[x][y]

    for move in moves:
            nx, ny = (x + move[0]) % n, (y + move[1]) % m
            dfs(temp, nx, ny, answer)


for answer in answers:
    count = 0
    for i in range(n):
        for j in range(m):
            dfs('', i, j, answer)
    
    result.append(count/8)
    count  = 0

print('\n'.join(list(map(str, result))))