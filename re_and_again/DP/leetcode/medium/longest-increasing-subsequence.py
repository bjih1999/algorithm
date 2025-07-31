'''
가장 긴 증가하는 subsequence의 길이 구하기

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

DP 풀이 가능

1. board[i] = i번째까지 가장 긴 subsequence의 길이
2. i를 1부터 n까지 순회
3. j를 i까지 순회하며 nums[i] 보다 작은 nums[j]인 j를 찾음
    3-1. nums[i] > nums[j] 인 경우, board[i]에 board[i]와 board[j] + 1 중 큰 값을 취함

4. board 중 가장 큰 값을 리턴

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        board = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    board[i] = max(board[i], board[j] + 1)

        return max(board)