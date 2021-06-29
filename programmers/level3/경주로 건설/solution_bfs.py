from collections import deque
import math
from copy import deepcopy

def bfs(y, x, board, cost, N, before_cost, before_direction):
    directions = [(1, 0, 'col'), (-1, 0, 'col'), (0, -1, 'row'), (0, 1, 'row')]
    queue = deque()
    queue.append((y, x, before_cost, before_direction))
    
    while queue:
        y, x, before_cost, before_direction = queue.popleft()
        for direction in directions:
            if 0 <= y + direction[0] < N and 0 <= x + direction[1] < N and board[ y + direction[0]][x + direction[1]] != 1:
                if direction[2] == before_direction:
                    if cost[y + direction[0]][x + direction[1]] >= before_cost + 100:
                        cost[y + direction[0]][x + direction[1]] = before_cost + 100
                        queue.append((y + direction[0], x + direction[1], cost[y + direction[0]][x + direction[1]], direction[2]))
                elif before_direction == 'start':
                    cost[y + direction[0]][x + direction[1]] = before_cost + 100
                    queue.append((y + direction[0], x + direction[1], cost[y + direction[0]][x + direction[1]], direction[2]))
                else:
                    if cost[y + direction[0]][x + direction[1]] >= before_cost + 600:
                        cost[y + direction[0]][x + direction[1]] = before_cost + 600
                        queue.append((y + direction[0], x + direction[1], cost[y + direction[0]][x + direction[1]], direction[2]))

def solution(board):
    N = len(board)
    cost = [[math.inf for _ in range(N)] for _ in range(N)]
    cost[0][0] = 0

    bfs(0, 0, board, cost, N, 0, 'start')

    return cost[N-1][N-1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))