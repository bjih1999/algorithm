import sys
from itertools import product

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

numbers = [i for i in range(1, n+1)]

results = list(product(numbers, repeat = m))

for r in results:
    print(' '.join(list(map(str, list(r)))))

