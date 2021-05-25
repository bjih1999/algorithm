import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

adjList = {}
notVisited = set(i for i in range(1, N+1))
for i in range(1, N+1):
    adjList[i] = set()

for _ in range(M):
    a, b =  list(map(int, sys.stdin.readline().rstrip().split()))
    adjList[a].add(b)
    adjList[b].add(a)

count = 0
queue = deque()
while len(notVisited) > 0:
    queue.append(min(notVisited))
    while len(queue) != 0:
        node = queue.popleft()
        if node in notVisited:
            notVisited.remove(node)
        for i in adjList[node]:
            if i in notVisited and i not in queue:
                queue.append(i)
    count += 1
print(count)