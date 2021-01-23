'''
���� ����
���̽�ƽ���� ���ĺ� �̸��� �ϼ��ϼ���. �� ó���� A�θ� �̷���� �ֽ��ϴ�.
ex) �ϼ��ؾ� �ϴ� �̸��� �� ���ڸ� AAA, �� ���ڸ� AAAA

���̽�ƽ�� �� �������� �����̸� �Ʒ��� �����ϴ�.

�� - ���� ���ĺ�
�� - ���� ���ĺ� (A���� �Ʒ������� �̵��ϸ� Z��)
�� - Ŀ���� �������� �̵� (ù ��° ��ġ���� �������� �̵��ϸ� ������ ���ڿ� Ŀ��)
�� - Ŀ���� ���������� �̵�
���� ��� �Ʒ��� ������� JAZ�� ���� �� �ֽ��ϴ�.

- ù ��° ��ġ���� ���̽�ƽ�� ���� 9�� �����Ͽ� J�� �ϼ��մϴ�.
- ���̽�ƽ�� �������� 1�� �����Ͽ� Ŀ���� ������ ���� ��ġ�� �̵���ŵ�ϴ�.
- ������ ��ġ���� ���̽�ƽ�� �Ʒ��� 1�� �����Ͽ� Z�� �ϼ��մϴ�.
���� 11�� �̵����� "JAZ"�� ���� �� �ְ�, �̶��� �ּ� �̵��Դϴ�.
������� �ϴ� �̸� name�� �Ű������� �־��� ��, �̸��� ���� ���̽�ƽ ���� Ƚ���� �ּڰ��� return �ϵ��� solution �Լ��� ���弼��.

���� ����
name�� ���ĺ� �빮�ڷθ� �̷���� �ֽ��ϴ�.
name�� ���̴� 1 �̻� 20 �����Դϴ�.

����� ��
name	return
JEROEN	56
JAN	23

https://programmers.co.kr/learn/courses/30/lessons/42860
'''

def _move_vertical(pos, count, name):
    if((ord(name[pos]) - ord('A') <= 13)):
        count[0] += ord(name[pos]) - ord('A')
    else:
        count[0] += ord('Z') - ord(name[pos]) + 1


def _move_horizon(pos, count, visited, name):
    _move_vertical(pos, count, name)

    while visited.count(0) > 0:
        distances = []
        for index, value in enumerate(visited):
            if value == 0:
                distances.append((index ,min(abs(index - pos), abs(((pos+1) - (index+1)) + len(name)))))
        
        distances = sorted(distances, key=lambda x:x[1])
        visited[distances[0][0]] = 1
        pos = distances[0][0]
        count[0] += distances[0][1]

        _move_vertical(pos, count, name)
    

def solution(name):
    visited = [0 for x in range(len(name))]
    count = [0]
    answer = 0
    
    for x in range(len(name)):
        if name[x] == 'A':
            visited[x] = 1
    
    visited[0] = 1
    _move_horizon(0, count, visited, name)

    return count[0]