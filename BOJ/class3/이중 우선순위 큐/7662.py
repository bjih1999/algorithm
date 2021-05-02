import sys
import heapq

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
	k = int(sys.stdin.readline().rstrip())
	q = []
	for _ in range(k):
		op, value = sys.stdin.readline().rstrip().split()
		value = int(value)
		if op == 'I':
			heapq.heappush(q, value)
		elif op == 'D' and value == -1:
			if len(q) > 0:
				heapq.heappop(q)
		elif op == 'D' and value == 1:
			if len(q) > 0:
				q = heapq.nlargest(len(q), q)[1:]
				heapq.heapify(q)
		# print(q)
	# print(q)
	if len(q) != 0:
		result.append(str(heapq.nlargest(1, q)[0])+' '+str(heapq.heappop(q)))
	else:
		result.append('EMPTY')

for answer in result:
	print(answer)