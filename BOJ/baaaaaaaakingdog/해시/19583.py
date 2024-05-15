import datetime
import sys

s, e, q = sys.stdin.readline().rstrip().split()
s = datetime.datetime.strptime(s, '%H:%M')
e = datetime.datetime.strptime(e, '%H:%M')
q = datetime.datetime.strptime(q, '%H:%M')

board = {}

input = sys.stdin.read()
print(input)
for i in input:

    t, id = input.rstrip().split()

    t = datetime.datetime.strptime(t, '%H:%M')

    if t <= s:
        board[id] = 0
    if id in board.keys() and e <= t <= q:
        board[id] = 1

print(len(filter(lambda x: x == 1, board.values())))