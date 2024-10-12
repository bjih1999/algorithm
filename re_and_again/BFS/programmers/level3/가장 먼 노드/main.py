'''
BFS로 최단 거리 구하는 문제,

n = 20000이기 때문에
최악인 경우, fully connected 일때,
간선을 모두 탐색한다고 하면 n^2 이기 때문에 20000 ^ 2 < 10^9(1초) 이내이기 때문에 BFS가 가능했다.

순간 헷갈렸던 점은 BFS는 큐에 넣음과 동시에 visited 처리를 해야한다는 점이었다.
'''

from collections import deque

def solution(n, edge):
    visited = [-1 for _ in range(n+1)]
    visited[0] = 0
    adj = [[] for _ in range(n+1)]
    queue = deque()
    
    for start, end in edge:
        adj[start].append(end)
        adj[end].append(start)
    queue.append((1, 0))
    visited[1] = 0
    while queue:
        node, dist = queue.popleft()
        
        for next_node in adj[node]:
            if visited[next_node] == -1:
                queue.append((next_node, dist + 1))
                visited[next_node] = dist + 1
    
    max_dist = max(visited)
    answer = len(list(filter(lambda x:x == max_dist, visited)))
    return answer