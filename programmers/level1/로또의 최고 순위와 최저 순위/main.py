def solution(lottos, win_nums):
    answer = []
    
    lottos_set = set(lottos)
    win_nums_set = set(win_nums)
    
    min_match = len(lottos_set & win_nums_set)
    max_match = min_match + lottos.count(0)
    
    max_rank = 7 - max_match
    min_rank = 7 - min_match
    if max_rank > 6:
        max_rank = 6
    if min_rank > 6:
        min_rank = 6
    return [max_rank, min_rank]