from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(maps):
    answer = []
    board = []
    for m in maps:
        board.append(list(m))
    n = len(board)
    m = len(board[0])
    
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] != 'X':
                count = int(board[i][j])
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for move in moves:
                        nx, ny = x + move[0], y + move[1]
                        
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] != 'X':
                            visited[nx][ny] = True
                            count += int(board[nx][ny])
                            queue.append((nx, ny))
                answer.append(count)
    answer = sorted(answer)
    if not answer:
        return [-1]
    return answer