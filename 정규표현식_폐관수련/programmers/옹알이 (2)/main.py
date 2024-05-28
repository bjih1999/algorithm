import re

def solution(babbling):
    answer = 0
    result = []
    pattern = '^?!(aya{1}|ye{1}|woo{1}|ma{1})*$'
    for b in babbling:
        if re.match(pattern, b):
            answer += 1
            result.append(b)
    return result