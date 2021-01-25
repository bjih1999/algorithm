import copy

def _search(tile, n, answer):
    if sum(tile) == n:
        # print(tile)
        answer[0] += 1
        return

    elif sum(tile) > n:
        return

    else:
        case1 = copy.deepcopy(tile)
        case1.append(1)
        _search(case1, n, answer)
        case2 = copy.deepcopy(tile)
        case2.append(2)
        _search(case2, n, answer)


def solution(n):
    answer = [0]
    tile = []
    _search([1], n, answer)
    _search([2], n, answer)

    return answer[0] % 1000000007