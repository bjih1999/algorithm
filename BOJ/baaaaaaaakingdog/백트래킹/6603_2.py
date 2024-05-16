import sys

k = 0
s = 0
result = [0 for _ in range(6)]
def dfs(depth, cur):
    global s, result
    if depth == 6:
        print(' '.join(list(map(str, result))))
        return
    
    for i in range(cur, k):
        result[depth] = s[i]
        dfs(depth+1, i+1)

question = []
while True:
    input = sys.stdin.readline().rstrip()
    if input == '0':
        break
    
    question.append(input)


for q in question:
    temp = list(map(int, q.split()))
    k = temp[0]
    s = temp[1:]
    dfs(0, 0)
    print('')
