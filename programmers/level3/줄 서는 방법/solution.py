import itertools

def solution(n, k):
    answer = []
    pool = list(range(1, n+1))
    # print(pool)
    answer = list(itertools.permutations(pool))
    return list(answer[k-1])

print(solution(3, 5))