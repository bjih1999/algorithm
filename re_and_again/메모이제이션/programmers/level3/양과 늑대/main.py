'''
최대 17개의 노드를 방문한 여부를 비트마스킹으로 표현
ex) 0, 1, 7, 8, 9를 방문했다 => 1110000011b => 899

1) 계산한 상태라는 것을 기억하기 위해 vis[state] = 1로 변경
이미 vis[state] == 1이면 계산하지 않음으로써 계산 횟수를 줄임

2) state의 비트 마스킹을 풀어서, 방문한 노드(1로 표현된 비트) 중,
  1. 늑대가 있는 노드의 개수와 방문한 노드를 비교하여, 절반 이상이 늑대인 경우이면 더 이상 계산을 하지 않음
  2. 양이 늑대보다 많은 경우 최대 양 개수(max_sheep)과 비교하여 max_sheep을 갱신

3) 최대 노드 개수 만큼 순회를 하며 방문한 노드에서 뻗어나갈 수 있는 자식 노드들을 state에 반영하고 재귀 호출을 함
    for _next in adj[i]:
        func(state | (1 << _next))

4) 초기 호출 func(1)을 함
    1은 초기 state로 0 0000 0000 0000 0001 즉, 0번 노드를 방문한 상태를 의미함

트리 혹은 그래프 탐색을 할때, 방문한 상태마다 방문 계획이 달라지는 경우.
상태를 비트마스킹으로 표현을 하고(ex. 노드 방문 여부를 0, 1로 표현한 비트마스킹 수)
visited[state]로 계산이 추가로 필요한지를 판단한 후 계산을 횟수를 줄일 수 있다.
방문 자체는 DFS, BFS를 알아서 사용하면 될듯 하다.

N이 충분히 작고, 백트래킹으로 풀기 어려운 경우 (유망하지 않았었는데 했는데 경우에 따라 유망할 수도 있는 경우가 발생)
1) 비트마스킹으로 상태를 저장하고, 2) BFS, DFS로 완전 탐색을 하고, 3) 메모이제이션으로 state별로 한번만 계산을 하게 하는 방법으로 풀 수 있음

ps. 피보나치 수열을 재귀-메모이제이션으로 푸는 방식과 같은 맥락
'''

max_sheep = 1
adj = [[] for _ in range(20)]
visited = [0] * (1<<17)
n = -1
board = []
temp = []
def func(state):
    global max_sheep, adj, visited, n, board, temp
    
    # 메모이제이션, 이미 계산을 완료한 상태는 계산을 하지 않음으로써, 계산 횟수를 줄임
    if visited[state]:
        return
    visited[state] = 1

    # 방문한 노드 개수의 절반 이상이 늑대인 경우를 거름
    #   항상 양 >= 늑대여야하기 때문    
    wolf, visited_count = 0, 0
    for i in range(n):
        if state & (1 << i):
            wolf += board[i]
            visited_count += 1
        
    if wolf * 2 >= visited_count:
        return
        

    # 양 >= 늑대인 경우 중 양이 가장 많은 경우 max_sheep을 갱신    
    max_sheep = max(max_sheep, visited_count - wolf)

    #다음 상태를 순회, 이미 방문한 노드의 자식을 순회
    for i in range(n):
        # 방문하지 않은 노드일 경우 패스
        if not state & (1 << i):
            continue
        
        # 방문한 노드들의 자식을 순회
        # state | << _next 연산으로 state에 _next 노드를 방문했다는 것을 반영함
        for _next in adj[i]:
            func(state | (1 << _next))

                
def solution(info, edges):
    global adj, n, max_sheep, board, temp
    
    # 1. 트리에 대한 인접 리스트를 만듦 
    board = info
    n = len(info)
    for v1, v2 in edges:
        adj[v1].append(v2)
    
    # 2. 1번 상태부터 시작
    #    상태 1 => 0 000 0000 0000 0001 즉, 0번 노드를 방문한 상태
    func(1)
    
    return max_sheep