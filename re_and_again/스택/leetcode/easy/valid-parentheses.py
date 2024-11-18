'''
올바른 괄호인지 찾기
1 <= s.length <= 104
O(n) 풀이
'''
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        queue = deque()
        parentheses = s

        for p in parentheses:
            if p == '(' or p == '{' or p == '[':
                queue.append(p)
            else:
                if p == ')' and (queue and queue[-1] != '('):
                    return False
                elif p == '}' and (queue and queue[-1] != '{'):
                    return False
                elif p == ']' and (queue and queue[-1] != '['):
                    return False
                elif not queue:
                    return False
                
                queue.pop()
        
        if queue:
            return False
        
        return True