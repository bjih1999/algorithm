import re

def solution(babbling):
    answer = 0
    pattern = '^(aya|ye|woo|ma)+$'
    # return str(re.match('(?:aya|ye|woo|ma)*', 'maa'))
    for b in babbling:
        if re.match(pattern, b) is not None:
            answer += 1
    return answer