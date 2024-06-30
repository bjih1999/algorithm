def solution(n):
    ans = 0
    
    i = n
    
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i -= 1
            ans += 1

    return ans + 1