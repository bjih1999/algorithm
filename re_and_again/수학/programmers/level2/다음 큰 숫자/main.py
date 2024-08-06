'''
n 다음으로 크고 1의 개수가 같은 이진수 구하기
'''
def solution(n):
    MAX = 1000000
    answer = 0
    
    count = bin(n).count('1')
    
    for i in range(n+1, 1000000):
        cur_count = bin(i).count('1')
        if cur_count == count:
            return i
    return answer