import sys

n = int(sys.stdin.readline().rstrip())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, sys.stdin.readline().strip().split())))

answer = 0
current = 0
arr = [-1 for _ in range(n)]
def func(k):
    global answer, current
    if k == n:
        answer = max(answer, current)
        return
    
    if eggs[k][0] <= 0 or current == n-1:
        func(k + 1)
        return
    
    for i in range(0, n):
        if i == k or eggs[i][0] <= 0:
            continue

        eggs[k][0] -= eggs[i][1]
        eggs[i][0] -= eggs[k][1]

        if eggs[k][0] <= 0:
            current += 1    
        if eggs[i][0] <= 0:
            current += 1
        func(k + 1)
        if eggs[k][0] <= 0:
            current -= 1
        if eggs[i][0] <= 0:
            current -= 1
        
        eggs[k][0] += eggs[i][1]
        eggs[i][0] += eggs[k][1]
        
func(0)

print(answer)


