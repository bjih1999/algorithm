import sys
from collections import deque
from types import coroutine

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().rstrip().split()))

answer = deque()

sortedX = enumerate(sorted(list(set(X))))
coordinate = {}

for pos, x in sortedX:
	coordinate[x] = pos

answers = []
for x in X:
	answers.append(coordinate[x])
print(' '.join(map(str, answers)))


