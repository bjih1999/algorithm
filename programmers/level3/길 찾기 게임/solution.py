from copy import deepcopy
import numpy as np

def prefix(tree, index, min_level, max_level, sequence):
    # print(index)
    # print(tree[index])
    sequence[0].append(tree[index][2])
    if tree[index][1] == min_level:
        sequence[1].append(tree[index][2])
        tree[index] = -1
        # print('end')
        return
    
    if index*2 <= 2**max_level and tree[index*2] != -1:
        prefix(tree, index*2, min_level, max_level, sequence)
    if index*2 + 1 <= 2**max_level and tree[index*2 + 1] != -1:
        prefix(tree, index*2 + 1, min_level, max_level, sequence)

    if tree[index*2] == -1 and tree[index*2 + 1] == -1:
        # print('terminal')
        sequence[1].append(tree[index][2])
        tree[index] = -1
        return

def solution(nodeinfo):
    nodeinfo_with_num = []
    for i, node in enumerate(nodeinfo):
        node.append(i+1)
        nodeinfo_with_num.append(node)
    sorted_nodeinfo = sorted(nodeinfo_with_num, key=lambda x: (-x[1], x[0]))
    max_level = np.max(np.array(sorted_nodeinfo)[:, 1])-1
    min_level = np.min(np.array(sorted_nodeinfo)[:, 1])
    tree = [-1 for _ in range(2**max_level + 1)]

    for node in sorted_nodeinfo:
        current = 1
        while tree[current] != -1:
            if tree[current][0] < node[0]:
                current = current*2 + 1
            else:
                current = current*2
        tree[current] = node
    
    # print(tree)
    sequence = [[], []]
    prefix(tree, 1, min_level, max_level, sequence)
    return sequence

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))