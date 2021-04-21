import sys
from collections import deque

def bfs(K, queue, visited):
	while len(queue):
		pos = queue.popleft()
		if pos + 1 <= K and visited[pos + 1] == -1:
			visited[pos+1] = visited[pos] + 1
			queue.append(pos + 1)
		if pos - 1 >= 0 and visited[pos - 1] == -1:
			visited[pos-1] = visited[pos] + 1
			queue.append(pos - 1)
		if pos * 2 <= K and visited[pos * 2] == -1:
			visited[pos*2] = visited[pos] + 1
			queue.append(pos * 2)

N, K = map(int, sys.stdin.readline().rstrip().split())
visited = [-1 for _ in range(K+1)]
queue = deque([N])
visited[N] = 0
if K < N:
	print(N-K)
else:
	bfs(K, queue, visited)
	# print(visited)
	print(visited[K])