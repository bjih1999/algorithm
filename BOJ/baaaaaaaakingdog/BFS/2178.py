import sys
from collections import deque
from copy import deepcopy

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = []
cost = []
length = 0
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    cost.append([ -1 for _ in range(m)])
queue = deque()

cost[0][0] = 1

queue.append((0, 0))


while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        continue
    
    for move in moves:
        next_x, next_y = x + move[0], y + move[1]

        if 0 <= next_x < n and 0 <= next_y < m and board[next_x][next_y] and cost[next_x][next_y] < 0:
            cost[next_x][next_y] = cost[x][y] + 1
            queue.append((next_x, next_y))

print(cost[n-1][m-1])