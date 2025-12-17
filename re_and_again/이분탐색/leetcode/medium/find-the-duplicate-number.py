# 1번 풀이
# from collections import Counter
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         board = Counter(nums)

#         return list(filter(lambda x: x[1] >= 2, board.items()))[0][0]


# 2번
'''
중복된 숫자를 찾는 이분 탐색. O(n log n)

mid값 이하의 데이터의 개수가 mid보다 많다면, mid값 이하의 데이터에서 중복이 발생한 것.
정수 범위인 1 ~ n-1까지를 이분 탐색.
count > mid 인 경우, mid값 이하에서 중복이 발생한 것이기 때문에 right = mid
count <= mid 인 경우, mid값 초과에서 중복이 발생한 것이기 때문에 left = mid + 1

최종적 left 리턴
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        left = 1
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        return left