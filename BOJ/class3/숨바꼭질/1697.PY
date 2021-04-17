import sys
from queue import Queue

def use_teleport(pos, dest):
	if pos == 0:
		return -1
	
	teleport_cnt = 0
	while pos < dest:
		pos *= 2
		# print(pos)
		teleport_cnt += 1
		if pos == dest:
			return teleport_cnt
	return -1

N, K = map(int, sys.stdin.readline().rstrip().split())

if K < N:
	print(N-K)

time_to_reach = [-1 for _ in range(K+1)]

for pos in range(N, K+1):
	if time_to_reach[pos]

print(time_to_reach[K])
	
