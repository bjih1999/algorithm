def _get_pascal(n):
    depth = 0
    pascal_triangle = []

    while(depth <= n):
        # print(depth)
        row = []
        for pos in range(depth+1):
            if pos == 0 or pos == depth:
                row.append(1)
            else:
                row.append(pascal_triangle[depth-1][pos-1] + pascal_triangle[depth-1][pos])
        depth += 1
        pascal_triangle.append(row)
    # print(pascal_triangle)
    return pascal_triangle



def solution(n):
    answer = 0
    r = 0
    pascal_triangle = _get_pascal(n)
    while n >= r:
        answer += pascal_triangle[n][r]
        n -= 1
        r += 1
    return answer %  1000000007

print(solution(5))