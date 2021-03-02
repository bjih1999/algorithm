'''
�Ǻ���ġ �Լ�
�ð� ����	�޸� ����	����	����	���� ���	���� ����
0.25 �� (�߰� �ð� ����)	128 MB	111477	28768	22632	30.012%

����
���� �ҽ��� N��° �Ǻ���ġ ���� ���ϴ� C++ �Լ��̴�.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n?1) + fibonacci(n?2);
    }
}

fibonacci(3)�� ȣ���ϸ� ������ ���� ���� �Ͼ��.

fibonacci(3)�� fibonacci(2)�� fibonacci(1) (ù ��° ȣ��)�� ȣ���Ѵ�.
fibonacci(2)�� fibonacci(1) (�� ��° ȣ��)�� fibonacci(0)�� ȣ���Ѵ�.
�� ��° ȣ���� fibonacci(1)�� 1�� ����ϰ� 1�� �����Ѵ�.
fibonacci(0)�� 0�� ����ϰ�, 0�� �����Ѵ�.
fibonacci(2)�� fibonacci(1)�� fibonacci(0)�� ����� ���, 1�� �����Ѵ�.
ù ��° ȣ���� fibonacci(1)�� 1�� ����ϰ�, 1�� �����Ѵ�.
fibonacci(3)�� fibonacci(2)�� fibonacci(1)�� ����� ���, 2�� �����Ѵ�.
1�� 2�� ��µǰ�, 0�� 1�� ��µȴ�. N�� �־����� ��, fibonacci(N)�� ȣ������ ��, 0�� 1�� ���� �� �� ��µǴ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� �׽�Ʈ ���̽��� ���� T�� �־�����.

�� �׽�Ʈ ���̽��� �� �ٷ� �̷���� �ְ�, N�� �־�����. N�� 40���� �۰ų� ���� �ڿ��� �Ǵ� 0�̴�.

���
�� �׽�Ʈ ���̽����� 0�� ��µǴ� Ƚ���� 1�� ��µǴ� Ƚ���� �������� �����ؼ� ����Ѵ�.

���� �Է� 1 
3
0
1
3
���� ��� 1 
1 0
0 1
1 2
'''

import sys

N = int(sys.stdin.readline().rstrip())

num_list = []
for i in range(N):
	num_list.append(int(sys.stdin.readline().rstrip()))

for num in num_list:
	zero_cnt = [1, 0]
	one_cnt = [0, 1]
	if num >= 2:
		for i in range(2, num+1):
			zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
			one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
		print(zero_cnt[-1], one_cnt[-1])
	else:
		print(zero_cnt[num], one_cnt[num])

