

def solution(m, n, puddles):
    map = []
    map.append([1 for _ in range(m)])

    for _ in range(1, n):
        row = [0 for _ in range(m)]
        row[0] = 1
        map.append(row)
    print(map)
    for i in range(n):
        for j in range(m):
            up = 0
            right = 0
            print(i, j)
            # print([i+1, j+1] in puddles)
            if [i+1, j+1] in puddles:
                # print(i+1, j+1)
                map[i][j] = 0
            else:
                if 1 < i < n:
                    up = map[i-1][j]
                if 0 < j < m-1:
                    right = map[i][j+1]
                map[i][j] = up + right
        print(map)
    return map[n-1][m-1]

print(solution(4, 3, [[2, 2]]))