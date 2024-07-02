moves = [(1, 0), (0, 1), (-1, -1)]
def solution(n):
    board = [[-1] * i for i in range(1, n + 1)]
    x, y = -1, 0
    count = 1
    m = 0
    
    for i in range(n, 0, -1):
        for _ in range(i):
            x = x + moves[m][0]
            y = y + moves[m][1]
            board[x][y] = count
            count += 1
        m += 1
        m %= len(moves)
    
    result = []
    for r in board:
        result.extend(r)
    return result