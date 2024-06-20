from collections import deque

'''
처음에는 트리 구조의 특성을 살려서 어캐든 해보려고 했는데,
2 <= n <= 100, wires의 길이가 n-1 즉, 최대 99여서
완전 탐색이 가능했다.

전략망을 끊을 전선을 하나씩 돌아가며 잘라보고, 잘린 결과물을 BFS로 탐색하며 개수를 셌다.
그 중 가장 차이가 적은 답을 구했다.
'''
def solution(n, wires):
    result = []
    
    
    for cut in range(len(wires)):
        tree = [[] for _ in range(n+1)]
        visited = [False for _ in range(n+1)]
        for i, w in enumerate(wires):
            if i == cut:
                continue
            v1, v2, = w
            tree[v1].append(v2)
            tree[v2].append(v1)
        
        
        count_list = []
        for i in range(1, n+1):
            
            if visited[i]:
                continue
            
            queue = deque()
            queue.append(i)
            visited[i] = True
            count = 1
            while queue:
                cur = queue.popleft()
                
                for _next in tree[cur]:
                    if visited[_next]:
                        continue
                    queue.append(_next)
                    visited[_next] = True
                    count += 1
            count_list.append(count)
        
        result.append(abs(count_list[0] - count_list[1]))
    
    return min(result)