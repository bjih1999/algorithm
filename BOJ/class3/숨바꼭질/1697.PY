import sys
from queue import Queue
min_cnt = 0
def dfs(pos, K, cnt, visited):
	global min_cnt
	while 0 < pos < K:
		dfs(pos*2, K, cnt+1)
		dfs(pos+1, K, cnt+1)
		dfs(pos-1, K, cnt+1)
	if pos == K and cnt < min_cnt:
		min_cnt = cnt

N, K = map(int, sys.stdin.readline().rstrip().split())
visited = [False for _ in range(K)]

if K < N:
	print(N-K)
else:
	dfs(N, K, 0, visited)
	print(min_cnt)
	
