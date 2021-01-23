'''
���� ����
n���� �� ���̿� �ٸ��� �Ǽ��ϴ� ���(costs)�� �־��� ��, �ּ��� ������� ��� ���� ���� ���� �����ϵ��� ���� �� �ʿ��� �ּ� ����� return �ϵ��� solution�� �ϼ��ϼ���.

�ٸ��� ���� �� �ǳʴ���, ������ ���� ������ ���� �����ϴٰ� ���ϴ�. ���� ��� A ���� B �� ���̿� �ٸ��� �ְ�, B ���� C �� ���̿� �ٸ��� ������ A ���� C ���� ���� ���� �����մϴ�.

���ѻ���

���� ���� n�� 1 �̻� 100 �����Դϴ�.
costs�� ���̴� ((n-1) * n) / 2�����Դϴ�.
������ i�� ����, costs[i][0] �� costs[i] [1]���� �ٸ��� ����Ǵ� �� ���� ��ȣ�� ����ְ�, costs[i] [2]���� �� �� ���� �����ϴ� �ٸ��� �Ǽ��� �� ��� ����Դϴ�.
���� ������ �� �� �־����� �ʽ��ϴ�. ���� ������ �ٲ���� ���� ����� ���ϴ�. �� 0�� 1 ���̸� �����ϴ� ����� �־����� ��, 1�� 0�� ����� �־����� �ʽ��ϴ�.
��� �� ������ �ٸ� �Ǽ� ����� �־����� �ʽ��ϴ�. �� ���, �� �� ������ �Ǽ��� �Ұ����� ������ ���ϴ�.
������ �� ���� ���� �־����� �ʽ��ϴ�.

����� ��

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4

����� �� ����

costs�� �׸����� ǥ���ϸ� ������ ������, �̶� �ʷϻ� ��η� �����ϴ� ���� ���� ���� ������� ��θ� ������ �� �ֵ��� ����� ����Դϴ�.

https://programmers.co.kr/learn/courses/30/lessons/42861
'''

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