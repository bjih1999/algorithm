# def solution(targets):
#     answer = 0

#     boundaries = []
    
#     sorted_targets = sorted(targets, key=lambda x: x[1] - x[0])
#     for target_x1, target_x2 in sorted_targets:
#         need_more = True
#         for index, (x1, x2) in enumerate(boundaries):
#             if (x1 <= target_x1 < x2) or (x1 < target_x2 <= x2) :
#                 boundaries[index][0] = max(x1, target_x1)
#                 boundaries[index][1] = min(x2, target_x2)
#                 need_more = False
#                 break
#             elif target_x1 <= x1 and x2 <= target_x2:
#                 need_more = False
        
#         if need_more:
#             answer += 1
#             boundaries.append([target_x1, target_x2])
#     return answer
#  1 try

# def solution(targets):
#     answer = 0

#     board = [0 for _ in range(0, max(sum(targets, [])))]

#     for x1, x2 in targets:
#         if sum(board[x1:x2]) == 0:
#             answer += 1
#             board[x1:x2] = [1 for _ in range(x2 - x1)]
#     return answer
# 2 try

def solution(targets):
    answer = 0
    start = 0
    end = 0

    for x1, x2 in sorted(targets):
        if end <= x1:
            start = x1
            end = x2
            answer += 1
        else:
            end = min(end, x2)
    return answer


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))

print(solution([[0,1],[1,2],[2,3]]))