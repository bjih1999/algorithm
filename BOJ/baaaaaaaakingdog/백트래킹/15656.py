import sys
from itertools import product

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = list(map(int, list(sys.stdin.readline().rstrip().split())))
numbers = sorted(numbers)
result = product(numbers, repeat=m)

answer = []

for r in result:
    print(' '.join(list(map(str, r))))
    # answer.append(' '.join(list(map(str, r))))

# for a in answer:
#     print(a)