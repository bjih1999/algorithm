from queue import Queue

def solution(n, edge):
    answer = 0
    not_visited = [i for i in range(1, n+1)]
    adj_list = [{} for i in range(n+1)]
    queue = Queue()
    queue.put((1, 0))
    not_visited.remove(1)

    for i in range(1, n+1):
        adj_list[i][i] = 0
    for path in edge:
        adj_list[path[0]][path[1]] = 1
        adj_list[path[1]][path[0]] = 1
    while queue.qsize() > 0:
        cur_node = queue.get()
        # print(not_visited)
        # print(cur_node)
        adj_nodes = adj_list[cur_node[0]]
        # print(adj_nodes)
        for node in not_visited:
            # print(node)
            if node in adj_nodes.keys() and adj_nodes[node] == 1:
                queue.put((node, cur_node[1] + 1))
                not_visited.remove(node)
        # print(queue.queue)
    return cur_node[1]

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))