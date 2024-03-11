import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
board = []
queue = deque()
dist = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    dist.append([-1 for _ in range(m)])

queue.append((0, 0))
dist[0][0] = 1
broke = False

while queue:
    x, y = queue