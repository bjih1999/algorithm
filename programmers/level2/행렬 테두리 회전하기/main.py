def rotate(board, x1, y1, x2, y2):
    min = 10000
    for col in range(y2, y1, -1):
        temp = board[x1][col-1]
        board[x1][col-1] = board[x1][col]
        board[x1][col] = temp
        if min > board[x1][col-1]:
            min = board[x1][col-1]
        if min > board[x1][col]:
            min = board[x1][col]
    
    for row in range(x1 + 1, x2 + 1):
        temp = board[row-1][y1]
        board[row-1][y1] = board[row][y1]
        board[row][y1] = temp
        if min > board[row-1][y1]:
            min = board[row-1][y1]
        if min > board[row][y1]:
            min = board[row][y1]

    for col in range(y1 + 1, y2 + 1):
        temp = board[x2][col-1]
        board[x2][col-1] = board[x2][col]
        board[x2][col] = temp
        if min > board[x2][col-1]:
            min = board[x2][col-1]
        if min > board[x2][col]:
            min = board[x2][col]

    for row in range(x2, x1 + 1, -1):
        temp = board[row-1][y2]
        board[row-1][y2] = board[row][y2]
        board[row][y2] = temp
        if min > board[row-1][y2]:
            min = board[row-1][y2]
        if min > board[row][y2]:
            min = board[row][y2]

    return min
def solution(rows, columns, queries):
    board = []
    count = 1
    
    for _ in range(rows):
        row = []
        for __ in range(columns):
            row.append(count)
            count += 1
        board.append(row)
        
    
    answer = []
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(board, x1-1, y1-1, x2-1, y2-1))
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))