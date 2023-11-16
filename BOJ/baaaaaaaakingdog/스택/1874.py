import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

stack = []

arr = deque()
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

result = []
i = 1
possible = True
while arr:
    stack.append(i)
    result.append('+')
    i += 1
    # print(arr)
    # print(stack)
    while stack and arr and (stack[-1] == arr[0]):
        # print(arr)
        # print(stack)
        stack.pop()
        arr.popleft()
        result.append('-')

    if i > n:
        if stack or arr:
            possible = False
        break

if not possible:
    print('NO')
else:
    for res in result:
        print(res)
        
    
