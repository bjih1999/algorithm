def solution(brown, yellow):
    answer = []
    half = brown // 2

    for r in range(2, half):
        c = half - r
        if (r-1) * (c-1) == yellow:
            return [c+1, r+1]
    
    
    return answer