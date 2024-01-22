import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

numbers = [i for i in range(1, n+1)]

results = list(combinations(numbers, m))

for r in results:
    print(' '.join(list(map(str, list(r)))))

