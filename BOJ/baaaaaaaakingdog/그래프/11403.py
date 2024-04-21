import sys

n = int(sys.stdin.readline().rstrip())

adj = [[] for i in range(n+1)]
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    row = [0]
    row.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    adj[i] = row

def dfs(start, cur, end, is_start):
    global visited, board
    if not is_start and cur == end:
        board[start][end] = 1

    if not is_start:
        visited[cur] = True
    
    for i in range(1, n+1):
        if not adj[cur][i] or visited[i]:
            continue
        
        dfs(start, i, end, False)


for i in range(1, n+1):
    for j in range(1, n+1):
        visited = [False for _ in range(n+1)]
        dfs(i, i, j, True)

for row in board[1:]:
    print(' '.join(map(str, row[1:])))