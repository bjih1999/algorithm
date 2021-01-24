'''
���� ����
�յڸ� ����� �Ȱ��� ���ڿ��� �Ӹ����(palindrome)�̶�� �մϴ�.
���ڿ� s�� �־��� ��, s�� �κй��ڿ�(Substring)�� ���� �� �Ӹ������ ���̸� return �ϴ� solution �Լ��� �ϼ��� �ּ���.

�������, ���ڿ� s�� abcdcba�̸� 7�� return�ϰ� abacde�̸� 3�� return�մϴ�.

���ѻ���
���ڿ� s�� ���� : 2,500 ������ �ڿ���
���ڿ� s�� ���ĺ� �ҹ��ڷθ� ����

����� ��
s	answer
abcdcba	7
abacde	3

����� �� ����
����� �� #1
4��°�ڸ� 'd'�� �������� ���ڿ� s ��ü�� �Ӹ������ �ǹǷ� 7�� return�մϴ�.

����� �� #2
2��°�ڸ� 'b'�� �������� aba�� �Ӹ������ �ǹǷ� 3�� return�մϴ�.

https://programmers.co.kr/learn/courses/30/lessons/12904
'''

def solution(s):
	length = [1]
	for index in range(len(s)):
		if (index-1 >= 0) and (index+1 < len(s)) and (s[index-1] == s[index+1]):
			# print(letter)
			count = 1
			i = 1
			# print('@', index)
			while (index-i >= 0) and (index+i < len(s)) and (s[index-i] == s[index+i]):
				count += 2
				i += 1
			length.append(count)

		if (index+1 < len(s)) and (s[index] == s[index+1]):
			count = 2
			i = 1
			# print('~', index)
			while (index-i >= 0) and (index+1+i < len(s)) and (s[index-i] == s[index+1+i]):
				count += 2
				i += 1
			length.append(count)
	return max(length)