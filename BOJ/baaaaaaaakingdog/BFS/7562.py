import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
answers = []

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for _ in range(n):
    I = int(sys.stdin.readline().rstrip())
    dist = [[-1 for _ in range(I)] for _ in range(I)]
    queue = deque()
    start_x, start_y = list(map(int, sys.stdin.readline().rstrip().split()))
    dest_x, dest_y = list(map(int, sys.stdin.readline().rstrip().split()))
    answers.append(0)
    queue.append((start_x, start_y))
    dist[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()
        if x == dest_x and y == dest_y:
            answers[-1] = (dist[x][y])
            break

        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < I and 0 <= ny < I and dist[nx][ny] < 0:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    
for answer in answers:
    print(answer)