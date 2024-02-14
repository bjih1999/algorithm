import sys

n = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(n)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(0, n):
    for j in range(0, i+1):
        if i == 0:
            dp[i][j] = board[i][j]

        else:
            if j == 0:
                dp[i][j] = dp[i-1][j] + board[i][j] 
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + board[i][j] 
            else:
                dp[i][j] = max(dp[i-1][j] + board[i][j], dp[i-1][j-1] + board[i][j])

print(max(dp[-1]))