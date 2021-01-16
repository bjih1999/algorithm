'''
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
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