'''
단순 heap 문제
'''

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        heap = []
        n = len(costs)
        left = 0
        right = n - 1
        visited = [False] * n
        for _ in range(candidates):
            if not visited[left]:
                heapq.heappush(heap, (costs[left], left, 1))
                visited[left] = True
                left += 1
            if not visited[right]:
                heapq.heappush(heap, (costs[right], right, -1))
                visited[right] = True
                right -= 1

        answer = 0
        for _ in range(k):
            cost, index, lr = heapq.heappop(heap)
            answer += cost

            _next = left if lr == 1 else right
            
            if 0 <= _next < n and not visited[_next]:
                heapq.heappush(heap, (costs[_next], _next, lr))
                visited[_next] = True
                if lr == 1:
                    left += 1
                else:
                    right -= 1

        return answer