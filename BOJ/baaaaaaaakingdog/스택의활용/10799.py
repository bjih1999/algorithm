import sys

pipes = sys.stdin.readline().rstrip()

stack = []
count = 0
n = len(pipes)
i = 0
while i < n:

    if pipes[i:i+2] == '()':
        count += len(stack)
        i += 1
    elif pipes[i] == '(':
        stack.append(pipes[i])
    elif pipes[i] == ')':
        stack.pop()
        count +=1
    i += 1
print(count)
