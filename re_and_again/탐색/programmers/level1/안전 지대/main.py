coverage = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
def solution(board):
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for c in coverage:
                    n_i, n_j = i + c[0], j + c[1]
                    if 0 <= n_i < n and 0 <= n_j < n and board[n_i][n_j] == 0:
                        board[n_i][n_j] = 2
    
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2 or board[i][j] == 1:
                count += 1
            
    
    return n * n - count