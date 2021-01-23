def _find(node, set_table):
    index = node
    while(set_table[index] != index):
        index = set_table[index]
    return index


def _union(node1, node2, set_table):
    root1 = _find(node1, set_table)
    root2 = _find(node2, set_table)
    set_table[root2] = root1


def solution(n, costs):

    total_cost = 0
    set_table = [x for x in range(n)]
    sorted_cost = sorted(costs, key=lambda x: x[2])

    for bridge in sorted_cost:
        if _find(bridge[0], set_table) != _find(bridge[1], set_table):
            _union(bridge[0], bridge[1], set_table)
            total_cost += bridge[2]
    return total_cost