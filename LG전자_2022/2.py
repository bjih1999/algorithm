import sys

n = int(sys.stdin.readline().rstrip())
mushrooms = list(map(int, sys.stdin.readline().rstrip().split()))

answer = []
ops = [1, -1]
def dfs(i, k, height):
    global answer, mushrooms, ops, n
    if i == n:
        answer.append(height)
        return
    
    # ate mushroom
    op = k % 2
    dfs(i+1, k+1, height + mushrooms[i] * ops[op])
    
    # did'nt eat mushroom
    dfs(i+1, k, height)

dfs(0, 0, 0)
print(max(answer))