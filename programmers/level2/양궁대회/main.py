'''
메인 아이디어: 완전 탐색

라이언이 점수를 효율적으로 따기 위해 고려해야할 경우의 수 = 점수별로 어피치보다 하나를 더 많이 쏘거나, 아예 0개를 쏜다
즉, 점수당 어피치보다 1개 더 많이 쏘거나 0개를 쏘거나 점수당 2개의 경우의 수 밖에 없음
점수는 0~10점까지 있기 때문에 점수당 2가지 경우의 수를 모두 고려해도 2*11 = 2048개의 경우의 수 밖에 없기 때문에 매우 완전 탐색으로 해봄직 함
모든 경우의 수 중 총 화살의 개수가 n개 인 것 중 어피치와 점수차이가 가장 많이 나고 가장 적은 점수를 많이 맞힌 경우를 비교하며 최종 값을 찾아냄
이 때, 한가지 경우의 수가 추가되는 것이 남은 화살을 모두 써도 점수를 더 딸 수 없을 경우 남은 화살을 모두 0점에다가 쏘는 방법이 있음 -> 가장 적은 점수를 더 많이 맞추도록
'''

BOARD_LENGTH = 11

max_gap = 0
min_point = 11
min_point_count = 10
result = [-1]
def getScore(appeach, ryon):
    appeach_score = 0
    ryon_score = 0
    length = 10
    for i in range(length + 1):
        if appeach[i] == 0 and ryon[i] == 0:
            continue
        if appeach[i] >= ryon[i]:
            appeach_score += length - i
        else:
            ryon_score += length - i
    return appeach_score, ryon_score

def getMinPoint(board):
    for index, point in enumerate(reversed(board)):
        if point != 0:
            return index
    return 10

def dfs(n, appeach, ryon, position):
    # print(ryon)
    global result
    global max_gap
    global min_point
    global min_point_count
    # print(ryon)
    if len(ryon) == BOARD_LENGTH:
        if sum(ryon) == n:
            # print(ryon)
            appeach_score, ryon_score = getScore(appeach, ryon)
            # print(max_gap, appeach_score, ryon_score)
            if ryon_score > appeach_score and max_gap <= ryon_score - appeach_score:
                if (max_gap == ryon_score - appeach_score) and (getMinPoint(ryon) >= min_point) and ryon[getMinPoint(ryon)] <= min_point_count:
                    return
                result = ryon
                max_gap = ryon_score - appeach_score
                min_point = getMinPoint(ryon)
        return
    dfs(n, appeach, ryon + [0], position + 1)
    dfs(n, appeach, ryon + [appeach[position] +1], position + 1)
    if len(ryon) == BOARD_LENGTH - 1 and (n - sum(ryon)) > 0:
        dfs(n, appeach, ryon + [n - sum(ryon)], position + 1)
    

def solution(n, info):
    
    dfs(n, info, [], 0)
    return result

# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))