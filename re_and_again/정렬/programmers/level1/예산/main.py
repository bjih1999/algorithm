def solution(d, budget):
    sorted_d = sorted(d)
    count = 0
    d_sum = 0
    for d in sorted_d:
        if d_sum + d > budget:
            break
        d_sum += d
        count += 1
    return count