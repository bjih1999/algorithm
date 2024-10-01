'''
파싱 후 리스트 처리에 정석..


'''

def solution(s):
    
    s = s[1:-1].split('},{')
    s = [(current.replace('{', '').replace('}', '').split(',')) for current in s]
    s = sorted(s, key=lambda x:len(x))
    result = []
    result.extend(s[0])
    for i in range(1, len(s)):
        prev = s[i-1]
        cur = s[i]
        temp = []

        # 순서를 유지하면서 중복을 제거하는 테크닉이 쉬운데도 손이 선뜻가지 않더라..
        for c in cur:
            if c not in prev:
                temp.append(c)
        if temp:
            result.extend(temp)
    
    answer = []
    for r in result:
        answer.append(int(''.join(r)))
    return list(map(lambda x:int(''.join(str(x))), result))