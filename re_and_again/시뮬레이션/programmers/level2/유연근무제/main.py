'''
시간을 4자리 정수로 나타낸 문제
-> 모듈러 연산을 잘 처리해주었어야 함
ex) 1159의 10분 뒤 -> 1169 -> 1209
'''

def solution(schedules, timelogs, startday):
    n = len(schedules)
    
    startday = startday-1
    result = [True] * n
    
    for j, day in enumerate(range(startday, startday + 7)):
        if day % 7 == 5 or day % 7 == 6:
            continue
        
        for i in range(n):
            limit = schedules[i] + 10
            if limit % 100 >= 60:
                limit = (schedules[i] // 100 + 1) * 100 + limit % 100 - 60
            
            if timelogs[i][j] > limit:
                result[i] = False
        
        
    return len(list(filter(lambda x: x, result)))