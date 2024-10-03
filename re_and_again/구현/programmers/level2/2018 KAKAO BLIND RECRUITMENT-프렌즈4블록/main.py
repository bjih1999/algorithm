'''
2 <n, m <30 으로 브루트포스 구현문제

'''

moves = [(1, 0), (0, 1), (1, 1)]

# 터트릴수 있는 블록이 있는지 확인하는 함수
def checkPop(i, j, blocks):
    global moves
    target = blocks[i][j]
    if target == -1:
        return False
    
    for move in moves:
        if target != blocks[i + move[0]][j + move[1]]:
            return False
    
    return True


def solution(m, n, board):
    global moves
    
    # 가로 배열로 주어진 블록들을 세로 배열로 수정함
    blocks = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            blocks[i][j] = board[m-1-j][i]
    
    count = 0
    while True:
        pop = set()

        # 터트릴 블록이 있는지 확인하고 터트릴 블록 집합(set)에 추가
        for i in range(n-1):
            for j in range(m-1):
                if checkPop(i, j, blocks):
                    pop.add((i, j))
                    pop.add((i+1, j))
                    pop.add((i, j+1))
                    pop.add((i+1, j+1))
        
        # 더 이상 터트릴 블록이 없는 경우 종료
        if not pop:
            break
        
        # 터트릴 블록을 제외한 세로줄 배열을 만듦으로써 블록을 아래로 내리는 효과. 빈 공간은 -1로 채움
        for i in range(n):
            row = [-1 for _ in range(n)]
            index = 0
            for j in range(m):
                if (i, j) in pop:
                    # 제외된 (터트린) 블록 개수 count
                    count += 1
                    continue
                row[index] = blocks[i][j]
                index += 1
            blocks[i] = row
    return count