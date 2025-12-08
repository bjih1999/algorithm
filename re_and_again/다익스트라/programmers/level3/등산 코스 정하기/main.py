'''
다익스트라 알고리즘으로 품.

n(노드의 개수)이 50000이기 때문에 완전 탐색은 불가능

각 노드의 최소 intensity를 저장하는 intensities 배열을 사용.
다익스트라 알고리즘을 활용하여 gate별로 node의 intensity를 측정하고, 기존 intensity보다 적을 경우 queue에 넣어서 추가 탐색을 하게 함.
다익스트라 알고리즘을 활용함으로써 O(N^2) 이지만 가지치기를 통해 시간 복잡도를 통과할 수 있었음.
+) 우선순위 큐를 사용하면 더 줄일 수 있을 듯 하다.
현재 노드에서 방문하지 않은 가장 최단 거리의 노드를 탐색하는 다익스트라 알고리즘을 변형하여,

1. 현재 책정된 intensities[node] 보다 적은 intensity로 탐색 가능할 때 큐에 넣어서 탐색을 하도록한다.
2. 새로운 게이트에서 출발하면 intensity가 달라질 수 있기 때문에 gate 마다 intensity계산을 다시 한다.
3. 다음 노드의 intensity가 intensities[node] 보다 작을 경우 intensity를 갱신한다. 다음 node가 gate가 아니거나, summit이 아닌 경우 queue에 넣어서 추가 탐색을 하게 한다.
4. summit중 가장 intensity가 적은 summit을 고른다. 이 때 summit을 set으로 만들어 두었기에, 번호가 낮은순 정령이 되지 않을 수 있으니, summits를 정렬한 후 최소값을 찾는다.




(바보같이) 틀렸던 부분)
1. 최댓값이 10000000인데, 그대로 최댓값으로 초기화를 시켰다가 테스트 케이스 하나 틀림..
** 최댓값은 언제나 제시한 값보다 1이라도 크게!! **

2. 같은 intensity의 산봉우리가 있는 경우 낮은 번호의 산봉우리를 골라야하는데, 내가 빠른 포함관계 체크를 위해 summits를 set으로 변경해두었다.
당연히 그러니 순서가 보장되지 않는데, 이 채로 set를 순회하며 가장 intensity가 적은 산봉우리를 찾게 하였다.
당연히 순서를 보장하지 않으니 동일한 intensity가 있을 경우 가장 낮은 번호의 산봉우리가 골라지지 않는 경우도 생겨 특정 테스트 케이스가 실패했다.

** 사전식으로 정답을 리턴하는 문제는 꼭 정령이 되어 있는지 확인하자!! 특히 순회하는 리스트가 set인지 잘 확인하자!! **
'''
from collections import deque

def solution(n, paths, gates, summits):
    summits = set(summits)
    gates = set(gates)
    
    adj = [[] for _ in range(n+1)]
    for a, b, intensity in paths:
        adj[a].append((b, intensity))
        adj[b].append((a, intensity))
        
    intensities = [10000001] * (n+1)
    
    for gate in gates:
        queue = deque()
        queue.append((gate, 0))
        intensities[gate] = 0
        
        while queue:
            current, intensity = queue.popleft()
            
            for _next, _next_intensity in adj[current]:
                current_intensity = max(intensity, _next_intensity)
                if current_intensity < intensities[_next]:
                    intensities[_next] = current_intensity
                    
                    if _next not in gates and _next not in summits:
                        queue.append((_next, current_intensity))
    
    min_intensity = 10000001
    summit = -1
    for s in sorted(list(summits)):
        if intensities[s] < min_intensity:
            summit = s
            min_intensity = intensities[s]
    
    return [summit, min_intensity]