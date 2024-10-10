import sys
from copy import deepcopy

def dfs(current, n, m):
    if len(current) == m:
        print(' '.join(list(map(str, current))))
        return
    
    for i in range(1, n+1):
        if i not in result:
            next = deepcopy(result)
            next.append(i)
            dfs(nest, n, m)

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

dfs([], n, m)