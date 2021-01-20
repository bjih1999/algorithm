def solution(citations):
    answer = 0

    sorted_citations = sorted(citations, reverse=True)
    
    for count, citation in enumerate(sorted_citations):
        if len([x for x in sorted_citations if x >= count + 1]) >= count + 1:
            answer = count + 1

    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([100, 96]))
print(solution([47, 42, 32, 28, 24, 22, 17, 15, 10, 8]))