def solution(citations):
    answer = 0

    sorted_citations = sorted(citations, reverse=True)
    
    for count, citation in enumerate(sorted_citations):
        if len([x for x in sorted_citations if x >= count + 1]) >= count + 1:
            answer = count + 1

    return answer