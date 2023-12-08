import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
stack = deque()
result = [-1 for _ in range(n)]
for index, value in enumerate(arr):

    while stack and stack[-1][1] < value:
        cur = stack.pop()
        result[cur[0]] = value
    
    stack.append((index, value))

print(' '.join(list(map(str, result))))

