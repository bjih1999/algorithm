'''
prefix 곱과 suffix 곱을 활용한 문제
i를 제외한 모든 곱 = prefix[i-1] * suffix[i+1]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[len(nums) -1 - i])
        suffix = suffix[::-1]
        answer = [0] * len(nums)

        answer[0] = suffix[1]
        answer[-1] = prefix[-2]
        for i in range(1, len(nums)-1):
            answer[i] = prefix[i-1] * suffix[i+1]

        return answer
        