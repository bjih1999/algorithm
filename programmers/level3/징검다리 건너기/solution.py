def solution(stones, k):
    left = 1
    right = max(stones)
    mid = (left + right) // 2
    while left < right-1:
        count = len([stone for stone in stones if stone <= mid])
        print(count)
        
        if count <= k:
            left = mid
            mid = (left + right) // 2
            
        else:
            right = mid
            mid = (left + right) // 2
            
    return mid
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))