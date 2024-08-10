'''
A: A팀 숫자 배열
B: B팀 숫자 배열

A팀의 배열이 주어질 때 B팀이 얻을 수 있는 최대의 승 수 구하기

A, B 배열을 각각 정렬 한 후

a[i] > b[j] 일때만 answer를 증가시키고, i, j를 1씩 증가시킨다.
a[i] <= b[j] 일때에는 j만 증가시킴으로써, b팀이 숫자를 높여 점수를 획득할 수 있는 경우인지 확인한다.

'''
def solution(A, B):
    answer = 0
    a = sorted(A)
    b = sorted(B)

    n = len(a)
    
    i = 0
    j = 0
    while j < n:
        if a[i] < b[j]:
            i += 1
            j += 1
            answer += 1
        else:
            j += 1
    
    return answer