import sys

string = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline().rstrip())

data = [-1 for _ in range(6000002)]
next = [-1 for _ in range(6000002)]
prev = [-1 for _ in range(6000002)]

index = 1
for s in string:
    data[index] = s
    prev[index] = index - 1
    next[index - 1] = index
    index += 1

cur = index - 1

for _ in range(M):
    move = sys.stdin.readline().rstrip().split()
    print('data', data[cur])
    if move[0] == 'L':
        if prev[cur] != -1:
            cur = prev[cur]
    
    if move[0] == 'D':
        if next[cur] != -1:
            cur = next[cur]
    if move[0] == 'B':
        if next[cur] == -1:
            next[prev[cur]] = next[cur]
        else:
            next[prev[cur]] = next[cur]
            prev[next[cur]] = prev[cur]
        
    if move[0] == 'P':
        data[index] = move[1]
        if next[cur] != -1:
            next[index] = next[cur]
            prev[index] = cur
            prev[next[cur]] = index
            next[cur] = index
        else:
            next[cur] = index
            prev[index] = cur
        cur = index
        index += 1
    
cursor = 0
print(data[:20])
print(next[:20])
print(prev[:20])
while next[cursor] != -1:
    print(data[next[cursor]])
    cursor = next[cursor]
        
        