'''
n = 10,000 이기 때문에, O(n^2) 풀이 불가

시그마의 성질을 사용하여 연속되는 정수의 합이 n과 같아지는지를 확인
'연속하는 정수'이기 때문에, 모든 경우의 수를 확인할 필요는 없음 -> 투 포인터를 활용

board[i] = sum(0,i) 인 board를 생성

투 포인터 l, r를 사용하여 

board[l] - board[r] == n 인 경우의 수를 체크 & 다음 케이스를 확인하기 위해 r += 1, l += 1
board[l] - board[r] < n 인 경우 l += 1
board[l] - board[r] > n 인 경우 r += 1

l <= n 일때까지 반복.
'''

def sigma(a, n):
    return n * (2*a + (n-1)) / 2

def solution(n):
    answer = 0
    
    board = [i*(i+1)/2 for i in range(n+1)]
    l, r = 0, 0
    
    while l <= n:
        cur = board[l] - board[r]
        
        if cur == n:
            answer += 1
            l += 1
            r += 1
        elif cur > n:
            r += 1
        else:
            l += 1
        
    return answer