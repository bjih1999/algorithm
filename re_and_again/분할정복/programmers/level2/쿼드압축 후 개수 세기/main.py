answer = {0:0, 1:0}
board = []
def check(r, c, k):
    global answer, board
    
    num = board[r][c]
    can_compress = True
    
    if k == 1:
        answer[num] += 1
        return
    
    for i in range(r, r+k):
        for j in range(c, c+k):
            if board[i][j] != num:
                can_compress = False
                break
        
        if not can_compress:
            break
    
    if can_compress:
        answer[num] += 1
        return
    
    next_k = k // 2
        
    check(r, c, next_k)
    check(r, c + next_k, next_k)
    check(r + next_k, c, next_k)
    check(r + next_k, c + next_k, next_k)

def solution(arr):
    global answer, board
    board = arr
    
    n = len(board)
    check(0, 0, n)
    return [answer[0], answer[1]]