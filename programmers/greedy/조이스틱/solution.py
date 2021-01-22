def _move_vertical(pos, count, name):
    if((ord(name[pos]) - ord('A') <= 13)):
        count[0] += ord(name[pos]) - ord('A')
        # print(ord(name[pos]) - ord('A'))
    else:
        count[0] += ord('Z') - ord(name[pos]) + 1
        # print(ord('Z') - ord(name[pos]) + 1)


def _move_horizon(pos, count, visited, name):
    
    _move_vertical(pos, count, name)

    while visited.count(0) > 0:
        distances = []
        for index, value in enumerate(visited):
            if value == 0:
                # print('!' ,abs(index - pos))
                # print('!' ,abs(((pos+1) + (index+2)) % len(name)))
                distances.append((index ,min(abs(index - pos), abs(((pos+1) + (index+1)) % len(name)))))
        
        # print(distances)
        distances = sorted(distances, key=lambda x:x[1])
        print(distances)
        visited[distances[0][0]] = 1
        pos = distances[0][0]
        count[0] += distances[0][1]
        # print(distances[0][1])

        _move_vertical(pos, count, name)
    

def solution(name):
    visited = [0 for x in range(len(name))]
    count = [0]
    answer = 0
    
    for x in range(len(name)):
        if name[x] == 'A':
            visited[x] = 1
    
    visited[0] = 1
    _move_horizon(0, count, visited, name)
    # print(count[0])

    return count[0]


# print(solution('JAN'))
# print('----------')
# print(solution('JEROEN'))
# print(solution('JAZ'))
print(solution('BBBAAAAAAAAAAB'))