import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()
result = []
for _ in range(n):
    inst = sys.stdin.readline().rstrip().split()
    op = inst[0]
    value = int(inst[1]) if len(inst) > 1 else 0
    if op == 'push':
        queue.append(int(value))
    elif op == 'pop':
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif op == 'size':
        result.append(len(queue))
    elif op == 'empty':
        if queue:
            result.append(0)
        else:
            result.append(1)
    elif op == 'front':
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)
    elif op == 'back':
        if queue:
            result.append(queue[-1])
        else:
            result.append(-1)

for r in result:
    print(r)