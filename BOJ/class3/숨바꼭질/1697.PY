import sys
from queue import Queue

N, K = map(int, sys.stdin.readline().rstrip().split())

now = N
field = [False for i in range(100001)]
q = Queue()
field[now] = 0
if now + 1 <= 100000:
	q.put(now + 1)
if now - 1 >= 0:
	q.put(now - 1)
if now*2 <= 100000:
	q.put(now * 2)
 
while not q.empty():
	pos = q.get()

	if pos == now - 1:
		if field[pos] == False:
			field[pos] = field[pos] - 1
	elif pos == now + 1:
		if field[pos] == False:
			field[pos] = field[pos] + 1
	else:
		if field[pos] == False:
			field[pos] = field[pos] * 2
	
	now = pos
	if now + 1 <= 100000:
		q.put(now + 1)
	if now - 1 >= 0:
		q.put(now - 1)
	if now*2 <= 100000:
		q.put(now * 2)

print(field[N])