from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    candidates = list(permutations(dungeons))

    for candidate in candidates:
        current = k
        count = 0
        for need, pay in candidate:
            if current < need:
                break
            count += 1
            current -= pay
        answer = max(answer, count)
    return answer