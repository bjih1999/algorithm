import re
from itertools import permutations

'''
permutation과 정규 표현식을 활용한 완전 탐색 풀이

n <= 8 * 8 이기 때문에,
O(n!) 풀이가 가능했다. 최대 O(8*7*6*5*4*3*2*1) => O(40320)

모든 아이디를 중복없이 순서를 고려하여 banned_id의 개수 만큼 뽑는 모든 케이스를 만듦(순열)
모든 케이스를 순회하며 banned_id의 정규 표현식에 맞는 케이스를 result에 추가함
이때, 뽑힌 아이디의 경우의수가 중복되는 것을 막기 위해 단어순 정렬을 하여 result에 추가함

result의 개수를 리턴.

'''
def solution(user_id, banned_id):
    board = {}
    result = set()
    length = len(banned_id)
    candidates = list(permutations(user_id, length))
    answer  = 0
    for candidate in candidates:
        is_match = True
        for c, b in zip(candidate, banned_id):
            pattern = b.replace('*', r'[0-9a-z]{1}')
            pattern = '^' + pattern + '$'
            if not re.match(pattern, c):
                is_match = False
                break
            
        if is_match:
            result.add(','.join(sorted(candidate)))
    return len(result)