import sys

n = int(sys.stdin.readline().rstrip())

stairs = [0]
for _ in range(n):
    stairs.append(int(sys.stdin.readline().rstrip()))

dp = [[0 for _ in range(2)] for _ in range(n+1)]

dp[0][0] = 0
dp[0][1] = 0
dp[1][0] = stairs[1]
dp[1][1] = stairs[1]
for i in range(2, n+1):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
    dp[i][1] = dp[i-1][0] + stairs[i]


# for d in dp:
#     print(d)

print(max(dp[n][0], dp[n][1]))