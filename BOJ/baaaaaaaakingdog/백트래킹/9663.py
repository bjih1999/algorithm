import sys
from copy import deepcopy

n = int(sys.stdin.readline().rstrip())
answer = 0

is_used1 = [False for _ in range(n)]
is_used2 = [False for _ in range(2*n -1)]
is_used3 = [False for _ in range(2*n -1)]


def func(k):
    global answer
    if k == n:
        answer += 1
        return
    
    for i in range(n):
        if is_used1[i] or is_used2[i + k] or is_used3[i - k + n -1]:
            continue
        is_used1[i] = True
        is_used2[i + k] = True
        is_used3[i - k + n - 1] = True
        func(k + 1)
        is_used1[i] = False
        is_used2[i + k] = False
        is_used3[i - k + n - 1] = False 
            
func(0)
print(answer)