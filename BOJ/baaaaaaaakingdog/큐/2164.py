import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque([i for i in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()
    cur = queue.popleft()
    queue.append(cur)

print(queue[0])