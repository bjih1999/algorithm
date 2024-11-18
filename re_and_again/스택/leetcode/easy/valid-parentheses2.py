from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parentheses = s

        board = {'}': '{', ')': '(', ']':'['}

        for p in parentheses:
            if p in board:
                top = stack.pop() if stack else None

                if board[p] != top:
                    return False
            else:
                stack.append(p)

        return not stack