import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
radors = list(map(int, sys.stdin.readline().rstrip().split()))[::-1]

stack = deque()

result = [0 for _ in range(n+1)]

for (index, rador) in enumerate(radors):


    while stack and stack[-1][0] <= rador:
        r, i = stack.pop()
        result[i] = n - index
    stack.append((rador, n - index))

print(' '.join(list(map(str, result[1:]))))