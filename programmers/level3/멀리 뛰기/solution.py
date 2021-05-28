def solution(n):
    prevprev = 1
    prev = 1
    current = 0
    if n <= 1:
        return 1
    for i in range(2, n+1):
        current = prevprev + prev
        prevprev = prev
        prev = current

    return current % 1234567