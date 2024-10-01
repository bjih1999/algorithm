'''
N, M이 모두 20이하로 완전 탐색이 가능했던 문제

특정 컬럼을 넣거나 빼는 경우의 수를 모두 탐색해야한다는 것에서 착안하여,
컬럼을 선택하는 경우를 itertools combinations로 모두 취합


해당 경우가 유일성 최소성을 만족하는지 확인 (check 함수)
선택한 칼럼대로의 조합에서 중복을 제거했을때 n과 동일한지 체크 -> 유일성
기존에 선택한 칼럼 조합을 포함하는지 체크 -> 최소성

0, 1, 2, 3, 01... 0123 순으로 경우를 체크해나갔기 때문에,
유일성이 체크된 조합을 visited에 넣고 정규 표현식으로 이전 조합들이 포함되었는지 확인(ex. \d*\[0]\d*\[1]\d* -> 0과 1이 모두 포함된 데이터를 거를 수 있음)
'''

from itertools import combinations
import re

visited = []
def check(n, m, candi, relation):
    global visited
    
    result_set = set()
    for r in relation:
        result  = []
        for i in range(m):
            if i in candi:
                result.append(r[i])
        
        result_set.add(''.join(result))
    
    if len(result_set) != n:
        return
    
    temp = ''.join(list(map(str, candi)))
    for v in visited:
        pattern = []
        for row in v:
            pattern.append('([' + str(row) +'])')
        pattern = r'\d*' + r'\d*'.join(pattern) + r'\d*'
        print(pattern)
        if re.search(pattern, temp):
            return
            
    visited.append(temp)
    
def solution(relation):
    global visited
    n = len(relation)
    m = len(relation[0])
    indexes = [i for i in range(0, m)]
    
    candidates = []
    for i in range(1, m+1):
        candidates.extend(combinations(indexes, i))

    for candi in candidates:
        check(n, m, candi, relation)
    
    if not len(visited):
        return 1
    return len(visited)