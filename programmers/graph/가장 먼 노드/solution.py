'''
���� ����
n���� ��尡 �ִ� �׷����� �ֽ��ϴ�. �� ���� 1���� n���� ��ȣ�� �����ֽ��ϴ�. 1�� ��忡�� ���� �ָ� ������ ����� ������ ���Ϸ��� �մϴ�. ���� �ָ� ������ ���� �ִܰ�η� �̵����� �� ������ ������ ���� ���� ������ �ǹ��մϴ�.

����� ���� n, ������ ���� ������ ��� 2���� �迭 vertex�� �Ű������� �־��� ��, 1�� ���κ��� ���� �ָ� ������ ��尡 �� �������� return �ϵ��� solution �Լ��� �ۼ����ּ���.

���ѻ���
����� ���� n�� 2 �̻� 20,000 �����Դϴ�.
������ ������̸� �� 1�� �̻� 50,000�� ������ ������ �ֽ��ϴ�.
vertex �迭 �� �� [a, b]�� a�� ���� b�� ��� ���̿� ������ �ִٴ� �ǹ��Դϴ�.

����� ��
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

����� �� ����
������ �׷����� ǥ���ϸ� �Ʒ� �׸��� ����, 1�� ��忡�� ���� �ָ� ������ ���� 4,5,6�� ����Դϴ�.
'''
from queue import Queue

def solution(n, edge):
    visited = set()
    adj_list = [{} for i in range(n+1)]
    queue = Queue()
    queue.put((1, 0))
    visited.add(1)
    distances = {}

    for i in range(1, n+1):
        adj_list[i][i] = 0
    for path in edge:
        adj_list[path[0]][path[1]] = 1
        adj_list[path[1]][path[0]] = 1
    
    while queue.qsize() > 0:
        cur_node = queue.get()
        distances[cur_node[0]] = cur_node[1]
        adj_nodes = adj_list[cur_node[0]]
        for node in adj_nodes.keys():
            if node not in visited and node in adj_nodes.keys() and adj_nodes[node] == 1:
                queue.put((node, cur_node[1] + 1))
                visited.add(node)
    longest_distance = max(distances.values())
    return list(distances.values()).count(longest_distance)