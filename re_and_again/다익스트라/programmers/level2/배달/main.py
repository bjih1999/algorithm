from collections import deque

def solution(N, road, K):
    answer = 0
    board = [[999999 for _ in range(N)]for _ in range(N)]
    visited = [False for _ in range(N)]
    for r in road:
        a, b, d = r
        board[a-1][b-1] = min(board[a-1][b-1], d)
        board[b-1][a-1] = min(board[b-1][a-1], d)
    
    result = board[0][:]
    result[0] = 0
    visited[0] = True
    
    for i in range(N):
        
        # 방문하지 않은 가장 가까운 노드 고르기
        min_node = -1
        _min = 999999
        for j in range(N):
            if not visited[j] and result[j] < _min:
                _min = result[j]
                min_node = j
        
        # 가장 가까운 노드를 통해서 도달할 수 있는 노드들의 거리와
        # 여태까지의 거리의 최소값을 비교하여 업데이트
        visited[min_node] = True

        for index, _next in enumerate(board[min_node]):
            if not visited[index]:
                result[index] = min(result[index], result[min_node] + _next)

    return len(list(filter(lambda x: x <= K, result)))