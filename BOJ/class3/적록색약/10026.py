import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
picture = []
que = deque()
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    picture.append(list(sys.stdin.readline().rstrip()))

area_cnt = 1
i = 0
while i < N:
    j = 0
    while j < N:
        if visited[i][j] == False:
            cur_color = picture[i][j]
            visited[i][j] = True
            que.append((i, j, area_cnt))
            while que:
                
                if 0 <= i-1 < N and picture[i-1][j] == cur_color:
                    que.append((i-1, j, area_cnt))
                    visited[i-1][j] = True
                if 0 <= i+1 < N and picture[i+1][j] == cur_color:
                    que.append((i+1, j, area_cnt))
                    visited[i+1][j] = True
                if 0 <= j-1 < N and picture[i][j-1] == cur_color:
                    que.append((i, j-1, area_cnt))
                    visited[i][j-1] = True
                if 0 <= j+1 < N and picture[i][j+1] == cur_color:
                    que.append((i, j+1, area_cnt))
                    visited[i][j+1] = True
                
            area_cnt += 1
        j += 1
        print(i, j)
    i += 1
print(area_cnt)
                