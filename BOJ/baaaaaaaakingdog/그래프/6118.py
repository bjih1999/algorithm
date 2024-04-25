import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

adj = [[] for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    adj[a].append(b)
    adj[b].append(a)

queue = deque()

queue.append(1)
distance[1] = 0
while queue:
    cur = queue.popleft()

    for next in adj[cur]:
        if not distance[next] != -1:
            distance[next] = distance[cur]+1
            queue.append(next)

room_distance = max(distance[2:])
room = distance.index(room_distance)
count = distance.count(room_distance)

print(str(room) + ' ' + str(room_distance) + ' ' + str(count))