import sys
from collections import deque

n, m, v = list(map(int, sys.stdin.readline().rstrip().split()))
adj = [[] for _ in range(n+2)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    adj[a].append(b)
    adj[b].append(a)

for i in range(n):
    adj[i] = sorted(adj[i])


dfs_visited = [False for _ in range(n+2)]
dfs_answer = []

def dfs(cur):
    global adj, dfs_visited, dfs_answer
    dfs_visited[cur] = True
    dfs_answer.append(cur)

    for i in adj[cur]:
        if dfs_visited[i]:
            continue
        dfs(i)

def bfs(v):
    global adj
    answer = []
    visited = [False for _ in range(n+2)]

    queue = deque()

    queue.append(v)
    visited[v] = True
    while queue:
        cur = queue.popleft()
        answer.append(cur)
        for i in adj[cur]:
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True

    print(' '.join(list(map(str, answer))))

dfs(v)
print(' '.join(list(map(str, dfs_answer))))
bfs(v)