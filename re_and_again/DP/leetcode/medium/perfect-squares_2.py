'''
n의 수를 제곱수로 나타내기 위해 필요한 최소의 수를 구하는 문제.
n < O(n^4), O(n^2) 풀이 가능.
0-1 knapsack 응용 풀이(DP)

모두 1*1로 채우는 경우로 초기화해두고,

무게를 1 <= i <= n까지 늘려가며,
1 < k^2 < i 인 k를 활용하여 가짓수를 줄일 수 있으면 dp[i] = min(dp[i], dp[i - k*k] + 1)로 사용한 숫자의 가짓수를 줄여 계산하는 방법
dp[i - k*k]에서 k*k을 추가하여 제곱수 하나를 더하여 i를 포현하는 방법


'''

import math

class Solution(object):
    def numSquares(self, n):
        board = [i for i in range(n+1)]
        board[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(math.sqrt(i)) + 1):
                board[i] = min(board[i-j*j] + 1, board[i])
        return board[n]