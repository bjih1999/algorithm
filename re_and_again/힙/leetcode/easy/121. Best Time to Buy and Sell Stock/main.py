'''
배열로 주어지는 시간대별 주식 가격(prices) 를 보고
얻을 수 있는 가장 큰 차익을 계산하는 문제

0 < prices < 10 ** 5
0 < prices[i] < 10 ** 4


1. prices의 최대힙을 만들어두고, O(n log n)
2. prices를 순회하며, O(n)
    2.1 최대힙과 현재 price의 차를 비교 & 최대값 저장, O(1)
    2.2 price의 인덱스와 최대힙의 인덱스를 비교해서 최대힙의 인덱스가 작은 경우 최대힙의 인덱스가 더 커질때 까지 힙 삭제(이미 지난 시점의 데이터인 경우)

=> O(n log n)
'''
import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        future_prices = [(-v, v, i) for i, v in enumerate(prices)]
        heapq.heapify(future_prices)

        for i in range(len(prices)-1):
            
            while future_prices and i > future_prices[0][2]:
                heapq.heappop(future_prices)
            
            result = max(result, future_prices[0][1] - prices[i])
        
        return result
        