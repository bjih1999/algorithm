import math
def solution(n,a,b):
    answer = 1

    while True:
        if abs(a-b) == 1 and math.ceil(a/2) == math.ceil(b/2):
            break
        
        if a % 2 == 0:
            a = a // 2
        else:
            a = (a+1) // 2
        
        if b % 2 == 0:
            b = b // 2
        else:
            b = (b+1) // 2
        answer += 1
    return answer