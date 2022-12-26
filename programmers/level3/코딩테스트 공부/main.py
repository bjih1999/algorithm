"""
메인 아이디어: DP

i: 알고력
j: 코딩력
board[i][j]: 알고력 i, 코딩력 j을 갖추기 위해 드는 최소의 시간

max_alp: 모든 문제를 풀기위해 길러야 하는 알고력 (알고력 최대값 - 초기 알고력)
max_cop: 모든 문제를 풀기위해 길러야 하는 코딩력 (코딩력 최대값 - 초기 코딩력)

1. 문제를 풀지않고 알고리즘 공부만으로 알고력, 코딩력을 길렀을 때 걸리는 시간으로 board를 초기화
2. 알고력 i, 코딩력이 j일 때, 풀 수 있는 문제를 체크하고 (i >= (alp_req - alp) and j >= (cop_req - cop))
   해당 문제를 풀었을 때 시간을 단축 시킬 수 있으면 board[i + alp_rwd][j + cop_rwd]에 문제의 cost를 더한 값을 대입
3. board[max_alp][max_cop]을 대입
"""
def solution(alp, cop, problems):    
    max_alp = max(max(list(map(lambda x: x[0],problems))) - alp, 0)
    max_cop = max(max(list(map(lambda x: x[1],problems))) - cop, 0)

    # 1
    board = [[0 for alp in range(max_cop + 1)] for _ in range(max_alp +1)]
    for i, row in enumerate(board):
        for j,col in enumerate(row):
            board[i][j] = i + j
    
    # 2
    for i, row in enumerate(board):
        for j,col in enumerate(row):
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                target_alp = min(max_alp, i + alp_rwd)
                target_cop = min(max_cop, j + cop_rwd)
                if i >= (alp_req - alp) and j >= (cop_req - cop):
                    board[target_alp][target_cop] = min(board[target_alp][target_cop], board[i][j] + cost)
    
    
    return board[-1][-1]