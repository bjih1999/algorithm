import sys
from collections import deque


n, m = list(map(int, sys.stdin.readline().rstrip().split()))
board = []
visited = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    visited.append([False for _ in range(m)])

queue = deque()
pictures = 0
max_width = 0
for x in range(n):
    for y in range(m):
        if board[x][y] and not visited[x][y]:
            queue.append((x, y))
            visited[x][y] = True
            width = 0
            while queue:
                cur_x, cur_y = queue.pop()
                width += 1
                for move in moves:
                    next_x, next_y = cur_x + move[0], cur_y + move[1]

                    if 0 <= next_x < n and 0 <= next_y < m and board[next_x][next_y] and not visited[next_x][next_y]:
                        queue.append((next_x, next_y))
                        visited[next_x][next_y] = True
            pictures += 1

            if width > max_width:
                max_width = width
print(pictures)
print(max_width)