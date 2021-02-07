import heapq

def solution(n, edge):
    answer = 0
    not_visited = [i for i in range(1, n+1)]
    adj_list = [{} for i in range(n+1)]
    distance = []
    
    not_visited.remove(1)

    # for index, path in enumerate(edge):
    #     edge[index] = sorted(path, key=lambda x:x)
    # sorted_edge = sorted(edge, key=lambda x:(x[0], x[1]))
    # print(sorted_edge)

    for i in range(1, n+1):
        adj_list[i][i] = 0
    for path in edge:
        adj_list[path[0]][path[1]] = 1
        adj_list[path[1]][path[0]] = 1
    
    distance = adj_list[1]
    # print('distance : ',distance)
    while len(not_visited) > 0:
        min_list = []
        # print('distance : ', distance)
        node_index = 0
        for node in not_visited:
            # print(node)
            # print('not_visited : ',not_visited)
            # print('distance : ', distance)
            if node in distance and distance[node] == min([distance[x] for x in distance if x in not_visited]):
                node_index = node
                break
        # print('---------------')
        # cur_visit = min_list[0]
        cur_visit = node_index
        not_visited.remove(cur_visit)
        for node in adj_list[cur_visit].keys():
            if node not in distance:
                distance[node] = distance[cur_visit] + adj_list[cur_visit][node]
        # print('distance : ',distance[1:])
    most_far_length = max(distance.values())
    # print(distance)
    # print(most_far_length)
    # print(distance.keys())
    for node in distance.keys():
        if most_far_length == distance[node]:
            answer += 1

    return answer

print(solution(6, 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))