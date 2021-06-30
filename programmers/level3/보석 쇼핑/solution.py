def solution(gems):
    
    start = 0
    end = 0
    res_start = start
    res_end = end
    N = len(gems)
    TYPE_NUM = len(set(gems))
    gem_state = {gems[0]:1}
    length = 999999
    while True:
        if len(gem_state) == TYPE_NUM:
            if length > end-start:
                length = end-start
                res_start = start
                res_end = end
        
        if len(gem_state) < TYPE_NUM:
            end += 1
            if end >= N:
                break
            if gems[end] in gem_state.keys():
                gem_state[gems[end]] += 1
            else:
                gem_state[gems[end]] = 1
        else:
            gem_state[gems[start]] -= 1
            if gem_state[gems[start]] == 0:
                del gem_state[gems[start]]
            start += 1
            if start >= N:
                break

    return [res_start + 1, res_end + 1]
                


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))