'''
n���� ���� �ƴ� ������ �ֽ��ϴ�. �� ���� ������ ���ϰų� ���� Ÿ�� �ѹ��� ������� �մϴ�. ���� ��� [1, 1, 1, 1, 1]�� ���� 3�� ������� ���� �ټ� ����� �� �� �ֽ��ϴ�.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
����� �� �ִ� ���ڰ� ��� �迭 numbers, Ÿ�� �ѹ� target�� �Ű������� �־��� �� ���ڸ� ������ ���ϰ� ���� Ÿ�� �ѹ��� ����� ����� ���� return �ϵ��� solution �Լ��� �ۼ����ּ���.
https://programmers.co.kr/learn/courses/30/lessons/43165
'''

import copy

def search(numbers, index, target, answer):
    number_arr = copy.deepcopy(numbers)
    if index > len(number_arr)-2 :
        if sum(number_arr[:-1]) + number_arr[-1] == target:
            answer[0] += 1
        
        if sum(number_arr[:-1]) - number_arr[-1] == target:
            answer[0] += 1
        
        return
    else:
        search(number_arr, index + 1, target, answer)
        
        number_arr[index] *= -1
        search(number_arr, index + 1, target, answer)
        

def solution(numbers, target):
    answer = [0]
    search(numbers, 0, target, answer)

    return answer[0]