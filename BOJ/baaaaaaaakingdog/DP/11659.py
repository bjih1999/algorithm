import sys

numbers = [0]
n, m = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.extend(list(map(int, sys.stdin.readline().rstrip().split())))

# dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(i, n+1):
#         if i == j:
#             dp[i][j] = numbers[i]
#         else:
#             dp[i][j] = dp[i][j-1] + numbers[j]

# for _ in range(m):
#     i, j = list(map(int, sys.stdin.readline().rstrip().split()))
#     print(dp[i][j])
        
###################

dp = [0]

for i in range(1, n+1):
    dp.append(dp[i-1] + numbers[i])

for _ in range(m):
    i, j = list(map(int, sys.stdin.readline().rstrip().split()))
    print(dp[j] - dp[i-1])