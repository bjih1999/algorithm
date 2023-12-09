import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

q = deque([i for i in range(1, n+1)])

posistions = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
cur_size = n
for pos in posistions:
    cur_count = 0
    while q[0] != pos:
        q.append(q.popleft())
        cur_count += 1
    q.popleft()
    count += min(cur_count, cur_size - cur_count)
    cur_size -= 1
print(count)