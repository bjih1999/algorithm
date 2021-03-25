'''
�躸��

�ð� ����	�޸� ����	����	����	���� ���	���� ����
2 ��	256 MB	25705	10430	7499	39.692%

����
�������� �赵 ���� ����� ��ܰ�, ���� ���� ����� ����� �־��� ��, �赵 ���� ���� ����� ����� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� �赵 ���� ����� �� N, ���� ���� ����� �� M�� �־�����. �̾ ��° �ٺ��� N���� �ٿ� ���� �赵 ���� ����� �̸���, N+2° �ٺ��� ���� ���� ����� �̸��� ������� �־�����. �̸��� ���� ���� ���� �ҹ��ڷθ� �̷������, �� ���̴� 20 �����̴�. N, M�� 500,000 ������ �ڿ����̴�.

 

�赵 ���� ����� ��ܿ��� �ߺ��Ǵ� �̸��� ������, ���� ���� ����� ��ܵ� ���������̴�.

���
�躸���� ���� �� ����� ���������� ����Ѵ�.

���� �Է� 1 
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

���� ��� 1 
2
baesangwook
ohhenrie
'''

import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

heardx = []
sawx = []

for _ in range(N):
	heardx.append(sys.stdin.readline().rstrip())

for _ in range(M):
	sawx.append(sys.stdin.readline().rstrip())

heardx = sorted(heardx)
sawx = sorted(sawx)

i = 0
j = 0
heard_saw_x = []
count = 0
while i < len(heardx) and j < len(sawx):
	if heardx[i] < sawx[j]:
		i += 1
	elif heardx[i] > sawx[j]:
		j += 1
	else:
		heard_saw_x.append(heardx[i])
		i += 1
		j += 1
		count += 1

print(count)
for name in heard_saw_x:
	print(name)