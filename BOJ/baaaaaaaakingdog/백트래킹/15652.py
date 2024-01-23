import sys
from itertools import combinations_with_replacement

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

numbers = [i for i in range(1, n+1)]

results = list(combinations_with_replacement(numbers, m))

for r in results:
    print(' '.join(list(map(str, list(r)))))

