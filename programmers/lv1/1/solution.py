def solution(seoul):

    for index,name in enumerate(seoul):
        if name == 'Kim':
            pos = index
            break
    answer = '�輭���� ' +str(pos)+'�� �ִ�'

    return answer

print(solution(["Jane", "Kim"]))