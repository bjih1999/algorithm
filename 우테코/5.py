def solution(rows, columns):
    board = []
    is_square = columns == rows
    visited_cnt = 0
    for r in range(rows):
        board.append([0] * columns)
    
    count = 1
    r = 0
    c = 0
    # print(board)
    while True:
        # print(r, c)
        if board[r][c] == 0:
            visited_cnt += 1
        board[r][c] = count
        
        if count % 2:
            c += 1
            if c == columns:
                c = 0
            
        else:
            r += 1
            if r == rows:
                r = 0
        count += 1
        
        if is_square and r == 0 and c == 0:
            break
        
        if (not is_square) and visited_cnt == columns * rows:
            break
    return board

print(solution(3, 4))
print(solution(3, 3))
print(solution(1000, 1000))
