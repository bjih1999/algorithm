'''
n의 체력과 k개의 무적권을 가지고 enemy 몇 라운드까지 버틸 수 있는지를 구하는 문제

1 ≤ enemy의 길이 ≤ 1,000,000 로 최대 O(n log n) 풀이가 가능

enemy를 순회하며 n을 원소만큼 깎는다. 이때 깎인 만큼을 최대 힙에 넣는다.
n < 0일 때 몇 스테이지에서 무적권을 사용하면 좋을지 확인한 후 무적권을 사용한다.
-> 이 말인 즉슨, k -=1 후, 최대 힙을 pop해서 가장 적이 많았던 스테이지를 무효화 하고 그 수 만큼 n을 회복한다.
이 것을 무적권이 없을때 까지 반복한다.
'''

import heapq

def solution(n, k, enemy):
    answer = 0
    hurts = [0 for _ in range(len(enemy))]
    heap = []
    round = 0
    for i, e in enumerate(enemy):
        n -= e
        heapq.heappush(heap, (-1 * e, e))
        if n < 0:
            k -= 1
            _, hurt = heapq.heappop(heap)
            n += hurt
        if k < 0:
            break
        
        round += 1
    return round