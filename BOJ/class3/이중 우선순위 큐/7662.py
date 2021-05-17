import sys
import heapq

T = int(sys.stdin.readline().rstrip())
result = []
id = 0
for _ in range(T):
	k = int(sys.stdin.readline().rstrip())
	minq = []
	maxq = []
	for _ in range(k):
		op, value = sys.stdin.readline().rstrip().split()
		value = int(value)
		if op == 'I':
			heapq.heappush(minq, (value, id))
			heapq.heappush(maxq, (-1*value, id))
			id += 1
		elif op == 'D' and value == -1:
			if len(minq) > 0:
				value, id = heapq.heappop(minq)
				maxq.remove((-1*value, id))
		elif op == 'D' and value == 1:
			if len(maxq) > 0:
				value, id = heapq.heappop(maxq)
				minq.remove((-1*value, id))
	if len(minq) != 0:
		result.append(str(-1*(heapq.heappop(maxq)[0]))+' '+str(heapq.heappop(minq)[0]))
	else:
		result.append('EMPTY')

for answer in result:
	print(answer)