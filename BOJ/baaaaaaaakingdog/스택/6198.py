import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
count = 0
stack = deque()

for _ in range(n):
    h = int(sys.stdin.readline().rstrip())

    while stack and stack[-1] <= h:
        stack.pop()
    
    count += len(stack)
    stack.append(h)

print(count)