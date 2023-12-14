import sys

stack = []
string = sys.stdin.readline().rstrip()
n = len(string)

sum = 0
num = 1

for i, s in enumerate(string):
    if s == '(':
        num *= 2
        stack.append(s)
    elif s == '[':
        num *= 3
        stack.append(s)
    elif s == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit(0)
        else:
            if string[i-1] =='(':
                sum += num
            stack.pop()
            num /= 2
    else:
        if not stack or stack[-1] != '[':
            print(0)
            exit(0)
        else:
            if string[i-1] == '[':
                sum += num
            stack.pop()
            num /=3
    

if not stack:
    print(sum)
else:
    print(0)

        
    