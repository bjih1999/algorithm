'''
�� ã��
�ð� ����	�޸� ����	����	����	���� ���	���� ����
2 ��	128 MB	78657	24338	15975	30.220%

����
N���� ���� A[1], A[2], ��, A[N]�� �־��� ���� ��, �� �ȿ� X��� ������ �����ϴ��� �˾Ƴ��� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� �ڿ��� N(1 �� N �� 100,000)�� �־�����. ���� �ٿ��� N���� ���� A[1], A[2], ��, A[N]�� �־�����. ���� �ٿ��� M(1 �� M �� 100,000)�� �־�����. ���� �ٿ��� M���� ������ �־����µ�, �� ������ A�ȿ� �����ϴ��� �˾Ƴ��� �ȴ�. ��� ������ ������ -231 ���� ũ�ų� ���� 231���� �۴�.

���
M���� �ٿ� ���� ����Ѵ�. �����ϸ� 1��, �������� ������ 0�� ����Ѵ�.

���� �Է� 1 
5
4 1 5 2 3
5
1 3 7 9 5
���� ��� 1 
1
1
0
0
1
'''
import sys

N = int(sys.stdin.readline().rstrip())

src_list = list(set(map(int, sys.stdin.readline().rstrip().split())))

M = int(sys.stdin.readline().rstrip())

dest_list = list(map(int, sys.stdin.readline().rstrip().split()))

answers = []

sorted_src_list = sorted(src_list)

pos = 0
for num in dest_list:
	if num in sorted_src_list:
		answers.append(1)
	else:
		answers.append(0)
		
for answer in answers:
	print(answer)