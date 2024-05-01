import sys

K, L = list(map(int, sys.stdin.readline().rstrip().split()))

board = {}
for i in range(L):
    id = sys.stdin.readline().rstrip()
    board[id] = i

result = list(sorted(board.items(), key=lambda x: x[1]))
answer = result[:K]

print('\n'.join(list(map(lambda x: x[0], answer))))