import sys
from copy import deepcopy

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

def func(cur):
    if len(cur) == m:
        print(' '.join(map(str, cur)))
        return
    
    for i in range(1, n+1):
        if i not in cur:
            next = deepcopy(cur)
            next.append(i)
            func(next)

func([])
