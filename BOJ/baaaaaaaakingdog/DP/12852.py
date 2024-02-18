import sys

n = int(sys.stdin.readline().rstrip())
dp = [n-i for i in range(n+1)]
prev = [-1 for _ in range(n+1)]

for i in range(n,0, -1):
    if i + 1 >= n:
        dp[i] = 1
        prev[i] = i + 1
    else:
        candidate = []
        if i * 3 <= n:
            candidate.append((dp[i*3] + 1, i*3))
        elif i * 2 <= n:
            candidate.append((dp[i*2] + 1, i*2))
        else:
            candidate.append((dp[i+1] + 1, i+1))
    
        result = sorted(candidate, lambda x: min(x[0]))
        dp[i] = result[0][0]
        prev[i] = result[0][1]
         

# print(dp[1])
# print(dp)
result = [1]
i = 1
while i != n:
    result.append(prev[i])
    i = prev[i]

print(' '.join(list(map(str, result[::-1]))))