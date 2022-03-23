def isCorrect(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '[' and ch == ']':
            stack.pop()
        elif stack[-1] == '(' and ch == ')':
            stack.pop()
        elif stack[-1] == '{' and ch == '}':
            stack.pop()
        else:
            stack.append(ch)
    
    return not stack
         

def solution(s):
    count = 0
    temp = s
    for i in range(len(temp)):
        temp = temp[1:] + temp[0]
        if isCorrect(temp):
            count += 1
    
    return count