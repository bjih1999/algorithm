import sys

n = int(sys.stdin.readline().rstrip())

count = 0
for _ in range(n):
    stack = []
    word = sys.stdin.readline().rstrip()
    for w in word:
        if not stack:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    if not stack:
        count += 1

print(count)    