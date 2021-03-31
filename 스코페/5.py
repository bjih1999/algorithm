import sys
import copy
minimum = 99999999999
def dfs(screen, count, row, col, N, M, visited):
	global minimum
	visited = copy.deepcopy(visited)
	visited[col][row] = 1
	# print(col, row, count)
	if col == M-1:
		# print('-----------')
		if count < minimum:
			# print('@@', col, row, count)
			minimum = count
			return
	if col + 1 < M and screen[col+1][row] == '.' and visited[col+1][row] != 1:
		dfs(screen, count, row, col+1, N, M, visited)
	if row - 1 > -1 and screen[col][row-1] == '.'and visited[col][row-1] != 1:
		dfs(screen, count+1, row-1, col, N, M, visited)
	if row + 1 < N and screen[col][row+1] == '.'and visited[col][row+1] != 1:
		dfs(screen, count+1, row+1, col, N, M, visited)

N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))

screen = []
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(M):
	screen.append(list(sys.stdin.readline().rstrip()))
for j in range(N):
	if screen[0][j] == 'c':
		visited = copy.deepcopy(visited)
		visited[0][j] = 1
		dfs(screen, 0, j, 0, N, M, visited)

if minimum == 99999999999:
	print(-1)
else:
	print(minimum)