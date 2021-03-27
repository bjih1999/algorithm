import sys

def dfs(x, K):
	right = abs(K - (x+1))
	left = abs(K - (x-1))
	multiply2 = abs(K - 2*x)
	shortest = min(right, left, multiply2)
	print(x)
	if shortest == right:
		x = x+1
	elif shortest == left:
		x = x-1
	elif shortest == multiply2:
		x = 2*x
	cnt += 1


N, K = map(int, sys.stdin.readline().rstrip().split())

x = N
cnt = 0

while x != K:
	
print(cnt)