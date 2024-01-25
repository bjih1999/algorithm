import sys
from itertools import permutations

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = sorted(numbers)
result = list(permutations(numbers, m))

for r in result:
    print(' '.join(list(map(str, list(r)))))