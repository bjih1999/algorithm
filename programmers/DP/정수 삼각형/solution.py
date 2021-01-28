'''
���� ����

���� ���� �ﰢ���� ����⿡�� �ٴڱ��� �̾����� ��� ��, ���İ� ������ ���� ���� ū ��츦 ã�ƺ����� �մϴ�. �Ʒ� ĭ���� �̵��� ���� �밢�� �������� �� ĭ ������ �Ǵ� �������θ� �̵� �����մϴ�. ���� ��� 3������ �� �Ʒ�ĭ�� 8 �Ǵ� 1�θ� �̵��� �����մϴ�.

�ﰢ���� ������ ��� �迭 triangle�� �Ű������� �־��� ��, ���İ� ������ �ִ��� return �ϵ��� solution �Լ��� �ϼ��ϼ���.

���ѻ���
�ﰢ���� ���̴� 1 �̻� 500 �����Դϴ�.
�ﰢ���� �̷�� �ִ� ���ڴ� 0 �̻� 9,999 ������ �����Դϴ�.

����� ��
triangle	result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30

https://programmers.co.kr/learn/courses/30/lessons/43105
'''

def solution(triangle):
	answer_arr = []
	for depth, row in enumerate(triangle):
		row_max_value = []
		for pos, int_num in enumerate(row):
			if depth == 0:
				row_max_value.append(int_num)
			else:
				if pos == 0:
					row_max_value.append(answer_arr[depth-1][pos] + triangle[depth][pos])
				elif pos == len(row)-1:
					row_max_value.append(answer_arr[depth-1][pos-1] + triangle[depth][pos])
				else:
					row_max_value.append(max(answer_arr[depth-1][pos-1], answer_arr[depth-1][pos]) + triangle[depth][pos])
		answer_arr.append(row_max_value)
		
	return max(answer_arr[-1])