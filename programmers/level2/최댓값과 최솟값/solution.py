def solution(s):
    candidates = list(s.split(' '))
    numbers = list(map(lambda x: int(x), candidates))
    maximum = max(numbers)
    minimum = min(numbers)
    return str(minimum) + ' ' + str(maximum)