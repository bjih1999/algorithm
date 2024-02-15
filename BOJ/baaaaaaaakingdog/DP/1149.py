import sys

n = int(sys.stdin.readline().rstrip())

cost = []
for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = []
for _ in range(n):
    dp.append([1000] * 3)

dp[0] = cost[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))