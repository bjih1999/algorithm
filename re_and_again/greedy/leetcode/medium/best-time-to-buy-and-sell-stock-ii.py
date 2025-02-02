'''
문제)
prices는 시점 당 주식 가격을 의미함. 최적의 이익을 계산해야함.

제약조건)
1 <= prices.length <= 3 * 10^4      -> O(n^2) 풀이까지 가능
0 <= prices[i] <= 10^4

풀이)
감소지점이 발생하기 전까지 가장 적은 가격을 저장하고 있다가, 감소 구간이 나오는 구간에서 최고가와 최저가의 합을 result에 계속 저장
마지막까지 상승만 할 경우를 대비하여 마지막 가격이 최저가보다 적을 경우 마지막 가격과 최저가의 차를 result에 추가함

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        n = len(prices)
        lowest = prices[0]

        for i in range(1, n):
            if prices[i-1] > prices[i]:
                result += max(0, (prices[i-1] - lowest))
                lowest = prices[i-1]
            lowest = min(lowest, prices[i])

        if lowest < prices[-1]:
            result += (prices[-1] - lowest)
        return result
