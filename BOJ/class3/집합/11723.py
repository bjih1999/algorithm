'''
����
 
�ð� ����	�޸� ����	����	����	���� ���	���� ����
1.5 ��	4 MB (�ϴ� ����)	31234	9632	6753	30.193%
����
����ִ� ������ S�� �־����� ��, �Ʒ� ������ �����ϴ� ���α׷��� �ۼ��Ͻÿ�.

add x: S�� x�� �߰��Ѵ�. (1 �� x �� 20) S�� x�� �̹� �ִ� ��쿡�� ������ �����Ѵ�.
remove x: S���� x�� �����Ѵ�. (1 �� x �� 20) S�� x�� ���� ��쿡�� ������ �����Ѵ�.
check x: S�� x�� ������ 1��, ������ 0�� ����Ѵ�. (1 �� x �� 20)
toggle x: S�� x�� ������ x�� �����ϰ�, ������ x�� �߰��Ѵ�. (1 �� x �� 20)
all: S�� {1, 2, ..., 20} ���� �ٲ۴�.
empty: S�� ���������� �ٲ۴�. 
�Է�
ù° �ٿ� �����ؾ� �ϴ� ������ �� M (1 �� M �� 3,000,000)�� �־�����.

��° �ٺ��� M���� �ٿ� �����ؾ� �ϴ� ������ �� �ٿ� �ϳ��� �־�����.

���
check ������ �־���������, ����� ����Ѵ�.

���� �Է� 1 
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
���� ��� 1 
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''

import sys
import math

M = int(sys.stdin.readline().rstrip())

S = set()
answers = ''
for _ in range(M):
	target_bit = 0
	instruction = sys.stdin.readline().rstrip().split()
	if len(instruction) > 1:
		value = int(instruction[1])

	if instruction[0] == 'add':
		S.add(value)
	elif instruction[0] == 'remove':
		S.discard(value)
	elif instruction[0] == 'check':
		if value in S:
			print(1)
		else:
			print(0)
	elif instruction[0] == 'toggle':
		if value in S:
			S.remove(value)
		else:
			S.add(value)
	elif instruction[0] == 'all':
		S = set(list(range(21)))
	elif instruction[0] == 'empty':
		S = set()