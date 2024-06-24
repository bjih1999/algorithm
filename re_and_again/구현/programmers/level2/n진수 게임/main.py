def convert(k, n):
    result = ''
    hex_num = '0123456789ABCDEF'
    if k == 0:
        return '0'
    while k:
        temp = k % n
        if n >= 11:
            result += hex_num[temp]
        else:
            result += str(temp)
        k //= n
    return result[::-1]

def solution(n, t, m, p):
    result = ''
    i = 0
    last = t *m
    while len(result) <= last:
        result += convert(i, n)
        
        i += 1
    
    answer = ''
    for i in range(t):
        answer += result[p + i*m -1]
    return answer