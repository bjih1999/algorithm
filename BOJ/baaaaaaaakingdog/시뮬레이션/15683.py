import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

count = 0
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for cam in range(1, 6, -1):
    for i in range(n):
        for j in range(m):
            if board[i][j] == cam:
                if cam == 5:
                    for i range(move):
