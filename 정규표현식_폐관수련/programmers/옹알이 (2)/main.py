import re

def solution(babbling):
    answer = 0
    result = []
    pattern1 = r'(aya|ye|woo|ma)\1+'
    pattern2 = r'^(aya|ye|woo|ma)+$'
    for b in babbling:
        if not re.search(pattern1, b) and re.search(pattern2, b):
            answer += 1
    return answer