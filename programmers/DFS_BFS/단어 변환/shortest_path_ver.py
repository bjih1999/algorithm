'''다익스트라 알고리즘을 사용한 최단 경로를 구하는 버전
미완성 입니다.
'''
def _word_compare(target, dest):
    diff_count = 0
    if target == dest:
        return 0
    for i in range(len(target)):
        if target[i] != dest[i]:
            diff_count += 1
        
        if diff_count > 1:
            return 60
    
    return 1


def shortest_search(begin, target, words, matrix):
    start_points = []
    distance = []
    length = []
    not_visited = [x for x in range(len(words))]

    if target not in words:
        return 0
    else:
        target_index = words.index(target)
    
    for index, word in enumerate(words):
        if _word_compare(begin, word):
            start_points.append(index)

    for start in start_points:
        distance = matrix[start]

        w = 60
        for node_index in range(len(words)):
            # w = distance.index(min([distance[x] for x in not_visited]))    
            
            if node_index in not_visited:
                if distance[node_index] < w:
                    w = node_index
            

            print(not_visited)
            print(min([distance[x] for x in not_visited]))
            print(w)
            not_visited.remove(w)
            for i in not_visited:
                distance[i] = min(distance[i], distance[w] + matrix[w][i])
        
        length.append(distance[target_index])
    
    print(min(length))
    return min(length)


def solution(begin, target, words):
    answer = 0
    matrix = []
    for word in words:
        row = []
        for i in range(len(words)):
            row.append(_word_compare(word, words[i]))
        
        matrix.append(row)

    shortest_search(begin, target, words, matrix)


    return answer

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])