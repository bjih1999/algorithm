answer = 0

def solution(info, edges):
    global answer
    n = len(info)
    max_case_count = ((2 ** n) + 1)
    adj = [set() for _ in range(n)]
    visited = [False] * max_case_count
    
    # 인접 리스트 만들기
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    
    # 방문한 노드의 상태를 숫자로 표현.
    # ex) 1 -> 0번 노드만 방문. 101 -> 5 -> 0, 2번 노드 방문
    def func(state):
        global answer
        
        # 이미 체크한 상태면 패스
        if visited[state]:
            return
        
        visited[state] = True
        
        visited_count = 0
        wolves = 0
        
        # 현재 방문한 노드들에서 양과 늑대의 개수를 셈
        for i in range(n):
            # 방문한 노드면 state & (1 << i)가 0이 아님
            # ex) 0, 4, 5번 노드 방문 -> 110001 -> 110001 & 1 = 1, 110001 & 1<<4 = 16
            if state & (1 << i):
                wolves += info[i]
                visited_count += 1
        
        # 방문한 노드에서 늑대의 개수를 셋을 때 과반수 이상이 늑대이면 패스
        if wolves * 2 >= visited_count:
            return
        
        # 양 최대값 갱신
        answer = max(answer, visited_count - wolves)
        
        # 다음 진행 노드 탐색
        for i in range(n):
            # 이미 방문한 노드는 패스
            if not state & (1 << i):
                continue
            
            # 방문하지 않는 노드 중에 여태 방문한 노드와 연결이 되어 있는 노드들을 state에 반영
            for _next in adj[i]:
                
                # _next 번째 노드를 탐색한다는 것을 state에 반영하기 위해 state | 1 << _next를 해줌
                func(state | 1 << _next)
    
    # 0번 노드부터 시작. 항상 0번 노드(루트)부터 시작하며 0번 노드는 항상 양이다.
    func(1)
    
    return answer