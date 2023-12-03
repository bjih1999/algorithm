import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    arr = list(sys.stdin.readline().rstrip()[1:-1].split(','))
    if not arr[0]:
        arr = []
    arr = deque(arr)
    is_reverse = False
    is_error = False
    for op in p:
        if op == 'R':
            is_reverse = not is_reverse
        elif op == 'D':
            if not arr:
                is_error = True
                break
            if is_reverse:
                arr.pop()
            else:
                arr.popleft()

    if is_error:
        result.append('error')
    elif is_reverse:
        result.append(list(arr)[::-1])
    else:
        result.append(list(arr))

for r in result:
    if r != 'error':
        print('[' + ','.join(r) +']')
    else:
        print(r)