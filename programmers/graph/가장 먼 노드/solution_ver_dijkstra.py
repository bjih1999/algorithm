import heapq

def solution(n, edge):
    answer = 0
    not_visited = [i for i in range(1, n+1)]    # not_visited 초기화
    adj_list = [{} for i in range(n+1)]         # 인접리스트 생성
    distance = []
    
    not_visited.remove(1)

    for index, path in enumerate(edge):
        edge[index] = sorted(path, key=lambda x:x)
    sorted_edge = sorted(edge, key=lambda x:(x[0], x[1]))   # edge 정렬

    for i in range(1, n+1):
        adj_list[i][i] = 0
    for path in edge:
        adj_list[path[0]][path[1]] = 1
        adj_list[path[1]][path[0]] = 1      # 인접 리스트 초기화
    
    distance = adj_list[1]
    while len(not_visited) > 0:
        min_list = []
        for node in not_visited:
            if node in distance:
                heapq.heappush(min_list, (distance[node], node))    # 방문하지 않은 노드들을 거리와 함꼐 최소힙에 넣음ㅁ
        cur_visit = min_list[0]     # cur_visit = 가장 거리가 짧은 노드
        not_visited.remove(cur_visit[1])    

        for node in adj_list[cur_visit[1]].keys():
            if node not in distance:
                distance[node] = distance[cur_visit[1]] + adj_list[cur_visit[1]][node]  # 거리정보 갱신
    
    most_far_length = max(distance.values())    # 최대값 확인
    for node in distance.keys():
        if most_far_length == distance[node]:
            answer += 1                         # 최대값의 개수 확인

    return answer

print(solution(6, 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))