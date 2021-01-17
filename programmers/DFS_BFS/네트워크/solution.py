'''
��Ʈ��ũ�� ��ǻ�� ��ȣ ���� ������ ��ȯ�� �� �ֵ��� ����� ���¸� �ǹ��մϴ�. ���� ���, ��ǻ�� A�� ��ǻ�� B�� ���������� ����Ǿ��ְ�, ��ǻ�� B�� ��ǻ�� C�� ���������� ����Ǿ� ���� �� ��ǻ�� A�� ��ǻ�� C�� ���������� ����Ǿ� ������ ��ȯ�� �� �ֽ��ϴ�. ���� ��ǻ�� A, B, C�� ��� ���� ��Ʈ��ũ �� �ִٰ� �� �� �ֽ��ϴ�.

��ǻ���� ���� n, ���ῡ ���� ������ ��� 2���� �迭 computers�� �Ű������� �־��� ��, ��Ʈ��ũ�� ������ return �ϵ��� solution �Լ��� �ۼ��Ͻÿ�.

��ǻ���� ���� n�� 1 �̻� 200 ������ �ڿ����Դϴ�.
�� ��ǻ�ʹ� 0���� n-1�� ������ ǥ���մϴ�.
i�� ��ǻ�Ϳ� j�� ��ǻ�Ͱ� ����Ǿ� ������ computers[i][j]�� 1�� ǥ���մϴ�.
computer[i][i]�� �׻� 1�Դϴ�.
����� ��
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
'''

from queue import Queue

def solution(n, computers):
    answer = 0

    visited = set()
    queue = Queue()

    queue.put(0)

    for node_index in range(n):
        if node_index not in visited:
            visited.add(node_index)
            queue.put(node_index)
            while(queue.qsize() > 0):
                cur = queue.get()
                visited.add(cur)
                
                for i in range(n):
                    if (computers[cur][i] == 1) and (i not in visited):
                        visited.add(i)
                        queue.put(i) 
            
            answer += 1

    return answer

