import sys
import heapq

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
	k = int(sys.stdin.readline().rstrip())
	maxq = []
	minq = []
	for _ in range(k):
		op, value = sys.stdin.readline().rstrip().split()
		value = int(value)
		if op == 'I':
			heapq.heappush(maxq, -value)
			heapq.heappush(minq, value)
		elif op == 'D' and value == -1:
			if len(minq) > 0:
				num = heapq.heappop(minq)
				maxq.remove(-num)
				heapq.heapify(maxq)
		elif op == 'D' and value == 1:
			if len(maxq) > 0:
				num = heapq.heappop(maxq)
				minq.remove(-num)
				heapq.heapify(minq)
		# print(maxq)
		# print(minq)
	if len(maxq) != 0 and len(minq) != 0:
		result.append(str(-1*heapq.heappop(maxq))+' '+str(heapq.heappop(minq)))
	else:
		result.append('EMPTY')

for answer in result:
	print(answer)