from collections import deque
def solution(land):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(land)
    m = len(land[0])
    result = 0
    zone = land
    zone_width = {0:0}
    
    for i in range(n):
        for j in range(m):
            if zone[i][j] == 1:
                zone[i][j] = -1
    
    zone_id = 1
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            width = 0
            if zone[i][j] == -1:
                width += 1
                zone[i][j] = zone_id
                queue.append((i, j))
            
            while queue:
                x, y = queue.popleft()
                for move in moves:
                    nx, ny = x + move[0], y + move[1]
                    if 0 <= nx < n and 0 <= ny < m and zone[nx][ny] == -1:
                        queue.append((nx, ny))
                        width += 1
                        zone[nx][ny] = zone_id
            
            zone_width[zone_id] = width
            zone_id += 1
    
    result = 0
    for j in range(m):
        passed = set()
        for i in range(n):
            passed.add(zone[i][j])
        
        print(passed)
        # current = sum(map(lambda x: zone_width[x], list(passed)))
        # result = max(result, current)
    
    return result

# print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]	))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]	))

# from collections import deque
# from copy import deepcopy
# n = 0
# m = 0
# amount = []
# board = []
# moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# def dfs(x, y, count):
#     global moves
    
#     for move in moves:
#         nx, ny = x + move[0], y + move[1]
        
#         if (0 <= nx < n and 0 <= ny < m) and amount[nx][ny] == -1:
#             max_count = dfs(nx, ny, count +1)
#             amount[nx][ny] = max_count
        
#     return count
                

# def solution(land):
#     global n, m, amount
#     result = 0
    
#     for i in range(n):
#         for j in range(m):
#             if land[i][j] == 1:
#                 amount[i][j] = -1
                
#     for i in range(n):
#         for j in range(m):
#             dfs(i, j, 0)
    
    
#     for j in range(m):
#         for i in range(n):
            
#     return result