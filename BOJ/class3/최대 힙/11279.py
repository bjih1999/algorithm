import sys
import heapq

N = int(sys.stdin.readline().rstrip())
queue = []
answers = []
for _ in range(N):
	x = int(sys.stdin.readline().rstrip())
	if x == 0:
		if len(queue):
			answers.append(heapq.heappop(queue)[1])
		else:
			answers.append(0)
	else:
		heapq.heappush(queue, (-x, x))

for answer in answers:
	print(answer)
