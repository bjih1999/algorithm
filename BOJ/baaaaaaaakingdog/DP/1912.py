import sys

n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(n)]
for i, num in enumerate(nums):
    if i == 0:
        dp[i] = num
        continue
    
    dp[i] = max(0, dp[i-1]) + num

print(max(dp))
    

