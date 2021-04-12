import sys

n = int(sys.stdin.readline().rstrip())

dp_list = [0, 1, 2]
for i in range(3, n+1):
	dp_list.append(dp_list[i-1] + dp_list[i-2])

print(dp_list[n] % 10007)