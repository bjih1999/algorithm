'''
board[i] = i를 만들기 위해 필요한 동전 수

0부터 coin을 하나씩 추가하며
board[i + coin] = max(board[i] + 1, board[i + coin])함.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        board = [2**31] * (amount + 1)
        board[0] = 0
        for i in range(amount):
            if board[i] == -1:
                continue
            
            for coin in coins:
                if i + coin > amount:
                    continue
                board[i + coin] = min(board[i] + 1, board[i+ coin])
        

        if board[amount] == 2**31:
            return -1
        return board[amount]

        