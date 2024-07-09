def solution(k, ranges):
    graph = []
    cur = k
    while cur != 1:
        graph.append(cur)
        if cur % 2 == 0:
            cur = cur // 2
        else:
            cur = cur * 3 + 1
    
    n = len(graph)
    graph.append(1)
    width = []
    for i in range(1, n+1):
        width.append(abs(graph[i]-graph[i-1]) / 2 + min(graph[i-1], graph[i])) 
    
    acuumulated_width = [0, width[0]]
    for w in width[1:]:
        acuumulated_width.append(acuumulated_width[-1] + w)
    
    answer = []
    for r in ranges:
        a, b = r
        b = n + b
        
        op = 1
        if a > b:
            answer.append(-1)
        else:
            answer.append(acuumulated_width[b] - acuumulated_width[a])
    
    return answer
        
    