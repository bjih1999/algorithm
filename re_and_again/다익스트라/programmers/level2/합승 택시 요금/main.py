from collections import deque
import heapq
MAX_COST = 999999


'''
다익스트라 알고리즘 사용.

3 <= n < 200 이라서 O(n^3) 풀이가 가능.
시작점에서 다익스트라 => O(v^2) v = n
각 노드를 순회 O(n)
    각 노드에서 다익스트라 => O(v^2) v = n
    즉, O(n^3)

1. 시작 점에서 다익스트라 알고리즘을 사용하여 각 노드의 최단 경로를 구함
2. 각 노드를 순회하며 해당 노드에서 시작하는 최단 경로를 구함.
3. 시작점~중간노드~A + 시작점~중간노드~B의 최소값을 구함

** 알아두어야 할 점**
다익스트라에서 우선순위 큐를 사용하면 시간 복잡도를 줄일 수 있음

** 개선해야할 점**
다익스트라에 대한 이해가 부족하였다. 다익스트라를 좀 더 잘 이해하도록 공부가 필요하다.
'''
def cal_cost(graph, start, n):
    global MAX_COST
    
    result = [MAX_COST] * (n+1)
    result[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, cur = heapq.heappop(heap)

        for cost, _next in graph[cur]:
            if result[cur] + cost < result[_next]:
                result[_next] = result[cur] + cost
                heapq.heappush(heap, (result[cur] + cost, _next))
    
    return result

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    
    for f in fares:
        c, d, cost = f
        heapq.heappush(graph[c], (cost, d))
        heapq.heappush(graph[d], (cost, c))
        
    result = cal_cost(graph, s, n)
    min_cost  = result[a] + result[b]

    for i in range(1, n+1):
        cur_result = cal_cost(graph, i, n)
        min_cost = min(min_cost, result[i] + cur_result[a] + cur_result[b])
        
    return min_cost
