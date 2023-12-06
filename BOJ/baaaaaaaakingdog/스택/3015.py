import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
stack = deque()
count = 0

for _ in range(n):
    h = int(sys.stdin.readline().rstrip())
    if stack and stack[-1] < h:
        while stack and stack[-1] < h:
            stack.pop()
            count += 1
    
    count += len(stack)
    stack.append(h)
print(count)


    