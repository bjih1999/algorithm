import numpy as np

def dfs(y, x, prev, cost, board):
    global cur_dir
    
    directions = [(-1, 0, '1'), (1, 0, '1'), (0, -1, '-'), (0, 1, '-')]
    
    for dir in directions:
        if prev == dir[2]:
            if cost + 100 < board[y][x]:
                board[y][x] = cost + 100
        else:
            if cost + 600 < board[y][x]:
                board[y][x] = cost + 600
        dfs(y + dir[0], x + dir[1], dir[2], board[y][x], board)



def solution(board):
    cost = [[0 for _ in range(len(board[0]))] for _ in range(len(board))] 
    for i in range(len(board[0])):
        if board[i][0] == 1:
            board[i][0] = 9999999
    
    for j in range(len(board)):
        if board[0][j] == 1:
            board[0][j] = 9999999

    
    
    

    
    answer = 0
    return answer
