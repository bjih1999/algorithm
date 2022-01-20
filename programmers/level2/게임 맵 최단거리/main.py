from copy import deepcopy

min_len = 100*100
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(maps):
    visited = deepcopy(maps)
    n = len(visited)
    m = len(visited[0])
    count = 0
    dfs(visited, 0, 0, n, m, count)
    
    answer = 0
    return min_len

def dfs(visited, r, c, n, m, count):
    if r == n and c == m:
        if count < min_len:
            min_len = count
        return
    visited = deepcopy(visited)
    for direction in directions:
        if 0 <= r - direction[0] < n and 0 <= c - direction[1] < m and visited[r - direction[0]][c - direction[1]] == 1:
            r = r - direction[0]
            c = c - direction[1]
            visited[r - direction[0]][c - direction[1]] = 0
            count += 1
            dfs(visited, r, c, n, m, count)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))