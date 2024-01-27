import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = sorted(numbers)

result = combinations(numbers, m)

for r in result:
    print(' '.join(list(map(str, r))))