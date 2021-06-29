from collections import deque
import math
from copy import deepcopy

def dfs(y, x, board, cost, N, before_cost, before_direction):
    directions = [(1, 0, 'col'), (-1, 0, 'col'), (0, -1, 'row'), (0, 1, 'row')]
    board = deepcopy(board)
    board[y][x] = 1
    if y == N-1 and x == N-1:
        return
    for direction in directions:
        if 0 <= y + direction[0] < N and 0 <= x + direction[1] < N and board[y + direction[0]][x + direction[1]] != 1:
            if direction[2] == before_direction:
                if cost[y + direction[0]][x + direction[1]] >= before_cost + 100:
                    cost[y + direction[0]][x + direction[1]] = before_cost + 100
                else:
                    return
            elif before_direction == 'start':
                cost[y + direction[0]][x + direction[1]] = before_cost + 100
            else:    
                if cost[y + direction[0]][x + direction[1]] >= before_cost + 600:
                    cost[y + direction[0]][x + direction[1]] = before_cost + 600
                else:
                    return
            dfs(y + direction[0], x + direction[1], board, cost, N, cost[y + direction[0]][x + direction[1]], direction[2])

def solution(board):
    N = len(board)
    cost = [[math.inf for _ in range(N)] for _ in range(N)]
    cost[0][0] = 0

    dfs(0, 0, board, cost, N, 0, 'start')

    return cost[N-1][N-1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))