'''
�Ҽ� ã�� 

�ð� ����	�޸� ����	����	����	���� ���	���� ����
2 ��	128 MB	65380	30792	25299	48.231%

����
�־��� �� N�� �߿��� �Ҽ��� �� ������ ã�Ƽ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù �ٿ� ���� ���� N�� �־�����. N�� 100�����̴�. �������� N���� ���� �־����µ� ���� 1,000 ������ �ڿ����̴�.

���
�־��� ���� �� �Ҽ��� ������ ����Ѵ�.

���� �Է� 1 
4
1 3 5 7

���� ��� 1 
3
'''

import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0

maximum = max(numbers)

prime_set = set([i for i in range(2, maximum+1)])
for i in range(2, maximum):
	if i in prime_set:
		prime_set -= set(range(2*i, maximum+1, i))

for number in numbers:
	if number in prime_set:
		answer += 1

print(answer)