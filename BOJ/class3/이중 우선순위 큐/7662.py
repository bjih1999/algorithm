import sys
import heapq

def sync(q, visited):
	while q and visited[q[0][1]] == False:
		heapq.heappop(q)

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
	k = int(sys.stdin.readline().rstrip())
	minq = []
	maxq = []
	visited = [False] * 1000
	for id in range(k):
		op, value = sys.stdin.readline().rstrip().split()
		value = int(value)
		if op == 'I':
			heapq.heappush(minq, (value, id))
			heapq.heappush(maxq, (-1*value, id))
			visited[id] = True
		elif op == 'D' and value == -1:
			sync(minq, visited)
			if minq:
				visited[minq[0][1]] = False
				value, id = heapq.heappop(minq)
		elif op == 'D' and value == 1:
			sync(maxq, visited)
			if maxq:
				visited[maxq[0][1]] = False
				value, id = heapq.heappop(maxq)
	
	sync(maxq, visited)
	sync(minq, visited)
	if minq and maxq:
		result.append(str(-1*(heapq.heappop(maxq)[0]))+' '+str(heapq.heappop(minq)[0]))
	else:
		result.append('EMPTY')

for answer in result:
	print(answer)