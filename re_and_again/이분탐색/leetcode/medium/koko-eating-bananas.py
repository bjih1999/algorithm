import math
'''
특정 기준을 만족하는 최댓값을 이분 탐색 하기
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            duration = 0
            for p in piles:
                duration += math.ceil(p / mid)
            
            if duration > h:
                left = mid + 1
            else:
                right = mid
        
        return right
        