import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())
answer = []
id_set = [i for i in range(N+1)]
print(id_set)
for _ in range(N-1):
	parent, child = list(map(int, sys.stdin.readline().rstrip().split()))
	id_set[child] = parent


for i in range(Q):
	answer.append('no')
	parent, child = list(map(int, sys.stdin.readline().rstrip().split()))
	while id_set[child] != child:
		if id_set[child] == parent:
			answer[i] = 'yes'
			break
		child = id_set[child]
for A in answer:
	print(A)

	
