from math import sqrt, floor

def solution(k, d):
    answer = 0
    
    for i in range(0, d+1, k):
        max_y = int(floor(sqrt(d**2 - i**2)))
        div = max_y // k
        answer += (div + 1)
    return answer