def solution(stones, k):
    left = 1
    right = max(stones)
    mid = (left + right) // 2
    if len(stones) == k:
        return right
    while left < right-1:
        count = 0
        possible = True
        for stone in stones:
            
            if stone < mid:
                count += 1
            else:
                count = 0
            
            if count == k:
                possible = False
                break
        
        if possible == True:
            left = mid
            mid = (left + right) // 2
            
        else:
            right = mid
            mid = (left + right) // 2
            
    return mid
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))