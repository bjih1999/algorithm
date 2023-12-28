import sys
from collections import deque

dist = [-1 for _ in range(1000002)]

f, s, g, u, d = list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque()
queue.append(s)
dist[s] = 0

while queue:
    pos = queue.popleft()
    if pos == g:
        print(dist[pos])
        exit(0)

    if 1 <= pos + u <= f and dist[pos + u] < 0:
        queue.append(pos + u)
        dist[pos + u] = dist[pos] + 1
    
    if 1 <= pos - d <= f and dist[pos - d] < 0:
        queue.append(pos - d)
        dist[pos - d] = dist[pos] + 1

print('use the stairs')