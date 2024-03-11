import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer_list = []
for _ in range(n):
    m, n = list(map(int, list(sys.stdin.readline().rstrip().split())))
    queue = deque()

    board = []
    visited = []
    fire = deque()
    fire_visited = []
    for _ in range(n):
        board.append(list(sys.stdin.readline().strip()))
        visited.append([-1 for _ in range(m)])
        fire_visited.append([-1 for _ in range(m)])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*':
                fire.append((i, j))
                fire_visited[i][j] = 0
            
            if board[i][j] == '@':
                queue.append((i, j))
                visited[i][j] = 0
    
    while fire:
        x, y = fire.popleft()
        for move in moves:
            next_x, next_y = x + move[0], y + move[1]
            if (0 <= next_x < n and 0 <= next_y < m) and fire_visited[next_x][next_y] == -1 and board[next_x][next_y] != '#':
                fire.append((next_x, next_y))
                fire_visited[next_x][next_y] = fire_visited[x][y] + 1
    
    result = 'IMPOSSIBLE'
    while queue and result == 'IMPOSSIBLE':
        x, y = queue.popleft()
        
        for move in moves:
            next_x, next_y = x + move[0], y + move[1]
            if (next_x < 0 or next_x >= n) or (next_y < 0 or next_y >= m):
                result = visited[x][y] + 1
                break
        

            if board[next_x][next_y] != '#' and (visited[x][y] + 1 < fire_visited[next_x][next_y] or fire_visited[next_x][next_y] == -1) and visited[next_x][next_y] == -1:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = visited[x][y] + 1

    answer_list.append(result)

for answer in answer_list:
    print(answer)