import sys
from itertools import combinations

answer = []
while True:
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    if numbers == [0]:
        break
    
    k = numbers[0]
    s = numbers[1:]

    result = combinations(s, 6)

    for r in result:
        answer.append((' '.join(list(map(str, r)))))
    answer.append('')

for a in answer:
    print(a)
