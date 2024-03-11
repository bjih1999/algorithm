import sys
from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(sys.stdin.readline().rstrip())
queue1 = deque()
board1 = []
visited1 = []
count1 = 0

for _ in range(n):
    board1.append(list(sys.stdin.readline().rstrip()))
    visited1.append([False for _ in range(n)])

for x in range(n):
    for y in range(n):
        if visited1[x][y] == -1:
            queue1.append((x, y))
            visited1