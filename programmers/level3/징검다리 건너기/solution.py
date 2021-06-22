# def is_decrese(bridge, k):
#     for i in range(1, k):
#         if bridge[i-1] - bridge[i] < 0:
#             return False
#     return True 

import numpy as np

def solution(stones, k):
    stones = np.array(stones)
    count = 200000001
    for i in range(len(stones)-k):
        if np.sum(stones[i:i+k] - stones[i]) < 1:
            if count > stones[i]:
                count = stones[i]
    
    return int(count)

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))