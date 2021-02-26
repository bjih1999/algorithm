def solution(seoul):

    for index,name in enumerate(seoul):
        if name == 'Kim':
            pos = index
            break
    answer = '김서방은 ' +str(pos)+'에 있다'

    return answer

print(solution(["Jane", "Kim"]))