from copy import deepcopy

def dfs(visited, node_index, tree):
    visited = deepcopy(visited)
    visited.append(node_index)

    childs = [child for child in tree[node_index] if not in visited]




def solution(a, edges):
    if sum(a) != 0 :
        return -1
    elif sum(a) == 0:
        return 0

    N = len(a)
    tree = {}
    for i in range(N):
        tree[i] = []
    
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
            
    return