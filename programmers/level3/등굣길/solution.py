

def solution(m, n, puddles):
    map = []

    for _ in range(n):
        row = [0 for _ in range(m)]
        map.append(row)
    map[0][0] = 1
    print(map)
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] not in puddles:
                map[i][j]
                if 0 < i < n:
                    map[i][j] += map[i-1][j]
                if 0 < j < m:
                    map[i][j] += map[i][j-1]
    print(map)
    return map[n-1][m-1]

# print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]))