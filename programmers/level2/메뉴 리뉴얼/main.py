from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    max_len = len(max(orders, key=lambda s:len(s)))
    
    for course in course:
        if max_len < course:
            continue
        combinations_list = []
        for order in orders:
            temp_list = list(combinations(list(order), course))
            temp_list = [tuple(sorted(comb)) for comb in temp_list]
            print(temp_list)
            combinations_list.extend(temp_list)
        
        counter = Counter(combinations_list).most_common()
        most_count = counter[0][1]
        most_counter = list(filter(lambda x:x[1] == most_count and x[1] >= 2, counter))
        for element in most_counter:
            answer.append("".join(element[0]))
    
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]		, [2,3,4]))
print(solution(["XYZ", "XWY", "WXA"]	, [2,3,4]))