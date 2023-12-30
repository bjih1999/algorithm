import sys
sys.setrecursionlimit(10**7)

def func(a, k, mod):
    if k == 1:
        return a % mod
    result = func(a, k // 2, mod)
    
    if not k % 2:
        return result * result % mod
    else:
        return result * result * a % mod

a, b, c = list(map(int, sys.stdin.readline().rstrip().split()))

print(func(a, b, c))