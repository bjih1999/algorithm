'''
nums의 두 수를 골라 target을 만들 수 있는 수의 인덱스를 리턴하는 문제
2 <= nums <= 10**4

투 포인터를 활용해 O(n)으로 풀이 가능.
반드시 해가 1개 존재하기 때문에 예외처리 없이 풀이 가능.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        board = [(index, value) for index, value in enumerate(nums)]
        board = sorted(board, key=lambda x:x[1])
        l = 0
        r = len(board) - 1

        while l <= r:
            current = board[l][1] + board[r][1]
            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                return [board[l][0], board[r][0]]
        
