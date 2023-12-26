import sys
from collections import deque

R, C = list(map(int, sys.stdin.readline().rstrip().split()))

board = []
dist  = []
fire_time = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))
    dist.append([-1 for _ in range(C)])
    fire_time.append([-1 for _ in range(C)])
queue = deque()
fires = deque()

for x in range(R):
    for y in range(C):
        if board[x][y] == 'J':
            dist[x][y] = 0
            queue.append((x, y))
        
        if board[x][y] == 'F':
            fires.append((x, y))
            fire_time[x][y] = 0

while fires:
    x, y = fires.popleft()
    
    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != '#' and fire_time[nx][ny] < 0:
            fire_time[nx][ny] = fire_time[x][y] + 1
            fires.append((nx, ny))

# for f in fire_time:
#     print(f)
# print()
while queue:
    x, y = queue.popleft()
    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            print(dist[x][y] + 1)
            exit(0)
        if board[nx][ny] == '.' and dist[nx][ny] < 0 and (fire_time[nx][ny] == -1 or  fire_time[nx][ny] > dist[x][y] + 1):
            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
          

    # for b in dist:
    #     print(b)
    # print()

print('IMPOSSIBLE')


