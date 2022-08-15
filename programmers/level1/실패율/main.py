def solution(N, stages):
    rate = []
    count_per_stage = [0 for _ in range(N + 2)]
    accumlate = [0 for _ in range(N + 2)]
    total = len(stages)
    
    for stage in stages:
        count_per_stage[stage] += 1
    
    for stage, count in enumerate(count_per_stage):
        if 1 <= stage <= N:
            if total == 0:
                rate.append((stage, 0))
            else:
                rate.append((stage, count_per_stage[stage] / total))
                total -= count_per_stage[stage]
            
    sorted_stage = sorted(rate, key = lambda x: -x[1])
    answer = list(map(lambda x: x[0], sorted_stage))
    return answer