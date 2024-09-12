from collections import deque

_board = []
_move = [(0, -1), (-1, 0), (1, 0), (0, 1)]
_dest_x, _dest_y = -1, -1    
N = -1
M = -1
_visited = []

'''
BFS인데 이동로직만 좀 특이했던 케이스
상하좌우 로직만 슬라이딩으로 변경
'''
def slide(move, cur_x, cur_y):
    global _board, N, M
    x, y = cur_x, cur_y
    while True:
        nx, ny = x + move[0], y + move[1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or _board[nx][ny] == 'D':
            break
        x, y = nx, ny

    return x, y
    

def solution(board):
    global _board, N, M, _visited, _move, _dest_x, _dest_y
    
    visited = []
    x, y = -1, -1
    
    N = len(board)
    M = len(board[0])
    # visited 초기화 및 시작점 찾기
    for i in range(N):
        row = []
        for j in range(M):
            row.append(-1)
            if board[i][j] == 'R':
                x, y = i, j
            elif board[i][j] == 'G':
                _dest_x, _dest_y = i, j
        visited.append(row)
    _visited = visited
    _board = board
    
    # BFS
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        cur_x, cur_y = queue.popleft()
            
        for m in _move:
            nx, ny = slide(m, cur_x, cur_y)
            if visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cur_x][cur_y] + 1
    
    return visited[_dest_x][_dest_y]