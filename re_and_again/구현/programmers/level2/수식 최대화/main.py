from itertools import permutations
from collections import deque
import re

def solution(expression):
    answer = 0
    op_list = ['*', '+', '-']
    candidates = permutations(op_list)
    
    pattern = r'(\d*|\-|\*|\+)'
    p = re.compile(pattern)
    exp = list(filter(lambda x: x, p.findall(expression)))
    result = 0
    for candidate in candidates:
        first = { key:value for value, key in enumerate(candidate)}
        postpone = deque()
        op = deque()
        
        for e in exp:
            if e.isdigit():
                postpone.append(int(e))
            else:
                while op and first[op[-1]] <= first[e]:
                    temp = op.pop()
                    postpone.append(temp)
                op.append(e)
            
        while op:
            temp = op.pop()
            postpone.append(temp)
        
        num = deque()
        
        for e in postpone:
            if e not in ['-', '+', '*']:
                num.append(e)
            else:
                temp2 = num.pop()
                temp1 = num.pop()
                if e == '*':
                    num.append(temp1 * temp2)
                elif e == '+':
                    num.append(temp1 + temp2)
                elif e == '-':
                    num.append(temp1 - temp2)
        cur = num[0]
        result = max(result, abs(cur))
    return result