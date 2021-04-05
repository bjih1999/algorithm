import sys
from queue import Queue

def bfs(box, M, N, q):
    cnt = 0
    while not q.empty():
        tomato = q.get()
        print(tomato)
        box[tomato[0]][tomato[1]] = 1
        cnt = tomato[2]
        if tomato[0] - 1 >= 0 and box[tomato[0]-1][tomato[1]] == 0:
            q.put(tomato[0] - 1, tomato[1], tomato[2]+1)
        if tomato[0] + 1 < M and box[tomato[0]+1][tomato[1]] == 0:
            q.put(tomato[0] + 1, tomato[1], tomato[2]+1)
        if tomato[1] - 1 >= 0  and box[tomato[0]][tomato[1]-1] == 0:
            q.put(tomato[0], tomato[1] - 1, tomato[2]+1)
        if tomato[1] + 1 < N and box[tomato[0]][tomato[1]+1] == 0:
            q.put(tomato[0] + 1, tomato[1], tomato[2]+1)
    return cnt

M, N = map(int, sys.stdin.readline().rstrip().split())
q = Queue()
box = []

for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.put((i, j, 0))

print(bfs(box, M, N, q))
    