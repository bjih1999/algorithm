'''
비트연산이지만 여러 테크닉이 필요했던 문제

result[i] = i번째 배열부터 가장 깞으면서도 가장 큰 값을 갖는 subarray의 길이 배열.

n == nums.length
1 <= n <= 10^5
0 <= nums[i] <= 10^9

1) 10^9은 최대 31비트임
2) nums를 거꾸로 순회하며 비트별로 마지막 1이 등장한 인덱스를 저장해둠
3) nums[i]의 특정 비트가 1인 경우 해당 비트가 1인 가장 작은 인덱스 값으로 bits[bit] = i로 저장해둠
    3-1) nums[i]의 특정 비트가 0인 경우 & 그리고 한번이라도 1이 나왔던 경우 이전에 해당 비트가 1인 인덱스를 기억함 => j. 이때 가장 큰 j를 기억함
4) 모든 비트를 순회한 후 result[i] = j(nums[i]가 가장 큰수가 되기 위해 필요한 가장 원소의 인덱스 중 가장 가까운 것) - i(현재 인덱스) + 1

'''

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        max_bit = 31
        result = [0] * n
        pos = [-1] * max_bit

        for i in range(n-1, -1, -1):
            j = i

            for bit in range(max_bit):
                if nums[i] & 1 << bit == 0:
                    if pos[bit] != -1:
                        j = max(pos[bit], j)
                else:
                    pos[bit] = i
            result[i] = j-i+1
        
        return result


        return result