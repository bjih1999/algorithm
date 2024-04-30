import sys

n = int(sys.stdin.readline().rstrip())

board = {}
for _ in range(n):
    name, op = sys.stdin.readline().rstrip().split()

    board[name] = op


entering_people = dict(filter(lambda x: x[1] == 'enter', board.items()))

print('\n'.join(sorted(entering_people.keys())[::-1]))