import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque()
MAX = 200002
dist = [-1 for _ in range(MAX)]

dist[N] = 0
queue.append(N)

while queue:
    pos = queue.popleft()
    nexts = []
    nexts.append(pos + 1)
    nexts.append(pos - 1)
    nexts.append(pos * 2)

    if pos == K:
        break

    for next in nexts:
        if 0 <= next < MAX and dist[next] < 0:
            dist[next] = dist[pos] + 1
            queue.append(next)
    
print(dist[K])