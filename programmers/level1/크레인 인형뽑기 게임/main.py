from collections import deque 

def solution(board, moves):
    basket = []
    answer = 0
    position = [deque() for _ in range(len(board[0]))]
    for row in board:
        for index, doll in enumerate(row):
            if doll != 0:
                position[index].append(doll)
    
    for move in moves:
        move = move - 1
        if position[move]:
            doll = position[move].popleft()
            if basket and doll == basket[-1]:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)
            
        else:
            basket.append(doll)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	, [1,5,3,5,1,2,1,4]	))