import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(n+1)]
count = 0
visited = [False for _ in range(n+1)]


for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    adj[a].append(b)
    adj[b].append(a)

visited[1] = True

queue = deque()
queue.append((1, 0))
while queue:
    k, depth = queue.popleft()
    
    for i in adj[k]:
        if not visited[i] and depth < 2:
            count += 1
            visited[i] = True
            queue.append((i, depth + 1))
    

print(count)