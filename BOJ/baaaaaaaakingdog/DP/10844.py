import sys

n = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i+1][j] = dp[i][1]
        elif j == 9:
            dp[i+1][j] = dp[i][8]
        else:
            dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
    

sum = 0
for k in range(10):
    sum += dp[n][k]

print(sum % 1000000000)

