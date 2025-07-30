'''
배열 회전 시키기.
result 배열에 모듈러 연산을 통해 i+k %n <-> i 만큼 교환하여 저장

nums[i] = result[i] 복사

공간 복잡도가 O(n)이라 완전 inplace로 수정가능한지 찾아보고자함.

'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[(i + k) %n] = nums[i]
        
        for i in range(n):
            nums[i] = result[i]


        