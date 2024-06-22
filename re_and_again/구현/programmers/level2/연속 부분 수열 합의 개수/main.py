def solution(elements):
    n = len(elements)
    board = []
    for i in range(n+1):
        board.append([0] * 2 * n)
    board[1] = elements * 2
    
    for i in range(2, n+1):
        for j in range(2*n - 1):
            board[i][j] = board[i-1][j] + board[i-1][j+1] - board[i-2][j+1]
    
    result = []
    for i in range(1, n+1):
        result += list(set(board[i][: -1 - (i-1)]))
    return len(set(result))