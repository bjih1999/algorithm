import sys

board = [['.' for _ in range(12)] for _ in range(6)]

for i in range(11, -1, -1):
    row = list(sys.stdin.readline().rstrip())
    for j, r in enumerate(row):
        board[j][i] = r


print(board)