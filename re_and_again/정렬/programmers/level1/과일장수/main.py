'''
슬라이싱을 사용해서 score 데이터들을 줄여가는 코드를 짰었다
ex) score = scord[:-m]
이렇게 하니, 슬라이싱이 성능이 좋지 않아 시간 초과가 뜨더라.
슬라이싱이 성능이 좋지 않다는 것을 인지하고 앞으로 무분별한  슬라이싱 사용을 지양해야겠다.
'''

def solution(k, m, score):
    answer = 0
    cost = 0
    score = sorted(score)
    last = len(score)
    
    while last >= m:
        last -= m
        lowest_k = score[last]
        cost += lowest_k * m
    return cost