import sys
from collections import deque

while True:
    stack = deque()
    cols = list(map(int,sys.stdin.readline().rstrip().split()))

    ans = 0
    n = cols[0]
    if not n:
        break

    for index, col in enumerate(cols[1:]):
        idx = index
        while stack and stack[-1][0] >= col:
            ans = max(ans, stack[-1][0] * (index - stack[-1][1]))
            _, idx = stack.pop()
        
        stack.append((col, idx))

    while stack:
        ans = max(ans, stack[-1][0] * (n - stack[-1][1]))
        stack.pop()
    print(ans)


