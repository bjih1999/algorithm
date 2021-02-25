facto = {
    0:1,
    1:1,
    }

def _get_factorial(n):
    if n in facto.keys():
        return facto[n]
    else:
        i = max(facto.keys())
        result = facto[i]
        while i <= n :
            result *= i
            facto[i] = result
            i += 1

        return result

def _get_n_permutation(n, r):
    # print(n, r)
    # print(_get_factorial(n))
    # print(_get_factorial(r))
    # print('n-r', _get_factorial(n-r))
    # print(int(_get_factorial(n) / (_get_factorial(r) * _get_factorial(n-r))))
    return int(_get_factorial(n) / (_get_factorial(r) * _get_factorial(n-r)))

def _get_puddle_route(m, n, puddles):
    route_count = 0
    for puddle in puddles:
        route_count += _get_n_permutation((puddle[0]-1) + (puddle[1]-1), puddle[0]-1) * _get_n_permutation((m-puddle[0]) + (n-puddle[1]), m-puddle[0])
        # print('route', route_count)
    return route_count

def solution(m, n, puddles):
    answer = 0
    puddle_route = 0
    all_path = _get_n_permutation((m-1) + (n-1), m-1)
    # print('??', all_path)
    puddle_route = _get_puddle_route(m, n, puddles)
    # print('!!', puddle_route)
    return all_path - puddle_route

print(solution(4, 3, [[2, 2], [2, 3]]))
print(_get_factorial(0))