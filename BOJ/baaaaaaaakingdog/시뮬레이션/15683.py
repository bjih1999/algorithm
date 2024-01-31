import sys
from copy import deepcopy

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cctvs = []
board = []
cur_board = []
max_value = 0
cur_value = 0
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            cctvs.append((i, j))

def OOB(i, j):
    global n, m
    return i < 0 or i >= n or j < 0 or j >= m

def upd(i, j, dir):
    global cur_board, cur_value
    move = moves[dir % 4]
    ni, nj = i, j
    while True:
        ni, nj = ni + move[0], nj + move[1]
        
        if OOB(ni, nj) or cur_board[ni][nj] == 6:
            return
        elif 0 < cur_board[ni][nj] <= 5:
            continue

        if cur_board[ni][nj] == 0:
            cur_board[ni][nj] = 7
            cur_value += 1

for temp in range(1 << 2 * len(cctvs)):
    cur_value = 0
    cur_board = deepcopy(board)
    
    for i in range(n):
        for j in range(m):
            if 1 <= cur_board[i][j] <= 6:
                cur_value += 1
    
    cur_case = temp

    for cctv in cctvs:
        dir = cur_case % 4
        cur_case /= 4

        if board[cctv[0]][cctv[1]] == 1:
            upd(cctv[0], cctv[1], dir)
        
        elif board[cctv[0]][cctv[1]] == 2:
            upd(cctv[0], cctv[1], dir)
            upd(cctv[0], cctv[1], dir + 2)
        
        elif board[cctv[0]][cctv[1]] == 3:
            upd(cctv[0], cctv[1], dir)
            upd(cctv[0], cctv[1], dir + 1)

        elif board[cctv[0]][cctv[1]] == 4:
            upd(cctv[0], cctv[1], dir)
            upd(cctv[0], cctv[1], dir + 1)
            upd(cctv[0], cctv[1], dir + 2)
        
        elif board[cctv[0]][cctv[1]] == 5:
            upd(cctv[0], cctv[1], dir)
            upd(cctv[0], cctv[1], dir + 1)
            upd(cctv[0], cctv[1], dir + 2)
            upd(cctv[0], cctv[1], dir + 3)

        
        max_value = max(max_value, cur_value)
print(n*m - max_value)
            

